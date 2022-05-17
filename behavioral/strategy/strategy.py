from abc import ABC, abstractmethod
from io import BytesIO

import pandas as pd

import xport.v56


def download_file(file_path: str) -> bytes:
    """
    Downloads the file with the given path.
    """


class DataExtractingStrategyInterface(ABC):
    """
    The interface must be implemented by
    all concrete strategies that extract data.
    """

    @abstractmethod
    def extract(self, file_contents: bytes) -> pd.DataFrame:
        """
        Extracts data and returns it as a pandas DataFrame.
        """


class DatasetContentsStrategy(DataExtractingStrategyInterface):
    """
    Extracts dataset contents from given bytes.
    """

    def extract(self, file_contents: bytes) -> pd.DataFrame:
        # we expect .xpt files in the example
        return pd.read_sas(BytesIO(file_contents), format="xport", encoding="utf-8")


class DatasetMetadataStrategy(DataExtractingStrategyInterface):
    """
    Extracts dataset metadata from given bytes.
    """

    def extract(self, file_contents: bytes) -> pd.DataFrame:
        dataset_container = xport.v56.loads(file_contents)
        dataset_id = next(iter(dataset_container))
        dataset = dataset_container.get(dataset_id)
        metadata: dict = {
            "variable_labels": list(dataset.contents.Label.values),
            "variable_names": list(dataset.contents.Variable.values),
        }
        return pd.DataFrame.from_dict(metadata)


class DatasetExtractingService:
    """
    This class is an entrypoint for data extracting.
    Allows to set the strategy on the fly.
    """

    def __init__(self, strategy: DataExtractingStrategyInterface):
        self._strategy = strategy

    @property
    def strategy(self) -> DataExtractingStrategyInterface:
        return self._strategy

    @strategy.setter
    def strategy(self, new_strategy: DataExtractingStrategyInterface):
        self._strategy = new_strategy

    def extract_data(self, file_path: str) -> pd.DataFrame:
        file_contents: bytes = download_file(file_path)
        return self._strategy.extract(file_contents)


if __name__ == "__main__":
    # client code
    metadata_strategy = DatasetMetadataStrategy()

    extracting_service = DatasetExtractingService(metadata_strategy)
    extracting_service.extract_data("test/test.xpt")

    extracting_service.strategy = DatasetContentsStrategy()
    extracting_service.extract_data("test/test.xpt")
