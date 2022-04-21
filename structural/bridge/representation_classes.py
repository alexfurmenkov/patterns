import json
from abc import ABC, abstractmethod
from decimal import Decimal

from dicttoxml import dicttoxml

from structural.bridge.exchange_clients import ExchangeClientInterface


class CoinRepresentationInterface(ABC):
    """
    Interface that must be implemented by all Representation classes.
    """

    @abstractmethod
    def display_coin_rate(self, coin_name: str, currency_name: str) -> str:
        """
        Displays coin rate
        :param coin_name: name of coin (BTC, ETH, ...)
        :param currency_name: name of currency (USD, EUR, ...)
        :return: str
        """


class BaseCoinRepresentation(CoinRepresentationInterface, ABC):
    """
    Base class.
    Used to represent coin rate in the format that the client wants.
    """

    def __init__(self, exchange_client: ExchangeClientInterface):
        self._exchange_client = exchange_client


class JSONCoinRepresentation(BaseCoinRepresentation):
    """
    Displays coin rate in JSON
    """
    def display_coin_rate(self, coin_name: str, currency_name: str) -> str:
        coin_rate: Decimal = self._exchange_client.get_coin_rate(coin_name, currency_name)
        data: dict = {'coin_rate': coin_rate}
        return json.dumps(data)


class XMLCoinRepresentation(BaseCoinRepresentation):
    """
    Displays coin rate in XML
    """
    def display_coin_rate(self, coin_name: str, currency_name: str) -> str:
        coin_rate: Decimal = self._exchange_client.get_coin_rate(coin_name, currency_name)
        data: dict = {'coin_rate': coin_rate}
        return dicttoxml(data)
