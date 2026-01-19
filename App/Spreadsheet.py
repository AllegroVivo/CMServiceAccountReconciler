from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, List, Dict, Tuple, Set, Any, Optional, Literal

from ._WorksheetFactory import _WorksheetFactory
from Utilities import Utilities as U

if TYPE_CHECKING:
    from GClient.Client import GSheetsClient
    from App.Worksheets.WorksheetBase import _WorksheetBase
    from .Exceptions import ParsingError
    from .Reconciler import ServiceReconciler
################################################################################

__all__ = ("Spreadsheet",)


################################################################################
class Spreadsheet:
    __slots__ = (
        "_client",
        "_raw",
        "_sheets",
        "_id_counter",
        "_last_run_date",
    )

################################################################################
    def __init__(self, client: GSheetsClient, payload: Dict[str, Any], last_run_date: Optional[date]) -> None:

        self._client: GSheetsClient = client
        self._raw: Dict[str, Any] = payload
        self._last_run_date: Optional[date] = last_run_date

        self._id_counter: int = 0

        self._sheets: List[_WorksheetBase] = [
            _WorksheetFactory.create(
                client=self._client,
                parent=self,
                payload=sheet
            )
            for sheet in self._raw.get("sheets", [])
            if sheet["properties"]["title"] in self.relevant_sheets()
        ]
        print(f"Loaded {len(self._sheets)} relevant sheets from spreadsheet.")

################################################################################
    def __getitem__(self, sheet: str) -> _WorksheetBase:

        for ws in self._sheets:
            if ws.title == sheet:
                return ws

            if self._last_run_date is not None:
                if ws.title == f"{sheet} - {self._last_run_date.strftime('%m-%d-%Y')}":
                    return ws

        raise KeyError(f"Unknown sheet: {sheet} or {sheet} - {self._last_run_date.strftime('%m-%d-%Y') if self._last_run_date else ''}")

################################################################################
    @property
    def id(self) -> str:

        return self._raw["spreadsheetId"]

################################################################################
    @property
    def properties(self) -> Dict[str, Any]:

        return self._raw.get("properties", {})

################################################################################
    def relevant_sheets(self, *, add_suffix: bool = True) -> Set[str]:

        if add_suffix:
            suffix = f" - {self._last_run_date.strftime('%m-%d-%Y')}" if self._last_run_date else ""
        else:
            suffix = ""
        return {
            f"Annual{suffix}",
            f"Monthly{suffix}",
            f"Plumbing - Annual{suffix}",
            f"Generator{suffix}",
            f"Duct Cleaning{suffix}",
        }

################################################################################
    @property
    def theme_colors(self) -> Dict[str, Dict[str, float]]:

        return {
            x["colorType"]: x["color"]["rgbColor"]
            for x
            in self.properties.get("spreadsheetTheme", {}).get("themeColors", {})
        }

################################################################################
    def new_id(self) -> int:

        self._id_counter += 1
        return self._id_counter

