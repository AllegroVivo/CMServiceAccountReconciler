from __future__ import annotations

import re
from datetime import date
from pathlib import Path
from typing import TYPE_CHECKING

from PySide6.QtCore import Signal, QTimer
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel, QProgressBar, QStatusBar, QLineEdit,
    QStyle, QFileDialog, QMessageBox, QHBoxLayout, QPushButton, QFormLayout,
)

from .LogPanel import LogPanel
from .DatePickerDialog import DatePickerDialog

if TYPE_CHECKING:
    from App.Classes import IssueRow
################################################################################

__all__ = ("MainWindow", )

################################################################################
class MainWindow(QMainWindow):

    loaded = Signal()
    run_requested = Signal(str, str, bool, date)  # spreadsheet_id, qb_csv_path, dry_run, run_date
    rules_requested = Signal()
    stop_requested = Signal()
    date_change_requested = Signal(date)

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Service Membership Auto-Reconciler")
        self.resize(550, 400)

        self._setup_ui()

        QTimer.singleShot(0, self.loaded.emit)

################################################################################
    def _setup_ui(self) -> None:

        self._setup_toolbar()

        # --- Central Widget ---
        central = QWidget()
        self.setCentralWidget(central)
        central_layout = QVBoxLayout(central)
        central_layout.setContentsMargins(8, 8, 8, 8)
        central_layout.setSpacing(8)

        # --- Top Pane ---
        top_layout = QHBoxLayout()
        inputs_layout = QFormLayout()

        self._spreadsheet_id = QLineEdit()
        self._spreadsheet_id.setPlaceholderText("Paste Google Spreadsheet Link or ID")
        self._spreadsheet_id.setClearButtonEnabled(True)
        inputs_layout.addRow("Spreadsheet URL:", self._spreadsheet_id)

        qb_layout = QHBoxLayout()
        self._qb_path = QLineEdit()
        self._qb_path.setPlaceholderText("Select QuickBooks CSV Export")
        self._qb_path.setReadOnly(True)
        qb_layout.addWidget(self._qb_path)
        browse = QPushButton("Browse...", self)
        browse.clicked.connect(self._on_browse_qb)
        browse.setFixedWidth(70)
        qb_layout.addWidget(browse)
        inputs_layout.addRow("QuickBooks CSV:", qb_layout)

        top_layout.addLayout(inputs_layout)

        btns_layout = QVBoxLayout()

        # self._rules_btn = QPushButton("Routing Rules", self)
        # self._rules_btn.clicked.connect(self.rules_requested.emit)
        # btns_layout.addWidget(self._rules_btn)

        self._run_action = QPushButton("Run", self)
        self._run_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        self._run_action.clicked.connect(self._on_run_clicked)
        btns_layout.addWidget(self._run_action)

        # self._stop_action = QPushButton("Stop", self)
        # self._stop_action.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaStop))
        # self._stop_action.setEnabled(False)
        # self._stop_action.clicked.connect(self._on_stop_clicked)
        # btns_layout.addWidget(self._stop_action)

        top_layout.addLayout(btns_layout)
        central_layout.addLayout(top_layout)

        # --- Log Panel ---
        self._log = LogPanel()
        central_layout.addWidget(self._log)

        # --- Status Bar ---
        self._phase_label = QLabel("Idle")
        self._progress = QProgressBar()
        self._progress.setRange(0, 100)
        self._progress.setValue(0)
        self._progress.setTextVisible(True)
        self._progress.setFixedWidth(280)

        status = QStatusBar()
        status.addPermanentWidget(self._phase_label, 1)
        status.addPermanentWidget(self._progress, 0)
        status.setContentsMargins(8, 0, 0, 10)
        self.setStatusBar(status)

################################################################################
    def _setup_toolbar(self) -> None:

        menubar = self.menuBar()

        admin_bar = menubar.addMenu("&Admin Actions")

        change_run_date_action = admin_bar.addAction("Change Last Reconcile Date")
        change_run_date_action.triggered.connect(self._change_run_date)

        routing_rules_action = admin_bar.addAction("Routing Rules")
        routing_rules_action.triggered.connect(self._request_rules)

        admin_bar.addAction(change_run_date_action)
        admin_bar.addAction(routing_rules_action)

################################################################################
    def _change_run_date(self) -> None:

        resp = QMessageBox.question(
            self,
            "Administrator Action Confirmation",
            (
                "Changing the 'Last Reconcile Date' may affect how records are processed during reconciliation.\n\n"
                
                "Only change this if you know what you're doing. :)\n\n"
            
                "Are you sure you want to proceed?"
            ),
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if resp != QMessageBox.StandardButton.Yes:
            self.append_log("[UI] Change Last Reconcile Date cancelled by user.")
            return

        new_date = DatePickerDialog.get_date()
        if new_date:
            self.append_log(f"[UI] Change Last Reconcile Date requested: {new_date.strftime('%m-%d-%Y')}.")
            self.date_change_requested.emit(new_date)

################################################################################
    def _request_rules(self) -> None:

        resp = QMessageBox.question(
            self,
            "Administrator Action Confirmation",
            (
                "Accessing the Routing Rules allows you to modify how records are categorized during reconciliation.\n\n"
                
                "Only modify these rules if you understand their impact on the reconciliation process.\n\n"
            
                "Are you sure you want to proceed?"
            ),
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if resp != QMessageBox.StandardButton.Yes:
            return

        self.rules_requested.emit()

################################################################################
    def _on_browse_qb(self) -> None:

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select QuickBooks CSV Export",
            str(Path.home()),
            "CSV Files (*.csv)"
        )
        if file_path:
            self._qb_path.setText(file_path)

################################################################################
    def _on_run_clicked(self) -> None:

        spreadsheet_id = self._spreadsheet_id.text().strip()
        if "/" in spreadsheet_id:
            gsheet_re = re.compile(
                r"https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)"
            )
            match = gsheet_re.search(spreadsheet_id)
            if match:
                spreadsheet_id = match.group(1)

        qb_path = self._qb_path.text().strip()
        # dry = self._dry_run.isChecked()
        dry = False

        if not spreadsheet_id:
            QMessageBox.warning(self, "Missing Spreadsheet ID", "Please enter a spreadsheet ID.")
            return
        if not qb_path:
            QMessageBox.warning(self, "Missing QB CSV", "Please select a QuickBooks CSV export.")
            return

        reconciled_thru = DatePickerDialog.get_date()
        if not reconciled_thru:
            self.append_log("[UI] Run cancelled: No 'Reconciled Thru' date selected.")
            return

        self.set_running(True)
        self.set_phase("Starting...", 0)

        self.run_requested.emit(spreadsheet_id, qb_path, dry, reconciled_thru)

################################################################################
    def _on_stop_clicked(self) -> None:

        self.stop_requested.emit()
        self.append_log("[UI] Stop requested...")

################################################################################
    def set_running(self, is_running: bool) -> None:

        self._run_action.setEnabled(not is_running)
        # self._rules_btn.setEnabled(not is_running)
        # self._stop_action.setEnabled(is_running)

################################################################################
    def set_progress_busy(self, busy: bool) -> None:

        self._progress.setRange(0, 0 if busy else 100)

################################################################################
    def set_phase(self, phase: str, progress_pct: int) -> None:

        self._phase_label.setText(f"Phase: {phase}")
        self._progress.setValue(max(0, min(100, progress_pct)))

################################################################################
    def append_log(self, line: str) -> None:

        self._log.append_log(line)

################################################################################
    def set_spreadsheet_id(self, spreadsheet_id: str) -> None:

        self._spreadsheet_id.setText(spreadsheet_id)

################################################################################
