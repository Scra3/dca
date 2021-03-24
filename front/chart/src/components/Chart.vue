<template>
    <div class="chart">
        <div id="chart"></div>
    </div>
</template>

<script>
  import {createChart} from 'lightweight-charts';
  import prices from '../../data/price_history_pickle_db_test.json'
  import portfolio from '../../data/portfolio_pickle_db_test.json'

  export default {
    name: 'HelloWorld',
    mounted() {
      this.displayChart();
    },
    props: {
      msg: String
    },
    computed: {
      points() {
        return prices["prices_history"].map((price, index) => {
          return {time: prices["timestamps"][index], value: price};
        });
      }
    },
    methods: {
      setData(lineSeries) {
        lineSeries.setData(this.points);
      },
      setMarkers(lineSeries) {
        const data = portfolio["timestamps"].map((timestamp) => {
          return {
            time: timestamp,
            position: 'belowBar',
            size: 1,
            color: 'red',
            shape: 'arrowUp',
          }
        });
        lineSeries.setMarkers(data);
      },
      displayChart() {
        const chart = createChart('chart', {width: 1000, height: 500});
        const lineSeries = chart.addLineSeries();
        this.setData(lineSeries);
        this.setMarkers(lineSeries);
        chart.timeScale().fitContent();
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
