import json
from abc import ABC, abstractmethod
from decimal import Decimal

import requests
from dicttoxml import dicttoxml
from requests import Response


class ExchangeClientInterface(ABC):
    """
    Interface that is obligatory to implement for all exchange clients.
    """

    @abstractmethod
    @property
    def _url(self) -> str:
        """
        Url of exchange server
        :return: str
        """

    @abstractmethod
    def _send(self, query_params: dict = None) -> dict:
        """
        Sends requests to the exchange
        :param query_params: query params
        :return: dict
        """

    @abstractmethod
    def coin_rate(self, coin_name: str, currency_name: str) -> Decimal:
        """
        Gets coin rate from cryptocurrency exchange.
        :param coin_name: name of coin (BTC, ETH, ...)
        :param currency_name: name of currency (USD, EUR, ...)
        :return: Decimal
        """


class BinanceClient(ExchangeClientInterface):
    """
    Communicates with Binance.
    """

    @property
    def _url(self) -> str:
        return 'https://api.binance.com/rate'

    def _send(self, query_params: dict = None) -> dict:
        response: Response = requests.get(self._url, params=query_params)
        return response.json()

    def coin_rate(self, coin_name: str, currency_name: str) -> Decimal:
        response_body: dict = self._send({'coin_name': coin_name, 'currency_name': currency_name})
        coin_rate: str = response_body['rate']
        return Decimal(coin_rate)


class CoinbaseClient(ExchangeClientInterface):
    """
    Communicates with Coinbase API.
    """

    @property
    def _url(self) -> str:
        return 'https://api.coinbase.com/get-rate'

    def _send(self, query_params: dict = None) -> dict:
        response: Response = requests.get(self._url, params=query_params)
        return response.json()

    def coin_rate(self, coin_name: str, currency_name: str) -> Decimal:
        response_body: dict = self._send({'coin_name': coin_name, 'currency_name': currency_name})
        coin_rate: str = response_body['coin_rate']
        return Decimal(coin_rate)


class KrakenClient(ExchangeClientInterface):
    """
    Communicates with Kraken API.
    """

    @property
    def _url(self) -> str:
        return 'https://api.kraken.com/get-rate'

    def _send(self, query_params: dict = None) -> dict:
        response: Response = requests.get(self._url, params=query_params)
        return response.json()

    def coin_rate(self, coin_name: str, currency_name: str) -> Decimal:
        response_body: dict = self._send({'coin_name': coin_name, 'currency_name': currency_name})
        coin_rate: str = response_body['rate']
        return Decimal(coin_rate)


class BaseCoinRate(ABC):
    """
    Base class.
    Used to represent coin rate in the format that the client wants.
    """

    def __init__(self, exchange_client: ExchangeClientInterface):
        self._exchange_client = exchange_client

    @abstractmethod
    def display_coin_rate(self, coin_name: str, currency_name: str) -> str:
        """
        Displays coin rate
        :param coin_name: name of coin (BTC, ETH, ...)
        :param currency_name: name of currency (USD, EUR, ...)
        :return: str
        """


class JSONCoinRate(BaseCoinRate):
    """
    Displays coin rate in JSON
    """
    def display_coin_rate(self, coin_name: str, currency_name: str) -> str:
        coin_rate: Decimal = self._exchange_client.coin_rate(coin_name, currency_name)
        data: dict = {'coin_rate': coin_rate}
        return json.dumps(data)


class XMLCoinRate(BaseCoinRate):
    """
    Displays coin rate in XML
    """
    def display_coin_rate(self, coin_name: str, currency_name: str) -> str:
        coin_rate: Decimal = self._exchange_client.coin_rate(coin_name, currency_name)
        data: dict = {'coin_rate': coin_rate}
        return dicttoxml(data)


if __name__ == '__main__':
    # client code

    client: KrakenClient = KrakenClient()
    representation_object: JSONCoinRate = JSONCoinRate(client)
    representation_object.display_coin_rate('BTC', 'USD')

    another_client: BinanceClient = BinanceClient()
    another_representation_object: XMLCoinRate = XMLCoinRate(client)
    another_representation_object.display_coin_rate('ETH', 'EUR')
