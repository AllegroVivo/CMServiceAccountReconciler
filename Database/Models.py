from __future__ import annotations

import re
from datetime import date
from typing import Type, Optional

from sqlalchemy import Integer, String, UniqueConstraint, CheckConstraint, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr

from App.Classes import *
from Utilities import Utilities as U
################################################################################

__all__ = (
    "BaseModel",
    "SheetRoutingRuleModel",
    "ApplicationStateModel",
)

################################################################################
class BaseModel[T](DeclarativeBase):
    """Base class for all ORM models."""
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )

    _DC_TYPE: Type[T] = None

    # noinspection PyMethodParameters
    @declared_attr.directive
    def __tablename__(cls) -> str:
        # If a subclass explicitly sets __tablename__, honor it
        if "__tablename__" in cls.__dict__:
            return cls.__dict__["__tablename__"]

        base = re.sub(r"Model$", "", cls.__name__)  # EditionContributionModel -> EditionContribution
        return U.pluralize(U.camel_to_snake(base))  # -> edition_contribution -> edition_contributions

################################################################################
    def to_dataclass(self) -> T:
        """Convert the ORM model instance to a dataclass instance of the specified type."""

        assert self._DC_TYPE is not None

        filtered_attrs = {
            k: v
            for k, v in self.__dict__.items()
            if not k.startswith("_")
        }
        return self._DC_TYPE(**filtered_attrs)

################################################################################
class IDMixin:
    """Mixin class to add an auto-incrementing integer primary key 'id' column."""
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

################################################################################
class SheetRoutingRuleModel(BaseModel[SheetRoutingRuleRead], IDMixin):

    _DC_TYPE = SheetRoutingRuleRead

    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    sheet: Mapped[str] = mapped_column(String(100), nullable=False)
    min_amount: Mapped[Optional[float]] = mapped_column()
    max_amount: Mapped[Optional[float]] = mapped_column()
    priority: Mapped[int] = mapped_column(Integer, nullable=False, default=100)

    __table_args__ = (
        UniqueConstraint("sheet", "min_amount", "max_amount", name="uq_sheet_amount_range"),
        CheckConstraint("min_amount || max_amount", name="ck_min_le_max_amount"),
    )

################################################################################
class ApplicationStateModel(BaseModel[ApplicationState], IDMixin):

    _DC_TYPE = ApplicationState

    spreadsheet_id: Mapped[Optional[str]] = mapped_column(String(100))
    last_run_date: Mapped[Optional[date]] = mapped_column()

################################################################################
