import portfolio_mapper as mapper
import typing


class Portfolio(mapper.PortfolioMapper):
    @staticmethod
    def get_average_price(total_spent: float, balance: float) -> float:
        return total_spent / balance

    @staticmethod
    def get_balance(prices: typing.List[float], amounts_spent: typing.List[float]) -> float:
        balance = 0
        for index, _ in enumerate(prices):
            balance += amounts_spent[index] / prices[index]

        return balance

    @staticmethod
    def get_total_spent_from_list(amounts_spent: typing.List[float]) -> float:
        return sum(amounts_spent)
