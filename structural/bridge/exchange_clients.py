from abc import ABC, abstractmethod
from decimal import Decimal

import requests
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
    def get_coin_rate(self, coin_name: str, currency_name: str) -> Decimal:
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

    def get_coin_rate(self, coin_name: str, currency_name: str) -> Decimal:
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

    def get_coin_rate(self, coin_name: str, currency_name: str) -> Decimal:
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

    def get_coin_rate(self, coin_name: str, currency_name: str) -> Decimal:
        response_body: dict = self._send({'coin_name': coin_name, 'currency_name': currency_name})
        coin_rate: str = response_body['rate']
        return Decimal(coin_rate)
