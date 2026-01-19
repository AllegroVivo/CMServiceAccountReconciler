from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict, List

if TYPE_CHECKING:
    from ..Spreadsheets import Spreadsheet
    from .Requests import SpreadsheetBatchUpdateRequest
    from .Responses import SpreadsheetBatchUpdateResponse
################################################################################
class BatchUpdateRequest(TypedDict):
    """Applies one or more updates to a spreadsheet.

    Members:
        - **requests** (List[Request]): A list of updates to apply to the spreadsheet
        - **includeSpreadsheetInResponse** (bool): Determines if the update response should include the spreadsheet resource.
        - **responseRanges** (List[str]): Limits the ranges included in the response spreadsheet. Meaningful only if ``includeSpreadsheetInResponse`` is 'true'.
        - **responseIncludeGridData** (bool): True if grid data should be returned. Meaningful only if ``includeSpreadsheetInResponse`` is 'true'. This parameter is ignored if a field mask was set in the request.
    """
    requests: List[SpreadsheetBatchUpdateRequest]
    includeSpreadsheetInResponse: bool
    responseRanges: List[str]
    responseIncludeGridData: bool

################################################################################
class BatchUpdateResponse(TypedDict):
    """The response to a batch update.

    Members:
        - **spreadsheetId** (str): The spreadsheet the updates were applied to.
        - **replies** (List[Response]): The reply of each request, in the same order as the requests.
        - **updatedSpreadsheet** (Spreadsheet): The spreadsheet resource after updates were applied. This is only set if ``includeSpreadsheetInResponse`` was 'true' in the request.
    """
    spreadsheetId: str
    replies: List[SpreadsheetBatchUpdateResponse]
    updatedSpreadsheet: Spreadsheet

################################################################################
