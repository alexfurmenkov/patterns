from .representation_classes import (
    JSONCoinRepresentation,
    XMLCoinRepresentation,
)
from .exchange_clients import (
    BinanceClient,
    KrakenClient,
)

if __name__ == "__main__":
    # client code

    kraken_client: KrakenClient = KrakenClient()
    json_representation_object = JSONCoinRepresentation(kraken_client)
    json_representation_object.display_coin_rate("BTC", "USD")

    binance_client: BinanceClient = BinanceClient()
    xml_representation_object = XMLCoinRepresentation(binance_client)
    xml_representation_object.display_coin_rate("ETH", "EUR")
