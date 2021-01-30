import requests
import time
import enum
import krakenex


class PairMapping(enum.Enum):
    XBTEUR = "XXBTZEUR"
    ETHEUR = "XETHZEUR"
    XBTUSDC = "XBTUSDC"


class AssetMapping(enum.Enum):
    XBTEUR = "XXBT"
    ETHEUR = "XETH"
    XBTUSDC = "XXBT"


WAITING_BEFORE_RETRY_SECOND = 10
KRAKEN_KEY_FILE = "kraken.key"


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

    @staticmethod
    def _compute_volume_to_buy(amount_to_spent: float, price: float) -> float:
        return amount_to_spent / price

    def send_buy_order(self, traded_pair: str, amount_to_spent: float, price: float):
        volume = self._compute_volume_to_buy(amount_to_spent, price)
        self._kraken.load_key(KRAKEN_KEY_FILE)
        try:
            response = self._kraken.query_private("AddOrder", {'pair': traded_pair,
                                                               'type': 'buy',
                                                               'ordertype': 'limit',
                                                               'price': price,
                                                               'volume': volume})
            print(response)
        except requests.HTTPError:
            print(
                f"[FAILED] Send buy order failed, "
                f"trade_pair={traded_pair}, price={traded_pair}, amount_to_spent={traded_pair}")

    def get_balance(self, traded_pair: str) -> float:
        self._kraken.load_key(KRAKEN_KEY_FILE)
        try:
            return self._kraken.query_private("Balance")["result"][AssetMapping[traded_pair].value]
        except requests.HTTPError:
            print(f"[FAILED] get balance failed, trade_pair={traded_pair}")
