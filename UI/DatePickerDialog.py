from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import TYPE_CHECKING, Optional

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog, QCalendarWidget, QDialogButtonBox, QVBoxLayout

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("DatePickerDialog", )

################################################################################
@dataclass
class DatePickerResult:
    """Class representing the result of a date picker dialog."""

    accepted: bool
    date: Optional[QDate] = None

################################################################################
class DatePickerDialog(QDialog):

    def __init__(self, parent=None, *, initial: Optional[QDate] = None) -> None:
        super().__init__(parent)

        self.setWindowTitle("Select Date")
        self.resize(300, 200)
        self.setModal(True)

        self._calendar = QCalendarWidget(self)
        self._calendar.setGridVisible(True)

        if initial:
            self._calendar.setSelectedDate(initial)

        self._buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel,
            parent=self
        )
        self._buttons.accepted.connect(self.accept)
        self._buttons.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self._calendar)
        layout.addWidget(self._buttons)

        self.setLayout(layout)

################################################################################
    def selected_date(self) -> QDate:
        """Get the currently selected date from the calendar widget."""
        return self._calendar.selectedDate()

################################################################################
    @staticmethod
    def get_date(parent=None, *, initial: Optional[QDate] = None) -> Optional[date]:
        """Static method to show the date picker dialog and return the result."""
        dialog = DatePickerDialog(parent, initial=initial)
        result = dialog.exec()
        if result == QDialog.DialogCode.Accepted:
            return dialog.selected_date().toPython()  # type: ignore

################################################################################
