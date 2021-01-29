import requests


class PriceHistoryApi:
    @staticmethod
    def get_current_bitcoin_price() -> float:
        parameters = {
            "pair": "XBTEUR"
        }
        response = requests.get("https://api.kraken.com/0/public/Ticker", params=parameters)
        return float(response.json()["result"]["XXBTZEUR"]["a"][0])
