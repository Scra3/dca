<template>
    <div class="chart">
        <section class="overview">
            <img class="bitcoin-image" src="../assets/bitcoin.png" />
            <h3>Total amount spent: {{ totalAmountSpent.toFixed(2) }}</h3>
            <h3>Average: {{ averagePrice.toFixed(2) }}</h3>
            <h3> Estimated balance: {{ balance.toFixed(2) }}</h3>
        </section>
        <section class="content">
            <div id="chart"></div>
        </section>
    </div>
</template>

<script>
  import {createChart, LineStyle} from 'lightweight-charts';
  import prices from '../../data/price_history.json'
  import portfolio from '../../data/orders.json'

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
    .bitcoin-image {
        width: 60px;
    }

    .chart {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .content {
        display: flex;
        justify-content: center;
        flex-direction: column;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23);
        padding: 10px;
    }

    .overview {
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23);
        padding: 10px;
        background-color: #222831;
        color: white;
    }
</style>
