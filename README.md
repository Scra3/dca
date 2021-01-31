# dca

## Run all tests

```bash
make tests
```

## Run in development mode

```bash
make run
```

## Deploy to production

### Configure application

```bash
make generate-configuration
```

### setup *dca_configuration_production.json* file:

* **price_initialisation**: the price/amount of the first investment
* **step_price**: the price increase each iteration. For example, for the third iteration, **price_initialisation + 3 -
  1 * step_price** will be invested.
* **traded_pair** : the pair to trade (ETHEUR, BTCEUR, XBTUSDC)
* **force_buy_under_price** (optional): under this price each iteration is bought
* **max_amount_to_spend** (optional): the maximum amount to spend each iteration
* **max_total_amount_to_spend** (optional): the total maximum to spend

json dca configuration:

```json
{
  "price_initialisation": 10,
  "step_price": 1,
  "traded_pair": "XBTEUR",
  "force_buy_under_price": 20,
  "max_amount_to_spend": 10000,
  "max_total_amount_to_spend": 1000
}
```

### Add secret key for the kraken broker

Add a *kraken.key* file with the first line et api key and the second line the secret key.

### Run

```bash
make run-production
```

or add cron task

```bash
* * * * * cd /home/pi/Documents/dca/ && make run >> log.txt 2>&1
* * * * * cd /home/pi/Documents/dca/ && make backup-db >> log.txt 2>&1
```
