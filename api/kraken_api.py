import time

import krakenex
import requests

from model.enum import TradedPairMapping
from model.log import Log

WAITING_BEFORE_RETRY_SECOND = 10
KRAKEN_KEY_FILE = "kraken.key"


class KrakenApi:
    @staticmethod
    def get_current_pair_price(pair: TradedPairMapping) -> float:
        kraken = krakenex.API()
        try:
            response = kraken.query_public(f"Ticker?pair={pair.name}")
            Log.info(f"kraken fetch {pair.name} price").save()
            return float(response["result"][pair.value]["a"][0])

        except requests.HTTPError:
            time.sleep(WAITING_BEFORE_RETRY_SECOND)
            Log.error(f"kraken fetch {pair.name} fail").save()
            return KrakenApi.get_current_pair_price(pair)

    @staticmethod
    def _compute_volume_to_buy(amount_to_spend: float, price: float) -> float:
        return amount_to_spend / price

    @staticmethod
    def send_buy_order(
        traded_pair: TradedPairMapping, amount_to_spend: float, price: float
    ):
        kraken = krakenex.API()

        volume = KrakenApi._compute_volume_to_buy(amount_to_spend, price)
        try:
            kraken.load_key(KRAKEN_KEY_FILE)
            kraken.query_private(
                "AddOrder",
                {
                    "pair": traded_pair.value,
                    "type": "buy",
                    "ordertype": "market",
                    "price": price,
                    "volume": volume,
                },
            )
            Log.success("send order is a successfully").save()

        except FileNotFoundError:
            Log.warning("KRAKEN KEY is not defined, buy order is not send").save()
        except requests.HTTPError:
            message = f"[FAILED] Send buy order failed, "
            f"trade_pair={traded_pair.value}, price={traded_pair.value}, amount_to_spend={traded_pair.value}"
            Log.error(message).save()
