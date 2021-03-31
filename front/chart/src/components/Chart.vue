<template>
    <div class="chart">
        <section class="overview">
            <img class="bitcoin-image" src="../assets/bitcoin.png"/>
            <h3>Total amount spent: {{ totalAmountSpent.toFixed(2) }}</h3>
            <h3>Average: {{ averagePrice.toFixed(2) }}</h3>
            <h3> Estimated balance: {{ balance.toFixed(2) }}</h3>
        </section>
        <Card>
            <section class="tradingview-chart">
                <div id="chart"></div>
            </section>
        </Card>
    </div>
</template>

<script>
  import {createChart, LineStyle} from 'lightweight-charts';
  import prices from '../../data/price_history.json'
  import portfolio from '../../data/orders.json'
  import Card from "./Card";

  export default {
    name: 'Chart',
    components: {Card},
    mounted() {
      this.displayChart();
    },
    computed: {
      points() {
        return prices["prices_history"].map((price, index) => {
          return {time: prices["timestamps"][index], value: price};
        });
      },
      totalAmountSpent() {
        return portfolio["amounts_spent"].reduce((totalAmount, amount) => {
          return totalAmount + amount
        }, 0);
      },
      balance() {
        const amounts_spent = portfolio["amounts_spent"];
        const portfolio_prices = portfolio["prices"];

        return portfolio_prices.reduce((computedBalance, price, index) => {
          return computedBalance + (amounts_spent[index] / portfolio_prices[index])
        }, 0);
      },
      averagePrice() {
        return this.totalAmountSpent / this.balance;
      },
    },
    methods: {
      setData(lineSeries) {
        lineSeries.setData(this.points);
      },
      setMarkers(lineSeries) {
        const data = portfolio["timestamps"].map((timestamp, index) => {
          return {
            time: timestamp,
            position: 'belowBar',
            size: 1,
            color: 'red',
            shape: 'arrowUp',
            text: `${portfolio["amounts_spent"][index]}`,
          }
        });
        lineSeries.setMarkers(data);
      },
      setupChartOptions: function (chart) {
        chart.timeScale().fitContent();
        chart.applyOptions({
          handleScroll: false,
          handleScale: false,
        });
      }, displayChart() {
        const chart = createChart('chart', {width: 1000, height: 800});
        const lineSeries = chart.addLineSeries();
        this.setData(lineSeries);
        this.setMarkers(lineSeries);

        this.setupChartOptions(chart);

        lineSeries.createPriceLine({
          price: this.averagePrice,
          color: 'green',
          lineWidth: 4,
          lineStyle: LineStyle.Dotted,
          axisLabelVisible: true,
          title: 'Average price',
        });
      }
    }
  }
</script>

<style scoped>
    .chart {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .tradingview-chart {
        display: flex;
        justify-content: center;
        flex-direction: column;
    }

    .overview {
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        background-color: #222831;
        color: white;
        margin-bottom: 10px;
        padding: 10px;
    }

    .bitcoin-image {
        width: 60px;
    }
</style>
