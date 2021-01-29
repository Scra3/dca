#!/usr/bin/env python3

import dca_runner as runner
import config
import model
import schedule
import time


def job():
    with open(config.DCA_CONFIGURATION_FILE) as json_file:
        dca_configuration = model.DcaConfiguration.serialise(json_file.read())
    dca_runner = runner.DcaRunner(price_history=model.PriceHistory(),
                                  dca_configuration=dca_configuration)
    dca_runner.run()
    print(f"balance: {model.Portfolio().get_balance()}")
    print(f"amounts spent: {model.Portfolio().get_amounts_spent()}")
    print(f"total: {model.Portfolio().get_total_spent()}")
    print(f"prices: {model.PriceHistory().get_prices()}")
    print(f"average: {model.Portfolio().get_average_price()}")


if __name__ == '__main__':
    job()
    # schedule.every(1).minutes.do(job)
    # while True:
    #   schedule.run_pending()
    #  time.sleep(1)
