import os
from abc import ABC, abstractmethod

import requests


class QueueClientInterface(ABC):
    """
    The interface must be implemented by all queue clients.
    """

    @abstractmethod
    def send_message(self, message_body: dict, queue_name: str):
        """
        Sends a message to the given queue.
        """


class AWSQueueClient(QueueClientInterface):
    """
    AWS queue client implementation
    """

    def __init__(self):
        self._queue_url: str = os.environ["AWS_QUEUE_URL"]
        self._queue_auth_token: str = os.environ["AWS_QUEUE_TOKEN"]

    def send_message(self, message_body: dict, queue_name: str):
        requests.post(url=f"{self._queue_url}/{queue_name}", json=message_body)


class AzureQueueClient(QueueClientInterface):
    """
    Azure queue client implementation
    """

    def __init__(self):
        self._queue_url: str = os.environ["AZURE_QUEUE_URL"]
        self._queue_key: str = os.environ["AZURE_QUEUE_KEY"]
        self._subscription_id: str = os.environ["AZURE_SUBSCRIPTION_ID"]

    def send_message(self, message_body: dict, queue_name: str):
        body: dict = {
            "message": message_body,
            "queue_name": queue_name,
        }
        requests.post(url=f"{self._queue_url}/{self._subscription_id}", json=body)
