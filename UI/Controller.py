from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import TYPE_CHECKING, Optional, Dict, Any

from PySide6.QtCore import QObject, QThread, Slot
from PySide6.QtWidgets import QMessageBox

from App.AppStateManager import AppStateManager
from App.RuleManager import RoutingRuleManager
from .RulesDialog import RoutingRulesDialog
from .Worker import ReconciliationWorker

if TYPE_CHECKING:
    from .MainWindow import MainWindow
    from App.Classes import RunStats, IssueRow, SheetRoutingRuleWrite
################################################################################

__all__ = ("ReconciliationController", )

################################################################################
class ReconciliationController(QObject):

    def __init__(self, main_window: MainWindow) -> None:
        super().__init__()

        self._win: MainWindow = main_window
        self._thread: Optional[QThread] = None
        self._worker: Optional[ReconciliationWorker] = None

        self._rule_mgr: RoutingRuleManager = RoutingRuleManager()
        self._app_state: AppStateManager = AppStateManager()
        self._win.set_spreadsheet_id(self._app_state.spreadsheet_id)

        self._win.loaded.connect(self.op_application_loaded)
        self._win.run_requested.connect(self.start_run)
        self._win.stop_requested.connect(self.stop_run)
        self._win.rules_requested.connect(self.open_rules)
        self._win.date_change_requested.connect(self.change_date)
        self._win.spreadsheet_id_changed.connect(self.change_spreadsheet_id)

################################################################################
    @Slot()
    def op_application_loaded(self) -> None:

        self._win.append_log("[Controller] Application loaded.")
        if self._app_state.last_run_date is not None:
            self._win.append_log(f"[Controller] Last reconciliation date: {self._app_state.last_run_date.strftime('%m-%d-%Y')}.")
        else:
            self._win.append_log("[Controller] No last reconciliation date stored.")

################################################################################
    @Slot(str, str, bool)
    def start_run(self, spreadsheet_id: str, qb_csv_path: Path, dry_run: bool, run_date: date) -> None:

        if self._thread is not None:
            self._win.append_log("[Controller] Run requested but already running.")
            return

        self._win.append_log("[Controller] Starting run...")
        self._win.set_running(True)

        self._thread = QThread()

        if self._app_state.last_run_date is not None:
            if self._app_state.last_run_date >= run_date:
                self._win.append_log(
                    "[Controller] Warning: The selected run date is earlier than or equal to "
                    "the last reconciliation date."
                )
                resp = QMessageBox.question(
                    self._win,
                    "Reconciliation Date Flagged",
                    (
                        "The selected date is earlier than the last reconciliation date. Continuing will most "
                        "likely lead to data inconsistencies and is highly inadvisable! Do you want to proceed?"
                    ),
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No
                )
                if resp == QMessageBox.StandardButton.No:
                    self._win.append_log("[Controller] Run cancelled by user due to date inconsistency.")
                    self._on_finished(False, "Run cancelled by user.", None)
                    return
            else:
                self._win.append_log(
                    f"[Controller] Most recent reconciliation date: {self._app_state.last_run_date.strftime('%m-%d-%Y')}. "
                    f"Updating to {run_date.strftime('%m-%d-%Y')}..."
                )

        self._worker = ReconciliationWorker(
            spreadsheet_id=spreadsheet_id,
            qb_csv_path=qb_csv_path,
            dry_run=dry_run,
            rule_mgr=self._rule_mgr,
            run_date=run_date,
            last_run_date=self._app_state.last_run_date,
        )
        self._worker.moveToThread(self._thread)

        # Wire the worker to the UI
        self._worker.log_line.connect(self._win.append_log)
        self._worker.phase_changed.connect(self._win.set_phase)
        self._worker.progress_busy.connect(self._win.set_progress_busy)
        self._worker.finished.connect(self._on_finished)

        # Start/Stop lifecycle
        self._thread.started.connect(self._worker.run)
        self._worker.finished.connect(self._thread.quit)
        self._thread.finished.connect(self._cleanup)

        self._thread.start()