################################################################################
    def final_batch_update(self, reconciler: ServiceReconciler, date_str: str) -> None:

        create_sheets_payload = {"requests": []}
        # Create new tabs first
        for sheet in self._sheets:
            create_sheets_payload["requests"].append(sheet.create_new_sheet_request(date_str))

        create_sheets_payload["requests"].append(self._add_summary_sheet_request(date_str))
        resp = self._client.batch_update_spreadsheet(self.id, create_sheets_payload)

        new_sheet_ids: Dict[str, int] = {
            x["addSheet"]["properties"]["title"]: x["addSheet"]["properties"]["sheetId"]
            for x
            in resp.get("replies", [])
            if "addSheet" in x
        }
        new_sheet_grid_props: Dict[str, Any] = {
            x["addSheet"]["properties"]["title"]: x["addSheet"]["properties"]["gridProperties"]
            for x
            in resp.get("replies", [])
            if "addSheet" in x
        }
        print(new_sheet_grid_props)

        print(f"Creating new sheets completed.")

        requests = []
        trim_requests = []
        for sheet in self._sheets:
            new_sheet_title = f"{sheet.base_title()} - {date_str}"
            # Title row
            requests.append(self.title_row_payload(new_sheet_ids[new_sheet_title], sheet.title))
            # Append cells
            requests.append(sheet.append_cells_payload(new_sheet_ids[new_sheet_title]))
            # Column sizing
            requests.extend(sheet.column_sizing_requests(new_sheet_ids[new_sheet_title]))
            # Horizontal justification
            requests.extend(sheet.justification_requests(new_sheet_ids[new_sheet_title]))
            # Trim excess rows and columns
            trim_requests.extend(
                sheet.trim_requests(
                    new_sheet_ids[new_sheet_title],
                    trim_rows=sheet.max_row < 1000,
                    row_count=new_sheet_grid_props[new_sheet_title]["rowCount"],
                    record_count=len(sheet._records),
                    column_count=new_sheet_grid_props[new_sheet_title]["columnCount"],
                )
            )

            print(f"Appending data to sheet '{new_sheet_title}'...")

        bulk_update_request = {
            "requests": requests,
            "includeSpreadsheetInResponse": False
        }
        self._client.batch_update_spreadsheet(self.id, bulk_update_request)

        # Execute trimming requests
        if trim_requests:
            print(f"Trimming excess rows and columns...")
            self._client.batch_update_spreadsheet(
                self.id,
                {"requests": trim_requests}
            )

        # Write final errors list to error sheet.
        error_payload = reconciler.format_all_errors(date_str)
        if len(reconciler._errors) > 0:
            error_sheet_payload = {
                "requests": [self.create_error_sheet_request(date_str)]
            }
            print(f"Creating sheet 'Parsing Errors'...")
            self._client.batch_update_spreadsheet(
                self.id,
                error_sheet_payload
            )
            print(f"Appending data to sheet 'Parsing Errors'...")
            self._client.values_append(
                self.id,
                cell_range=U.absolute_range(f"Parsing Errors - {date_str}", f"A1:D{len(reconciler._errors)}"),
                body=error_payload,
                params={"valueInputOption": "USER_ENTERED"}
            )

        # Add data to the summary sheet for totals
        summary_sheet_id = new_sheet_ids[f"Summary - {date_str}"]
        summary_requests = self._summary_sheet_requests(summary_sheet_id, date_str)
        print(f"Appending data to sheet 'Summary'...")
        self._client.batch_update_spreadsheet(
            self.id,
            {"requests": list(summary_requests)}
        )

################################################################################
    @staticmethod
    def create_error_sheet_request(date_str: str) -> Dict[str, Any]:

        return {
            "addSheet": {
                "properties": {"title": f"Parsing Errors - {date_str}"}
            }
        }

################################################################################
    @staticmethod
    def _add_summary_sheet_request(date_str: str) -> Dict[str, Any]:

        return {
            "addSheet": {
                "properties": {"title": f"Summary - {date_str}"}
            }
        }

