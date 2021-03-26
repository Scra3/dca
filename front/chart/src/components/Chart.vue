<template>
    <div class="chart">
        <ul>
            <li>Total amount spent: {{ totalAmountSpent }}</li>
            <li>Average: {{ averagePrice }}</li>
            <li>Estimated balance: {{ balance }}</li>
        </ul>

        <div id="chart"></div>
    </div>
</template>

<script>
  import {createChart, LineStyle} from 'lightweight-charts';
  import prices from '../../data/price_history_pickle_db_test.json'
  import portfolio from '../../data/portfolio_pickle_db_test.json'

  export default {
    name: 'Chart',
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
      displayChart() {
        const chart = createChart('chart', {width: 1000, height: 800});
        const lineSeries = chart.addLineSeries();
        this.setData(lineSeries);
        this.setMarkers(lineSeries);
        chart.timeScale().fitContent();

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
        justify-content: center;
    }
</style>
