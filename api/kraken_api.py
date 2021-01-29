import requests
import time
import enum


class PairMapping(enum.Enum):
    XBTEUR = "XXBTZEUR"
    ETHEUR = "XETHZEUR"


WAITING_BEFORE_RETRY_SECOND = 10


class KrakenApi:
    @staticmethod
    def get_current_pair_price(pair: str) -> float:
        parameters = {"pair": pair}
        response = requests.get("https://api.kraken.com/0/public/Ticker", params=parameters)

        if response.ok:
            return float(response.json()["result"][PairMapping[pair].value]["a"][0])
        else:
            time.sleep(WAITING_BEFORE_RETRY_SECOND)
            print("[retry] Kraken API is done")
            return KrakenApi.get_current_pair_price(pair)

    @staticmethod
    def send_buy_order(pair: str, amount_to_spent: float, price: float) -> float:
        pass
