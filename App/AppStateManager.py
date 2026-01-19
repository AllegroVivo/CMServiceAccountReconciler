from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Optional

from Database import UnitOfWork
from .Classes import ApplicationState

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("AppStateManager",)

################################################################################
class AppStateManager:

    __slots__ = (
        "_state",
    )

################################################################################
    def __init__(self) -> None:

        self._state: ApplicationState = None  # type: ignore
        self.refresh()

################################################################################
    def refresh(self) -> None:

        with UnitOfWork() as db:
            self._state = db.app_state.get()
            if self._state is None:
                self._state = db.app_state.create()

        assert self._state is not None

        # TEMPORARY
        if self._state.last_run_date is None:
            self.update_last_run_date(date(2025, 8, 2))

################################################################################
    @property
    def spreadsheet_id(self) -> Optional[str]:

        return self._state.spreadsheet_id

################################################################################
    @property
    def last_run_date(self) -> Optional[date]:

        return self._state.last_run_date

################################################################################
    def update_spreadsheet_id(self, spreadsheet_id: str) -> str:

        if self.spreadsheet_id == spreadsheet_id:
            return self.spreadsheet_id

        with UnitOfWork() as db:
            self._state = db.app_state.update_spreadsheet_id(self._state.id, spreadsheet_id)
            return self.spreadsheet_id

################################################################################
    def update_last_run_date(self, new_last_run_date: date) -> date:

        if self.last_run_date == new_last_run_date:
            return self.last_run_date

        with UnitOfWork() as db:
            self._state = db.app_state.update_last_run_date(self._state.id, new_last_run_date)
            return self.last_run_date

################################################################################