################################################################################
    @Slot()
    def stop_run(self) -> None:

        if self._worker is None:
            return

        self._win.append_log("[Controller] Stop requested → worker cancel flag set.")
        self._worker.request_cancel()

################################################################################
    @Slot(bool, str, date)
    def _on_finished(self, success: bool, message: str, run_date: Optional[date]) -> None:

        if run_date and self._app_state.last_run_date is not None and self._app_state.last_run_date.strftime("%m-%d-%Y") != run_date.strftime("%m-%d-%Y"):
            self._win.append_log(
                f"[Controller] Note: The last run date was {self._app_state.last_run_date.strftime('%m-%d-%Y')}."
            )
            self._win.append_log(f"[Controller] Updating last run date to {run_date.strftime("%m-%d-%Y")}.")
            self._app_state.update_last_run_date(run_date)

        self._win.append_log(f"[Controller] Finished: {message}")
        self._win.set_phase(message, 100 if success else 0)
        self._win.set_running(False)
        self._cleanup()

################################################################################
    @Slot()
    def _cleanup(self) -> None:

        self._worker = None
        if self._thread is not None:
            self._thread.deleteLater()
        self._thread = None

################################################################################
    @Slot()
    def open_rules(self) -> None:

        if self._thread is not None:
            self._win.append_log("[Controller] Cannot edit rules while a run is in progress!")
            return

        dlg = RoutingRulesDialog(parent=self._win)
        self._rules_dlg = dlg
        dlg.finished.connect(lambda: setattr(self, "_rules_dlg", None))
        dlg.set_rules(self._rule_mgr.list_rules())

        dlg.create_rule_requested.connect(self._on_rule_create)
        dlg.update_rule_requested.connect(self._on_rule_update)
        dlg.delete_rule_requested.connect(self._on_rule_delete)

        dlg.exec()

################################################################################
    @Slot(object)
    def _on_rule_create(self, rule: SheetRoutingRuleWrite) -> None:

        try:
            self._rule_mgr.create_rule(rule)
            self._win.append_log(f"[Rules] Created new rule: {rule.name}.")
        except Exception as ex:
            self._win.append_log(f"[Rules] Failed to add rule: {ex}.")

        self._rules_dlg.set_rules(self._rule_mgr.list_rules())

################################################################################
    @Slot(int, object)
    def _on_rule_update(self, rule_id: int, data: Dict[str, Any], emit_log: bool) -> None:

        try:
            updated = self._rule_mgr.update_rule(rule_id, data)
            if emit_log:
                self._win.append_log(f"[Rules] Updated rule: {updated.name}.")
        except Exception as ex:
            self._win.append_log(f"[Rules] Failed to update rule ID {rule_id}: {ex}.")

        self._rules_dlg.set_rules(self._rule_mgr.list_rules())

################################################################################
    @Slot(int)
    def _on_rule_delete(self, rule_id: int) -> None:

        try:
            self._rule_mgr.delete_rule(rule_id)
            old_rule = self._rules_dlg._original_by_id[rule_id]
            self._win.append_log(f"[Rules] Deleted rule: {old_rule["name"]}.")
        except Exception as ex:
            self._win.append_log(f"[Rules] Failed to delete rule ID {rule_id}: {ex}.")

        self._rules_dlg.set_rules(self._rule_mgr.list_rules())

################################################################################
    @Slot(date)
    def change_date(self, new_date: date) -> None:

        if self._thread is not None:
            self._win.append_log("[Controller] Cannot change date while a run is in progress!")
            return

        self._app_state.update_last_run_date(new_date)
        self._win.append_log(f"[Controller] Updated last run date to {new_date.strftime('%m-%d-%Y')}.")

################################################################################
    @Slot(str)
    def change_spreadsheet_id(self, new_id: str) -> None:

        if self._thread is not None:
            self._win.append_log("[Controller] Cannot change Spreadsheet ID while a run is in progress!")
            return

        self._app_state.update_spreadsheet_id(new_id)
        self._win.append_log(f"[Controller] Updated stored Spreadsheet ID to {new_id}.")

################################################################################
