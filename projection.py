if __name__ == '__main__':
    price_initialisation: float = 10
    step_price: float = 7.0
    max_total_amount_to_spend: float = 14000

    remaining_amount = max_total_amount_to_spend
    iteration: int = 0
    while remaining_amount > 0:
        amount = price_initialisation + step_price * iteration
        remaining_amount -= amount
        print("week:", iteration, ", amount:", amount)
        print("remaining_amount:", remaining_amount)
        iteration = iteration + 1

    # first bear market 90 weeks
    # second bear market 53 weeks
    weeks_in_year = 52.1429
    print("weeks:", iteration)
    print("years:", iteration / weeks_in_year)
