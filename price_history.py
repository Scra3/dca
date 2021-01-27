import price_history_api as api
import price_history_mapper as mapper


class PriceHistory(api.PriceHistoryApi, mapper.PriceHistoryMapper):
    pass
