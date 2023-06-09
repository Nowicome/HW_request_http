import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": "OAuth {}".format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, file_path: str, filename: str):
        """Метод загружает файл по адресу file_path на яндекс диск"""
        href = self._get_upload_link(disk_file_path=file_path).get("href", "")
        response = requests.put(href, data=open(filename, "rb"))
        response.raise_for_status()
        return response.status_code
