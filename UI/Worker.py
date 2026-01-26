from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import TYPE_CHECKING, Optional

from PySide6.QtCore import Signal, QObject, Slot

from App.Reconciler import ServiceReconciler

if TYPE_CHECKING:
    from App.RuleManager import RoutingRuleManager
################################################################################

__all__ = ("ReconciliationWorker", )

################################################################################
class ReconciliationWorker(QObject):

    phase_changed = Signal(str, int)  # phase name, progress percent
    progress_busy = Signal(bool)  # is busy
    log_line = Signal(str)  # log message
    finished = Signal(bool, str, date)  # success, error message, run_date

    def __init__(
        self,
        spreadsheet_id: str,
        qb_csv_path: Path,
        dry_run: bool,
        rule_mgr: RoutingRuleManager,
        run_date: date,
        last_run_date: Optional[date],
    ) -> None:
        super().__init__()

        self._spreadsheet_id: str = spreadsheet_id
        self._qb_csv_path: Path = qb_csv_path
        self._dry_run: bool = dry_run
        self._cancel_requested = False
        self._run_date: date = run_date
        self._last_run_date: Optional[date] = last_run_date

        self._rule_mgr: RoutingRuleManager = rule_mgr

################################################################################
    @Slot()
    def request_cancel(self) -> None:

        self._cancel_requested = True

################################################################################
    def _check_cancel(self) -> bool:

        if self._cancel_requested:
            self.log_line.emit("[Worker] Cancel requested. Stopping after current phase.")
            self.finished.emit(False, "Cancelled by user.", None)
            return True
        return False

################################################################################
    @Slot()
    def run(self) -> None:

        reconciler = ServiceReconciler(self._rule_mgr)
        try:
            # Phase 1: Load Data
            self.phase_changed.emit("Loading spreadsheet...", 5)
            self.progress_busy.emit(True)
            self.log_line.emit("[1/4] Loading and parsing spreadsheet payload...")
            reconciler.load_data(self._spreadsheet_id, self._last_run_date)
            if self._check_cancel():
                return
            # Phase 2: Load QB CSV
            self.progress_busy.emit(False)
            self.phase_changed.emit("Parsing QuickBooks CSV...", 15)
            self.log_line.emit("[2/4] Loading and parsing QuickBooks export CSV...")
            reconciler.load_qb_export(Path(self._qb_csv_path))
            if self._check_cancel():
                return

            # Phase 3: Reconciliation
            self.phase_changed.emit("Reconciling...", 25)
            self.log_line.emit("[3/4] Reconciling QB records into sheet records...")
            reconciler.reconcile_all(self.phase_changed, self.log_line)
            if self._check_cancel():
                return

            # Phase 4: Writeback
            if self._dry_run:
                self.phase_changed.emit("Complete.", 100)
                self.log_line.emit("[4/4] Dry run complete. No changes written.")
            else:
                self.phase_changed.emit("Writing back. Please Wait...", 90)
                self.progress_busy.emit(True)
                self.log_line.emit("[4/4] Writing changes back to spreadsheet. This may take several moments...")
                reconciler.write_to_destination(self._run_date.strftime("%m-%d-%Y"))
                self.progress_busy.emit(False)
                self.phase_changed.emit("Done!", 100)
                self.log_line.emit("[4/4] Changes written to spreadsheet.")

            self.finished.emit(True, "Done!", self._run_date)

        except Exception as ex:
            self.log_line.emit(f"[Worker] Fatal error: {ex!r}")
            self.finished.emit(False, f"Failed: {ex!r}", self._run_date)

################################################################################
