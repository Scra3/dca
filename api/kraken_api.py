import requests
import time


class KrakenApi:
    @staticmethod
    def get_current_pair_price(pair: str) -> float:
        parameters = {
            "pair": pair
        }
        response = requests.get("https://api.kraken.com/0/public/Ticker", params=parameters)
        if response.ok:
            return float(response.json()["result"]["XXBTZEUR"]["a"][0])
        else:
            time.sleep(10)
            print("[retry] Kraken API is done")
            return KrakenApi.get_current_pair_price(pair)
