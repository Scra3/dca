import dataclasses

import model


@dataclasses.dataclass()
class BrokerStub(model.Broker):
    prices = []
    get_current_pair_price_count_call = 0
    send_buy_order_count_call = 0

    def get_current_pair_price(self, pair: str) -> float:
        self.get_current_pair_price_count_call += 1
        return self.prices[self.get_current_pair_price_count_call - 1]

    def send_buy_order(self, traded_pair: str, amount_to_spend: float, price: float):
        self.send_buy_order_count_call += 1
