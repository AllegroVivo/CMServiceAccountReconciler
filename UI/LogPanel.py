from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from PySide6.QtWidgets import QWidget, QPlainTextEdit

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("LogPanel", )

################################################################################
class LogPanel(QPlainTextEdit):

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.setReadOnly(True)
        self.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self.document().setMaximumBlockCount(5000)

################################################################################
    def append_log(self, log_msg: str) -> None:

        self.appendPlainText(log_msg)

################################################################################
