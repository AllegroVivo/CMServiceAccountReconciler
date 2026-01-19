from __future__ import annotations

from typing import List, Optional, Any

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from App.Classes import SheetRoutingRuleRead
################################################################################

__all__ = ("RoutingRulesTableModel", )

################################################################################
class RoutingRulesTableModel(QAbstractTableModel):

    HEADERS = ("Name", "Sheet", "Min. Amount", "Max. Amount")

    def __init__(self, sheet_names: List[str], rules: Optional[List[SheetRoutingRuleRead]] = None) -> None:
        super().__init__()

        self._sheet_names: List[str] = sheet_names
        self._rules: List[SheetRoutingRuleRead] = rules or []

################################################################################
    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:

        return 0 if parent.isValid() else len(self._rules)

################################################################################
    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:

        return 0 if parent.isValid() else len(self.HEADERS)

################################################################################
    def headerData(self, section: int, orientation: Qt.Orientation, role = Qt.ItemDataRole.DisplayRole) -> Optional[str]:

        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self.HEADERS[section]
        return None

################################################################################
    def data(self, index: QModelIndex, role: Qt.ItemDataRole = Qt.ItemDataRole.DisplayRole) -> Any:

        if not index.isValid():
            return None

        rule = self._rules[index.row()]
        col = index.column()

        if role in (Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole):
            if col == 0:
                return rule.name
            elif col == 1:
                return rule.sheet
            elif col == 2:
                return f"{rule.min_amount:.2f}" if rule.min_amount is not None else "N/A"
            elif col == 3:
                return f"{rule.max_amount:.2f}" if rule.max_amount is not None else "N/A"

        return None

################################################################################
    def flags(self, index: QModelIndex) -> Qt.ItemFlag:

        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        # noinspection PyTypeChecker
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable

################################################################################
    def setData(self, index: QModelIndex, value: Any, role: int = Qt.ItemDataRole.EditRole) -> bool:

        if role != Qt.ItemDataRole.EditRole or not index.isValid():
            return False

        rule = self._rules[index.row()]
        col = index.column()

        try:
            match col:
                case 0:
                    new = rule.__dict__ | {"name": str(value).strip()}
                case 1:
                    sheet = str(value).strip()
                    if sheet not in self._sheet_names:
                        return False
                    new = rule.__dict__ | {"sheet": sheet}
                case 2:
                    if value in (None, "", "N/A"):
                        min_amount = None
                    else:
                        min_amount = float(value)
                    new = rule.__dict__ | {"min_amount": min_amount}
                case 3:
                    if value in (None, "", "N/A"):
                        max_amount = None
                    else:
                        max_amount = float(value)
                    new = rule.__dict__ | {"max_amount": max_amount}
                case _:
                    return False
        except ValueError:
            return False

        # noinspection PyUnboundLocalVariable
        self._rules[index.row()] = SheetRoutingRuleRead(**new)
        self.dataChanged.emit(index, index)

        return True

################################################################################
    def set_rules(self, rules: List[SheetRoutingRuleRead]) -> None:

        self.beginResetModel()
        self._rules = rules
        self.endResetModel()

################################################################################
    def get_rules(self) -> List[SheetRoutingRuleRead]:

        return self._rules

################################################################################
    def add_empty_rule(self) -> None:

        self.beginInsertRows(QModelIndex(), len(self._rules), len(self._rules))
        self._rules.append(
            SheetRoutingRuleRead(
                id=-1,
                name="New Rule",
                sheet="",
                min_amount=None,
                max_amount=None
            )
        )
        self.endInsertRows()

################################################################################
    def remove_row(self, row: int) -> Optional[SheetRoutingRuleRead]:

        if 0 <= row < len(self._rules):
            self.beginRemoveRows(QModelIndex(), row, row)
            removed = self._rules.pop(row)
            self.endRemoveRows()
            return removed

        return None

################################################################################
