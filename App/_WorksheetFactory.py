from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict

from App.Worksheets import (
    AnnualWorksheet,
    PlumbingWorksheet,
    GeneratorWorksheet,
    DuctCleaningWorksheet,
    MonthlyWorksheet
)

if TYPE_CHECKING:
    from GClient.Client import GSheetsClient
    from .Spreadsheet import Spreadsheet
    from App.Worksheets.WorksheetBase import _WorksheetBase
################################################################################

__all__ = ("_WorksheetFactory", )

################################################################################
class _WorksheetFactory:

    @staticmethod
    def create(client: GSheetsClient, parent: Spreadsheet, payload: Dict[str, Any]) -> _WorksheetBase:

        title = payload["properties"]["title"]
        assert title is not None
        cls = None

        if title.startswith("Annual"):
            cls = AnnualWorksheet
        elif title.startswith("Monthly"):
            cls = MonthlyWorksheet
        elif title.startswith("Plumbing"):
            cls = PlumbingWorksheet
        elif title.startswith("Generator"):
            cls = GeneratorWorksheet
        elif title.startswith("Duct Cleaning"):
            cls = DuctCleaningWorksheet

        if cls is None:
            raise ValueError(f"Unknown worksheet type: {title}")

        return cls(
            client=client,
            parent=parent,
            payload=payload
        )

################################################################################
