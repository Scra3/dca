import requests


class PriceHistoryApi:
    @staticmethod
    def get_current_bitcoin_price() -> float:
        parameters = {
            "ids": "bitcoin",
            "vs_currencies": "eur"
        }
        response = requests.get("https://api.coingecko.com/api/v3/simple/price", params=parameters)
        return float(response.json()["bitcoin"]["eur"])
