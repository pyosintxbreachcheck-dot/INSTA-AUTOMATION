from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


class DriveManager:

    def __init__(self, service_file):
        self.creds = service_account.Credentials.from_service_account_file(
            service_file,
            scopes=SCOPES
        )

        self.service = build(
            "drive",
            "v3",
            credentials=self.creds
        )

    def get_videos(self, folder_id):

        results = self.service.files().list(
            q=f"'{folder_id}' in parents and mimeType contains 'video/'",
            fields="files(id,name)"
        ).execute()

        return results.get("files", [])
