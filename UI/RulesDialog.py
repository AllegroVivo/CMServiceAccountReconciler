from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QTableView, QMessageBox,
    QHeaderView, QAbstractItemView
)

from App.Classes import SheetRoutingRuleRead, SheetRoutingRuleWrite
from .RulesTableModel import RoutingRulesTableModel
from .Delegates import SheetComboDelegate, OptionalAmountSpinDelegate
################################################################################

__all__ = ("RoutingRulesDialog", )

SHEETS = ["Annual", "Monthly", "Plumbing - Annual", "Generator", "Duct Cleaning"]

################################################################################
class RoutingRulesDialog(QDialog):
    
    create_rule_requested = Signal(SheetRoutingRuleWrite)
    update_rule_requested = Signal(int, dict, bool)  # rule id, data, emit log
    delete_rule_requested = Signal(int)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setWindowTitle("Routing Rules")
        self.resize(550, 350)

        self._model = RoutingRulesTableModel(SHEETS)

        self._table = QTableView()
        self._table.setModel(self._model)

        self._table.setItemDelegateForColumn(1, SheetComboDelegate(SHEETS, self._table))
        self._table.setItemDelegateForColumn(2, OptionalAmountSpinDelegate(self._table))
        self._table.setItemDelegateForColumn(3, OptionalAmountSpinDelegate(self._table))

        self._table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self._table.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self._table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self._table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        # noinspection PyTypeChecker
        self._table.setEditTriggers(
            QAbstractItemView.EditTrigger.DoubleClicked |
            QAbstractItemView.EditTrigger.SelectedClicked |
            QAbstractItemView.EditTrigger.EditKeyPressed
        )

        add_btn = QPushButton("Add")
        remove_btn = QPushButton("Remove")
        close_btn = QPushButton("Close")

        add_btn.clicked.connect(self._on_add)
        remove_btn.clicked.connect(self._on_remove)
        close_btn.clicked.connect(self.accept)

        button_layout = QHBoxLayout()
        button_layout.addWidget(add_btn)
        button_layout.addWidget(remove_btn)
        button_layout.addStretch(1)
        button_layout.addWidget(close_btn)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self._table)
        main_layout.addLayout(button_layout)

################################################################################
    def _on_add(self) -> None:

        self._model.add_empty_rule()
        idx = self._model.index(self._model.rowCount() - 1, 0)
        self._table.setCurrentIndex(idx)
        self._table.edit(idx)

################################################################################
    def _on_remove(self) -> None:

        idx = self._table.currentIndex()
        if not idx.isValid():
            QMessageBox.warning(self, "No Selection", "Please select a rule to remove.")
            return

        rule = self._model.get_rules()[idx.row()]
        if rule.name != "New Rule" and rule.sheet in (None, "", "N/A"):
            resp = QMessageBox.question(
                self,
                "Confirm Removal",
                f"Are you sure you want to remove rule: '{rule.name}'?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            if resp != QMessageBox.StandardButton.Yes:
                return

        rule = self._model.remove_row(idx.row())
        if rule and rule.id != -1:
            self.delete_rule_requested.emit(rule.id)

################################################################################
    def set_rules(self, rules: list[SheetRoutingRuleRead]) -> None:

        self._original_by_id = {
            r.id: {"name": r.name, "sheet": r.sheet, "min_amount": r.min_amount, "max_amount": r.max_amount}
            for r in rules
            if r.id != -1
        }
        self._model.set_rules(rules)

################################################################################
    def accept(self) -> None:

        for rule in self._model.get_rules():
            data = {
                "name": rule.name,
                "sheet": rule.sheet,
                "min_amount": rule.min_amount,
                "max_amount": rule.max_amount
            }

            original = self._original_by_id.get(rule.id)
            is_dirty = (original != data)

            if rule.id == -1:
                self.create_rule_requested.emit(SheetRoutingRuleWrite(**data))
            else:
                self.update_rule_requested.emit(rule.id, data, is_dirty)

        super().accept()

################################################################################
