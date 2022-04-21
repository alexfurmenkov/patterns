from abc import ABC, abstractmethod
from typing import List


class FileStorageClientInterface(ABC):
    """
    This class represents an interface that all clients
    of file storage use.
    """

    @abstractmethod
    def list_files(self) -> List[dict]:
        """
        Returns a list of files from file storage.
        :return: List[dict]
        """
