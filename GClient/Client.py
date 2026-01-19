from __future__ import annotations

import json

from typing import (
    TYPE_CHECKING, MutableMapping, Any, Optional, Union, List, Mapping,
    IO, Tuple, Dict
)

import requests
from google.auth.transport.requests import AuthorizedSession
from google.oauth2.service_account import Credentials as SACredentials

from .Types import SpreadsheetBatchUpdateResponse, SpreadsheetBatchUpdateRequest, Spreadsheet
from Utilities import Utilities as U

if TYPE_CHECKING:
    from google.auth.credentials import Credentials
################################################################################

__all__ = ("GSheetsClient", "ParamsType")

BASE_URL_SPREADSHEETS = "https://sheets.googleapis.com/v4/spreadsheets"
SPREADSHEET_URL = f"{BASE_URL_SPREADSHEETS}/{{spreadsheetId}}"
SPREADSHEET_VALUES_URL = f"{SPREADSHEET_URL}/values/{{range}}"
SPREADSHEET_BATCH_UPDATE_URL = f"{SPREADSHEET_URL}:batchUpdate"
SPREADSHEET_COPY_TO_URL = f"{SPREADSHEET_URL}/sheets/{{sheetId}}:copyTo"
SPREADSHEET_VALUES_BATCH_URL = f"{SPREADSHEET_URL}/values:batchGet"
SPREADSHEET_VALUES_APPEND_URL = f"{SPREADSHEET_VALUES_URL}:append"

ParamsType = MutableMapping[str, Optional[Union[str, int, bool, float, List[str]]]]
FileType = Optional[
    Union[
        MutableMapping[str, IO[Any]],
        MutableMapping[str, Tuple[str, IO[Any]]],
        MutableMapping[str, Tuple[str, IO[Any], str]],
        MutableMapping[str, Tuple[str, IO[Any], str, MutableMapping[str, str]]],
    ]
]

################################################################################
class GSheetsClient:

    __slots__ = (
        "_auth",
        "_session",
        "_timeout",
        "_service",
    )

################################################################################
    def __init__(self, svc_account_file: str = "service_account.json") -> None:

        self._auth: Credentials = self._build_credentials(svc_account_file)
        self._session: AuthorizedSession = AuthorizedSession(self._auth)
        self._timeout: float = 30.0

################################################################################
    @staticmethod
    def _build_credentials(svc_account_file: str):

        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/drive.file"
        ]
        return SACredentials.from_service_account_file(svc_account_file, scopes=scopes)

################################################################################
    def login(self) -> None:
        from google.auth.transport.requests import Request

        self._auth.refresh(Request(self._session))
        self._session.headers.update({"Authorization": "Bearer %s" % self._auth.token})

################################################################################
    def request(
        self,
        method: str,
        url: str,
        params: Optional[ParamsType] = None,
        data: Optional[bytes] = None,
        json: Optional[Mapping[str, Any]] = None,
        files: Optional[FileType] = None,
        headers: Optional[MutableMapping[str, str]] = None,
    ) -> requests.Response:

        response = self._session.request(
            method=method,
            url=url,
            params=params,
            data=data,
            json=json,
            files=files,
            headers=headers,
            timeout=self._timeout,
        )

        if response.ok:
            return response
        # TODO: Handle this more gracefully
        print(response.json())
        raise Exception(response.text)

################################################################################
    def spreadsheet_get(
        self,
        spreadsheet_id: str,
        ranges: List[str] = None,
        include_grid_data: bool = False
    ) -> Dict[str, Any]:

        params: ParamsType = {
            "includeGridData": include_grid_data
        }
        if ranges:
            params["ranges"] = ranges

        resp = self.request(
            "GET",
            SPREADSHEET_URL.format(spreadsheetId=spreadsheet_id),
            params=params
        )
        return resp.json()

################################################################################
    def spreadsheet_create(self, payload: Dict[str, Any]) -> str:
        """Returns the newly created spreadsheet's ID."""

        resp = self.request(
            "POST",
            BASE_URL_SPREADSHEETS,
            json=payload
        )
        return resp.json()["spreadsheetUrl"]

################################################################################
    def batch_update_spreadsheet(
        self,
        spreadsheet_id: str,
        body: Dict[str, Any]
    ) -> Dict[str, Any]:

        resp = self.request(
            "POST",
            SPREADSHEET_BATCH_UPDATE_URL.format(spreadsheetId=spreadsheet_id),
            json=body
        )
        return resp.json()

################################################################################
    # TODO: Update return type once ValueBatchGetResponse is implemented
    def values_batch_get(
        self,
        spreadsheet_id: str,
        params: Optional[ParamsType] = None
    ) -> Any:

        resp = self.request(
            "GET",
            SPREADSHEET_VALUES_BATCH_URL.format(spreadsheetId=spreadsheet_id),
            params=params
        )
        return resp.json()

################################################################################
    # TODO: Update body and return type once request and response types are implemented
    def values_batch_update(
        self,
        spreadsheet_id: str,
        body: Any
    ) -> Any:

        resp = self.request(
            "POST",
            SPREADSHEET_VALUES_BATCH_URL.format(spreadsheetId=spreadsheet_id),
            json=body
        )
        return resp.json()

################################################################################
    # TODO: Update body and return type once request and response types are implemented
    def values_get(self, spreadsheet_id: str, cell_range: str, params: Optional[ParamsType] = None) -> Any:

        resp = self.request(
            "GET",
            SPREADSHEET_VALUES_URL.format(
                spreadsheetId=spreadsheet_id,
                range=U.safe_quote(cell_range)
            ),
            params=params
        )
        return resp.json()

################################################################################
    def values_append(
        self,
        spreadsheet_id: str,
        cell_range: str,
        body: Dict[str, Any],
        params: Optional[ParamsType] = None
    ) -> Any:

        resp = self.request(
            "POST",
            SPREADSHEET_VALUES_APPEND_URL.format(
                spreadsheetId=spreadsheet_id,
                range=U.safe_quote(cell_range)
            ),
            params=params,
            json=body
        )
        return resp.json()

################################################################################
