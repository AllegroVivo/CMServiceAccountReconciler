from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, List, Type, Any, Dict, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from App.Classes import *
from .Models import *

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("MatchingRuleRepo", "ApplicationStateRepo")

################################################################################
class _RepoBase:

    def __init__(self, session: Session) -> None:
        self.s: Session = session

################################################################################
class MatchingRuleRepo(_RepoBase):

    def add(self, data: SheetRoutingRuleWrite) -> SheetRoutingRuleRead:

        new_rule = SheetRoutingRuleModel(**data.__dict__)

        self.s.add(new_rule)
        self.s.flush()
        self.s.refresh(new_rule)

        return new_rule.to_dataclass()

################################################################################
    def list_all(self) -> List[SheetRoutingRuleRead]:

        rules: List[SheetRoutingRuleModel] = self.s.scalars(  # type: ignore
            select(SheetRoutingRuleModel)
            .order_by(SheetRoutingRuleModel.priority.desc())
        ).all()
        return [rule.to_dataclass() for rule in rules]

################################################################################
    def update(self, rule_id: int, data: Dict[str, Any]) -> SheetRoutingRuleRead:

        existing: SheetRoutingRuleModel = self.s.get(SheetRoutingRuleModel, rule_id)  # type: ignore
        if existing is None:
            raise ValueError(f"Rule with ID {rule_id} does not exist.")

        for field, value in data.items():
            setattr(existing, field, value)

        self.s.flush()
        self.s.refresh(existing)

        return existing.to_dataclass()

################################################################################
    def remove(self, rule_id: int) -> None:

        existing: SheetRoutingRuleModel = self.s.get(SheetRoutingRuleModel, rule_id)  # type: ignore
        if existing is None:
            raise ValueError(f"Rule with ID {rule_id} does not exist.")

        self.s.delete(existing)
        self.s.flush()

################################################################################
class ApplicationStateRepo(_RepoBase):

    def create(self) -> ApplicationState:

        new_state = ApplicationStateModel()

        self.s.add(new_state)
        self.s.flush()
        self.s.refresh(new_state)

        return new_state.to_dataclass()

################################################################################
    def update_spreadsheet_id(self, key: int, data: str) -> ApplicationState:

        existing: ApplicationStateModel = self.s.get(ApplicationStateModel, key)  # type: ignore
        if existing:
            existing.spreadsheet_id = data

            self.s.flush()
            self.s.refresh(existing)

            return existing.to_dataclass()

        new_id = ApplicationStateModel(spreadsheet_id=data)

        self.s.add(new_id)
        self.s.flush()
        self.s.refresh(new_id)

        return new_id.to_dataclass()

################################################################################
    def update_last_run_date(self, key: int, last_run_date: date) -> ApplicationState:

        existing: ApplicationStateModel = self.s.get(ApplicationStateModel, key)  # type: ignore
        if existing is None:
            raise ValueError(f"Application state with ID {key} does not exist.")

        existing.last_run_date = last_run_date

        self.s.flush()
        self.s.refresh(existing)

        return existing.to_dataclass()

################################################################################
    def get(self) -> Optional[ApplicationState]:

        state: Optional[ApplicationStateModel] = self.s.scalar(select(ApplicationStateModel))
        return state.to_dataclass() if state is not None else None

################################################################################
