from abc import ABC, abstractmethod
from io import BytesIO

import pandas as pd


class ReaderInterface(ABC):
    """
    An interface that must be implemented
    by a dataset reader.
    """

    @abstractmethod
    def read(self, data: bytes) -> pd.DataFrame:
        """
        Reads the data from bytes and returns it as a pandas DataFrame.
        The method is an entrypoint.
        """


class BaseReader(ReaderInterface, ABC):
    """
    Base reader that defines the common algorithm.
    """

    def __init__(self):
        self._df_to_return: pd.DataFrame = pd.DataFrame()

    def read(self, data: bytes) -> pd.DataFrame:
        self._df_to_return: pd.DataFrame = self._read_data_from_bytes(data)
        self._round_floats()
        self._rename_all_columns_to_uppercase()
        return self._df_to_return

    @abstractmethod
    def _read_data_from_bytes(self, data: bytes) -> pd.DataFrame:
        """
        Reads bytes and returns a DataFrame.
        The method is abstract because all concrete readers
        extract data their own way.
        """

    def _round_floats(self):
        self._df_to_return = self._df_to_return.applymap(
            lambda x: round(x, 5) if isinstance(x, float) else x
        )

    def _rename_all_columns_to_uppercase(self):
        self._df_to_return.columns = [
            column.upper() for column in self._df_to_return.columns
        ]


class XPTReader(BaseReader):
    """
    Reads data from xpt files.
    """

    def _read_data_from_bytes(self, data: bytes) -> pd.DataFrame:
        return pd.read_sas(BytesIO(data), format="xport", encoding="utf-8")

    def _round_floats(self):
        # we need 15 digits in xpt files
        self._df_to_return = self._df_to_return.applymap(
            lambda x: round(x, 15) if isinstance(x, float) else x
        )


class ExcelReader(BaseReader):
    """
    Reads data from excel files.
    """

    def _read_data_from_bytes(self, data: bytes) -> pd.DataFrame:
        return pd.read_excel(BytesIO(data))


class CSVReader(BaseReader):
    """
    Reads data from csv files.
    """

    def _read_data_from_bytes(self, data: bytes) -> pd.DataFrame:
        return pd.read_csv(BytesIO(data))
