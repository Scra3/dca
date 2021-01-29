import dca_runner as runner
import dca as dca
import price_history as price_history
import portfolio as portfolio
import config

if __name__ == '__main__':
    with open(config.DCA_CONFIGURATION_FILE) as json_file:
        config = dca.DcaConfiguration.serialise(json_file.read())

    dca_runner = runner.DcaRunner(price_history=price_history.PriceHistory(),
                                  dca=dca.Dca(config=config))
    dca_runner.run()

    print(f"balance: {portfolio.Portfolio().get_balance()}")
    print(f"amounts spent: {portfolio.Portfolio().get_amounts_spent()}")
    print(f"total: {portfolio.Portfolio().get_total_spent()}")
    print(f"prices: {price_history.PriceHistory().get_prices()}")
    print(f"average: {portfolio.Portfolio().get_average_price()}")
