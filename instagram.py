import requests


class InstagramUploader:

    def __init__(self, account_id, token):

        self.account_id = account_id
        self.token = token

    def upload_reel(self, video_url, caption):

        endpoint = (
            f"https://graph.facebook.com/v23.0/"
            f"{self.account_id}/media"
        )

        payload = {
            "media_type": "REELS",
            "video_url": video_url,
            "caption": caption,
            "access_token": self.token
        }

        response = requests.post(
            endpoint,
            data=payload
        )

        creation_id = response.json()["id"]

        publish = requests.post(
            f"https://graph.facebook.com/v23.0/"
            f"{self.account_id}/media_publish",
            data={
                "creation_id": creation_id,
                "access_token": self.token
            }
        )

        return publish.json()
