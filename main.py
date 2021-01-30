#!/usr/bin/env python3

import dca_runner as runner
import config
import model


def job():
    with open(config.DCA_CONFIGURATION_FILE) as json_file:
        dca_configuration: model.DcaConfiguration = model.DcaConfiguration.serialise(json_file.read())
    dca_runner = runner.DcaRunner(broker=model.Broker(),
                                  dca_configuration=dca_configuration)
    dca_runner.run()
    print(f"balance: {model.Portfolio().get_balance()}")
    print(f"amounts spent: {model.Portfolio().get_amounts_spent()}")
    print(f"total: {model.Portfolio().get_total_spent()}")
    print(f"average: {model.Portfolio().get_average_price()}")
    print(f"prices: {model.price_history.PriceHistory().get_prices()}")

    print(f"----------------MAIN INFO----------------------")
    print(f"Unrealized gain: {model.Portfolio().get_unrealized_gains()}")
    print(f"Unrealized percentage gain: {model.Portfolio().get_unrealized_gains_in_percentage()}%")
    print(f"Broker balance: {model.Broker().get_balance(dca_configuration.traded_pair)}")
    print(f"-----------------------------------------------")


if __name__ == '__main__':
    job()
