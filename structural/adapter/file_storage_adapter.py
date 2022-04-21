from typing import List

import requests
from requests import Response

from .file_storage_client_interface import FileStorageClientInterface


class FileStorage:
    """
    This class is responsible for "communicating" with file storage.
    It has an interface which cannot be used by clients.
    """

    def __init__(self):
        self.__storage_url = 'https://test-storage.com'

    def all_files(self) -> List[dict]:
        response: Response = requests.get(self.__storage_url)
        return response.json()


class FileStorageAdapter(FileStorageClientInterface):
    """
    This class is an adapter between FileStorage and FileStorageClientInterface interfaces.
    It allows using FileStorage with an interface that is convenient for a client.
    """

    def __init__(self, storage_obj: FileStorage):
        self._storage_obj = storage_obj

    def list_files(self) -> List[dict]:
        return self._storage_obj.all_files()


if __name__ == '__main__':
    # client code

    file_storage_obj: FileStorage = FileStorage()
    file_storage_adapter: FileStorageAdapter = FileStorageAdapter(file_storage_obj)
    file_storage_adapter.list_files()
