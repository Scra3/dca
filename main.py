import dca_runner as runner
import dca as algo
import price_history as price_history
import portfolio as portfolio

if __name__ == '__main__':
    dca_runner = runner.DcaRunner(price_history=price_history.PriceHistory(),
                                  dca=algo.Dca(price_initialisation=20, step_price=1,
                                               max_total_amount_to_spend=2000))
    dca_runner.run()

    amounts_spent = portfolio.Portfolio().get_amounts_spent()
    balance = portfolio.Portfolio().get_balance()

    print(amounts_spent)
    print(balance)
