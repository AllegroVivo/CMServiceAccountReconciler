from __future__ import annotations

from typing import Callable

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .Engine import SessionLocal
from .Repositories import *
################################################################################

__all__ = ("UnitOfWork", )

################################################################################
class UnitOfWork:

    def __init__(self, session_factory: Callable[[], Session] = SessionLocal):

        self._factory: Callable[[], Session] = session_factory
        self._session: Session = None  # type: ignore

        self._rules: MatchingRuleRepo = None  # type: ignore
        self.app_state: ApplicationStateRepo = None  # type: ignore

################################################################################
    def __enter__(self) -> UnitOfWork:

        self._session = self._factory()

        self._rules = MatchingRuleRepo(self._session)
        self.app_state = ApplicationStateRepo(self._session)

        return self

################################################################################
    def __exit__(self, exc_type, exc_val, exc_tb):

        try:
            if exc_type is None:
                self._session.commit()
            else:
                self._session.rollback()
        finally:
            if self._session:
                self._session.close()

################################################################################
