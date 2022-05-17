from abc import ABC, abstractmethod
from collections import defaultdict


class SubscriberInterface(ABC):
    """
    This interface must be implemented by all subscribers
    of an exchange.
    """

    @abstractmethod
    def notify(self, ticker: str, price: float):
        """
        This method is called by a publisher when
        a price of the ticker changes.
        """


class LongTermInvestor(SubscriberInterface):
    """
    One of the exchange subscribers.
    """

    def notify(self, ticker: str, price: float):
        print(
            f"I am not afraid that ticker {ticker} price changed to {price}. I am a long term investor."
        )


class BeginnerInvestor(SubscriberInterface):
    """
    One of the exchange subscribers.
    """

    def notify(self, ticker: str, price: float):
        print(
            f"Panic. Price of {ticker} ticker changed to {price}. What should I do? Sell?"
        )


class Exchange:
    """
    This class imitates a currency exchange that
    notifies the users when the desired price change occurs.
    """

    def __init__(self):
        self._tickers: dict = {
            "AAPL": 100.12,
            "AMZN": 321.23,
        }
        self._ticker_subscribers: dict = defaultdict(list)

    def add_subscriber(self, ticker: str, subscriber: SubscriberInterface):
        """
        Adds a new ticker subscriber.
        """
        self._ticker_subscribers[ticker].append(subscriber)

    def update_ticker_price(self, ticker: str, price: float):
        """
        The method imitates the situation when the ticker price
        has changed, and we need to notify all interested subscribers.
        """
        if ticker not in self._tickers:
            raise ValueError(f"Invalid ticker name: {ticker}")

        self._tickers[ticker] = price
        self._notify_subscribers(ticker, price)

    def _notify_subscribers(self, ticker: str, price: float):
        """
        Internal method that notifies all interested subscribers.
        """
        for subscriber in self._ticker_subscribers[ticker]:
            subscriber.notify(ticker, price)


if __name__ == "__main__":
    # client code

    exchange = Exchange()
    long_term_investor = LongTermInvestor()
    beginner_investor = BeginnerInvestor()

    exchange.add_subscriber("AMZN", long_term_investor)
    exchange.add_subscriber("AMZN", beginner_investor)

    exchange.update_ticker_price("AMZN", 220.12)
