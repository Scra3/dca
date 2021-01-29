import requests
import time
import enum
import krakenex


class PairMapping(enum.Enum):
    XBTEUR = "XXBTZEUR"
    ETHEUR = "XETHZEUR"


WAITING_BEFORE_RETRY_SECOND = 10


class KrakenApi:
    def __init__(self):
        self._kraken = krakenex.API()

    def get_current_pair_price(self, pair: str) -> float:
        try:
            response = self._kraken.query_public(f"Ticker?pair={pair}")
            return float(response["result"][PairMapping[pair].value]["a"][0])
        except requests.HTTPError:
            time.sleep(WAITING_BEFORE_RETRY_SECOND)
            print("[retry] Kraken API is done")
            return self.get_current_pair_price(pair)

    def send_buy_order(self, pair: str, amount_to_spent: float, price: float) -> float:
        pass
