import os

import requests
from requests import Response


class DBClient:
    """
    A singleton DB client.
    """

    _instance = None

    def __init__(self):
        self._db_endpoint: str = os.getenv("DB_ENDPOINT")
        self._db_username: str = os.getenv("DB_USERNAME")
        self._db_password: str = os.getenv("DB_PASSWORD")

    @classmethod
    def get_instance(cls) -> "DBClient":
        instance = cls._instance
        if instance is None:
            instance = cls()
            cls._instance = instance
        return instance

    def execute_query(self, query: str) -> dict:
        """
        Executes a query and returns a response
        """
        return self._send({"query": query})

    def _send(self, request_body: dict) -> dict:
        """
        Internal method that sends the request to the DB server.
        """
        response: Response = requests.post(
            url=self._db_endpoint,
            json=request_body,
            auth=(self._db_username, self._db_password),
        )
        response_body: dict = response.json()
        print(
            f"Response status: {response.status_code}, Response body: {response_body}"
        )
        return response_body


if __name__ == "__main__":
    db_client = DBClient.get_instance()
    another_db_client = DBClient.get_instance()
    assert id(db_client) == id(another_db_client)
