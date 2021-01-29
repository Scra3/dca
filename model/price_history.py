import price_history_api as api
import mapper


class PriceHistory(api.PriceHistoryApi, mapper.PriceHistoryMapper):
    pass
