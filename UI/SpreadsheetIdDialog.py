from __future__ import annotations

import re
from typing import Optional

from PySide6.QtWidgets import (
    QDialog, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QDialogButtonBox
)
################################################################################

__all__ = ("SpreadsheetIdDialog", )

################################################################################
class SpreadsheetIdDialog(QDialog):

    def __init__(self, spreadsheet_id: Optional[str], parent=None) -> None:
        super().__init__(parent)

        self._sid: Optional[str] = spreadsheet_id

        self.setModal(True)
        self.resize(500, 90)

        self._setup_ui()

################################################################################
    def _setup_ui(self) -> None:

        layout = QVBoxLayout()

        sid_layout = QHBoxLayout()
        sid_text = QLabel("Spreadsheet ID:")
        sid_layout.addWidget(sid_text)
        self._spreadsheet_id = QLineEdit()
        self._spreadsheet_id.setPlaceholderText("Paste Google Spreadsheet Link or ID")
        self._spreadsheet_id.setClearButtonEnabled(True)
        self._spreadsheet_id.setText(self._sid)
        sid_layout.addWidget(self._spreadsheet_id)
        layout.addLayout(sid_layout)

        self._buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel,
            parent=self
        )
        self._buttons.accepted.connect(self.accept)
        self._buttons.rejected.connect(self.reject)
        layout.addWidget(self._buttons)

        self.setLayout(layout)

################################################################################
    def spreadsheet_id(self) -> Optional[str]:

        sid = self._spreadsheet_id.text().strip()
        if "/" in sid:
            gsheet_re = re.compile(
                r"https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)"
            )
            match = gsheet_re.search(sid)
            if match:
                sid = match.group(1)

        self._sid = sid
        return self._sid

################################################################################
    @staticmethod
    def get_spreadsheet_id(spreadsheet_id: Optional[str], parent=None) -> Optional[str]:

        dialog = SpreadsheetIdDialog(spreadsheet_id, parent)
        result = dialog.exec()
        if result == QDialog.DialogCode.Accepted:
            return dialog.spreadsheet_id()

################################################################################
