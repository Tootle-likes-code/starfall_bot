""" Implementations of definition collectors specifically for extracting google sheets data. """

import os

from google.oauth2.credentials import Credentials
from google_auth_httplib2 import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from starfall_bot.definition_collector import DefinitionCollector


class DefinitionSheetsCollector(DefinitionCollector):
    """  Implements DefinitionCollector for google sheets.   """
    def __init__(self, sheet_id, scopes=None):
        self._sheet_id = sheet_id
        if scopes:
            self._scopes = scopes
        else:
            self._scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    def get_definition(self, word) -> str:

        credentials = self._get_credentials()
        results = self._request_sheets_data(credentials)

        if word in results:
            return results[word]

        return None

    def _get_credentials(self):
        credentials = None

        if os.path.exists("token.json"):
            credentials = Credentials.from_authorized_user_file("token.json", self._scopes)

        if not credentials or not credentials.valid:
            credentials = self._update_credentials(credentials)

        return credentials

    def _update_credentials(self, credentials):
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", self._scopes)
            credentials = flow.run_local_server(port=0)

        with open("token.json", "w", encoding="utf-8") as token_file:
            token_file.write(credentials.to_json())

        return credentials

    def _request_sheets_data(self, credentials) -> dict[str, str]:
        try:
            service = build("sheets", "v4", credentials=credentials)

            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=self._sheet_id, range="Sheet1!C9:D").execute()
            values = result.get('values', [])

            if not values:
                raise ValueError("No data returned.")

            results = {}
            for row in values:
                results[row[0]] = row[1]

            return results

        except HttpError as err:
            print(err)
            raise err
