import os
from abc import ABC, abstractmethod


class LoggingClientInterface(ABC):
    """
    Interface that must be implemented by all concrete loggers.
    """

    @abstractmethod
    def info(self, message: str):
        """
        Logs a message on info level.
        """

    @abstractmethod
    def debug(self, message: str):
        """
        Logs a message on debug level.
        """


class AWSLogger(LoggingClientInterface):
    """
    AWS logger implementation
    """

    def __init__(self):
        self._cloudwatch_id: str = os.environ["AWS_CLOUDWATCH_ID"]

    def info(self, message: str):
        print(f"[INFO: AWS LOGGER, CLOUDWATCH_ID: {self._cloudwatch_id}] {message}")

    def debug(self, message: str):
        print(f"[DEBUG: AWS LOGGER, CLOUDWATCH_ID: {self._cloudwatch_id}] {message}")


class AzureLogger(LoggingClientInterface):
    """
    Azure logger implementation
    """

    def __init__(self):
        self._app_metrics_id: str = os.environ["AZURE_APP_METRICS_ID"]

    def info(self, message: str):
        print(f"[INFO: AZURE LOGGER, CLOUDWATCH_ID: {self._app_metrics_id}] {message}")

    def debug(self, message: str):
        print(f"[DEBUG: AZURE LOGGER, CLOUDWATCH_ID: {self._app_metrics_id}] {message}")
