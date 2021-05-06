# Weighted Dollar Cost Average (WDCA)

![alt dca_front](https://pbs.twimg.com/media/Exrc57oWgAY4lqk?format=jpg&name=large)

The idea of this this algorithm is to smooth the entrance fee. It will buy all the new lows by weighting them.

For example :

The first buy will cost **10$**. The second will cost **11$**. The goal to increment the amount to invest is to attrack the price down to the bottom.

It buy only the lower price, if the price increases, we will count each candle between the last low and the new low and we make the sum of it.

For example, if at each candle it increments to **1$** and it starts to **10$** :

* price : **9, 8, 13, 10, 9, `7`**
* invest : **10, 11, 0(12), 0(13), 0(14), `12+13+14+15`** => when the price is **7$**, it invests **54$** (12+13+14+15).


## Install

```bash
make install
```

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

Add a *kraken.key* file with the first line, and the second line the secret key.

### Run

*  Run iteration manually

    ```bash
    make run-production
    ```

*  Scheduling execution with cron task

    ```bash
    * * * * * cd /home/pi/Documents/dca/ && make run-production >> log.txt 2>&1
    * * * * * cd /home/pi/Documents/dca/ && make backup-db >> log.txt 2>&1
    * * * * * cd /home/pi/Documents/dca/ && make copy-data-to-front >> log.txt 2>&1
    ```

### Display front

Copy the backups files in *front > chart > data* and add json extension to the files.


```bash
make run-front
```

### Estimate configuration parameters

```bash
make projection
```

## faq 

* [ssh on raspberrypi](https://www.raspberrypi-france.fr/guide/connecter-ssh-raspbian/).

* backups are generated in **backup** directory.
