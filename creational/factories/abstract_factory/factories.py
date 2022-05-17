import os
from abc import ABC, abstractmethod

from creational.factories.abstract_factory.queue_clients import (
    QueueClientInterface,
    AWSQueueClient,
    AzureQueueClient,
)
from creational.factories.abstract_factory.logging_clients import (
    LoggingClientInterface,
    AWSLogger,
    AzureLogger,
)


class FactoryInterface(ABC):
    """
    An interface that must be implemented by
    all concrete factories.
    """

    @classmethod
    @abstractmethod
    def get_queue_client(cls) -> QueueClientInterface:
        """
        Returns a queue client.
        """

    @classmethod
    @abstractmethod
    def get_logger(cls) -> LoggingClientInterface:
        """
        Returns a logger.
        """


class AWSFactory(FactoryInterface):
    """
    Factory for creating AWS resources.
    """

    @classmethod
    def get_queue_client(cls) -> QueueClientInterface:
        """
        Returns AWS queue client.
        """
        return AWSQueueClient()

    @classmethod
    def get_logger(cls) -> LoggingClientInterface:
        """
        Returns AWS logger.
        """
        return AWSLogger()


class AzureFactory(FactoryInterface):
    """
    Factory for creating Azure resources.
    """

    @classmethod
    def get_queue_client(cls) -> QueueClientInterface:
        """
        Returns Azure queue client.
        """
        return AzureQueueClient()

    @classmethod
    def get_logger(cls) -> LoggingClientInterface:
        """
        Returns Azure logger.
        """
        return AzureLogger()


if __name__ == "__main__":
    cloud_provider_type: str = os.environ["CLOUD_PROVIDER"]
    if cloud_provider_type == "AWS":
        factory = AWSFactory()
    elif cloud_provider_type == "Azure":
        factory = AzureFactory()
    else:
        raise ValueError(f"Unknown cloud provider {cloud_provider_type}")

    logger = factory.get_logger()
    queue_client = factory.get_queue_client()
