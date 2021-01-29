import requests
import time
import enum


class PairMapping(enum.Enum):
    XBTEUR = "XXBTZEUR"
    ETHEUR = "XETHZEUR"


class KrakenApi:
    @staticmethod
    def get_current_pair_price(pair: str) -> float:
        parameters = {
            "pair": pair
        }
        response = requests.get("https://api.kraken.com/0/public/Ticker", params=parameters)
        if response.ok:
            return float(response.json()["result"][PairMapping[pair].value]["a"][0])
        else:
            time.sleep(10)
            print("[retry] Kraken API is done")
            return KrakenApi.get_current_pair_price(pair)
