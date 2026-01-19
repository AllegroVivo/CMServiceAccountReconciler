from __future__ import annotations

from typing import List, Optional

from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtWidgets import QComboBox, QStyledItemDelegate, QWidget, QDoubleSpinBox

################################################################################

__all__ = ("SheetComboDelegate", "OptionalAmountSpinDelegate")

################################################################################
class SheetComboDelegate(QStyledItemDelegate):

    def __init__(self, sheets: List[str], parent=None) -> None:
        super().__init__(parent)

        self._sheets = sheets.copy()

################################################################################
    def createEditor(self, parent: QWidget, _, index: QModelIndex) -> QWidget:

        combo = QComboBox(parent)
        combo.setEditable(False)
        combo.addItems(self._sheets)
        return combo

################################################################################
    def setEditorData(self, editor: QWidget, index: QModelIndex) -> None:

        combo: QComboBox = editor  # type: ignore
        current = str(index.data(Qt.ItemDataRole.EditRole) or "")
        idx = combo.findText(current)
        combo.setCurrentIndex(idx if idx >= 0 else 0)

################################################################################
    def setModelData(self, editor: QWidget, _, index: QModelIndex) -> None:

        combo: QComboBox = editor  # type: ignore
        index.model().setData(index, combo.currentText(), Qt.ItemDataRole.EditRole)

################################################################################
class OptionalAmountSpinDelegate(QStyledItemDelegate):

    def __init__(
        self,
        parent: Optional[QWidget] = None,
        *,
        minimum: float = 0.0,
        maximum: float = 1_000_000_000.0,
        decimals: int = 2,
        step: float = 1.0
    ) -> None:
        super().__init__(parent)

        self._min: float = minimum
        self._max: float = maximum
        self._decimals: int = decimals
        self._step: float = step

################################################################################
    def createEditor(self, parent: QWidget, _, index: QModelIndex) -> QWidget:

        spin = QDoubleSpinBox(parent)
        spin.setRange(self._min, self._max)
        spin.setDecimals(self._decimals)
        spin.setSingleStep(self._step)
        spin.setSpecialValueText("N/A")
        spin.setAccelerated(True)
        spin.setKeyboardTracking(False)
        spin.setFrame(False)
        return spin

################################################################################
    def setEditorData(self, editor: QWidget, index: QModelIndex) -> None:

        spin: QDoubleSpinBox = editor  # type: ignore
        raw = index.data(Qt.ItemDataRole.EditRole)

        if raw in (None, "", "N/A"):
            spin.setValue(0.0)
            spin.setProperty("_was_none", True)
        else:
            spin.setProperty("_was_none", False)
            spin.setValue(float(raw))

################################################################################
    def setModelData(self, editor: QWidget, model, index: QModelIndex) -> None:

        spin: QDoubleSpinBox = editor  # type: ignore
        value = float(spin.value())

        was_none = bool(spin.property("_was_none"))
        if was_none and value == 0.0:
            model.setData(index, "", Qt.ItemDataRole.EditRole)
        else:
            model.setData(index, value, Qt.ItemDataRole.EditRole)

################################################################################