################################################################################
    @staticmethod
    def _summary_sheet_requests(sheet_id: int, date_str: str) -> Tuple[Dict[str, Any], ...]:

        def _cell_str(text: str) -> Dict[str, Any]:
            return {"userEnteredValue": {"stringValue": text}}

        def _cell_formula(formula: str) -> Dict[str, Any]:
            return {"userEnteredValue": {"formulaValue": formula}}

        def _row(label: Optional[str] = None, formula: Optional[str] = None, force_str: bool = False) -> Dict[str, Any]:
            values = []
            if label is not None:
                values.append(_cell_str(label))
            if formula is not None and not force_str:
                values.append(_cell_formula(formula))
            if force_str:
                values.append(_cell_str(formula if formula is not None else ""))
            return {"values": values}

        def _sum(sheet: str, a1_range: str) -> str:
            return f"=SUM({U.absolute_range(sheet, a1_range)})"

        rows_spec: List[Tuple[Optional[str], Optional[str]]] = [
            (f"Annual - {date_str}", _sum(f"Annual - {date_str}", "C:C")),
            (f"Monthly - {date_str}", _sum(f"Monthly - {date_str}", "C:C")),
            (f"Plumbing - Annual - {date_str}", _sum(f"Plumbing - Annual - {date_str}", "C:C")),
            (f"Generator - {date_str}", _sum(f"Generator - {date_str}", "C:C")),
            (f"Duct Cleaning - {date_str}", _sum(f"Duct Cleaning - {date_str}", "C:C")),
            ("Opening Balances", _sum("Opening Balances", "B:B")),
            ("Total", _sum(f"Summary - {date_str}", "B1:B6")),
            ("", None),
            ("", None),
        ]

        append_cells_request = {
            "appendCells": {
                "sheetId": sheet_id,
                "fields": "userEnteredValue",
                "rows": [_row(label, formula) for (label, formula) in rows_spec],
            }
        }
        append_cells_request["appendCells"]["rows"].append(_row("Reconciled Thru", date_str, force_str=True))

        format_cells_request = {
            "repeatCell": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": 0,
                    "endRowIndex": len(rows_spec) - 4,
                    "startColumnIndex": 1,
                    "endColumnIndex": 1,
                },
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {
                            "type": "NUMBER",
                            "pattern": "$#,##0.00",
                        }
                    }
                },
                "fields": "userEnteredFormat.numberFormat",
            }
        }

        format_date_request = {
            "repeatCell": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": len(rows_spec) - 2,
                    "endRowIndex": len(rows_spec) - 2,
                    "startColumnIndex": 1,
                    "endColumnIndex": 1,
                },
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {
                            "type": "DATE",
                            "pattern": "MM/DD/YYYY",
                        }
                    }
                },
                "fields": "userEnteredFormat.numberFormat",
            }
        }

        return append_cells_request, format_cells_request, format_date_request

################################################################################
    @staticmethod
    def title_row_payload(sheet_id: int, parent_sheet_name: str) -> Dict[str, Any]:

        col_names = [
            "Name",
            "Membership Type",
            "Balance",
        ]
        if (parent_sheet_name.startswith("Annual") or
           parent_sheet_name.startswith("Generator") or
           parent_sheet_name.startswith("Plumbing")):
            col_names.extend([
                "Expiration Date",
                "",
                "CSR",
                "Last Contact",
                "Notes",
                "Date Booked",
                "Age/Install Date",
                "Equipment",
            ])
        if parent_sheet_name.startswith("Monthly"):
            col_names.extend([
                "",
                "CSR",
                "Last Contact",
                "Contact Method(s)",
                "Scheduled Date",
                "Recognize As",
                "Last Service",
            ])
        if parent_sheet_name.startswith("Duct Cleaning"):
            col_names.append("CSR Data")

        return {
            "appendCells": {
                "sheetId": sheet_id,
                "rows": [
                    {
                        "values": [
                            {
                                "userEnteredValue": {"stringValue": col_name},
                                "userEnteredFormat": {
                                    "textFormat": {"bold": True}
                                }
                            }
                            for col_name in col_names
                        ]
                    }
                ],
                "fields": "userEnteredValue,userEnteredFormat.textFormat.bold"
            }
        }

################################################################################
    @staticmethod
    def _effective_format_dict(
        horizontal_alignment: Literal["LEFT", "CENTER", "RIGHT"] = "LEFT",
        wrap_strategy: Literal["OVERFLOW_CELL", "LEGACY_WRAP", "CLIP", "WRAP"] = "CLIP",
        number_fmt: Optional[Dict[str, Any]] = None,
        r: float = 1.0,
        g: float = 1.0,
        b: float = 1.0
    ) -> Dict[str, Any]:

        ret = {
            "horizontalAlignment": horizontal_alignment,
            "wrapStrategy": wrap_strategy,
            "backgroundColorStyle": {
                "rgbColor": {
                    "red": r,
                    "green": g,
                    "blue": b,
                }
            }
        }

        if number_fmt is not None:
            ret["numberFormat"] = number_fmt["numberFormat"]

        return ret

################################################################################
    @staticmethod
    def _number_format_dict(
        format_type: Literal[
            "TEXT",
            "NUMBER",
            "PERCENT",
            "CURRENCY",
            "DATE",
            "TIME",
            "DATE_TIME",
            "SCIENTIFIC"
        ] = "NUMBER",
        pattern: str = "#,##0.00"
    ) -> Dict[str, Any]:

        return {
            "numberFormat": {
                "type": format_type,
                "pattern": pattern
            }
        }

################################################################################
