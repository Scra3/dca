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
      decoratedData() {
        return prices["prices_history"].map((price, index) => {
          const date = this.addDays(Date.now(), index).toISOString().split('T')[0];
          return {time: date, value: price};
        });
      }
    },
    methods: {
      addDays(date, days) {
        const result = new Date(date);
        result.setDate(result.getDate() + days);
        return result;
      },
      setData(lineSeries) {
        lineSeries.setData(this.decoratedData);
      },
      setMarkers(lineSeries) {
        const data = this.decoratedData.map(price => {
          const isFound = portfolio["prices"].find(portfolioPrice => portfolioPrice === price["value"]);
          return isFound === undefined ? null : {
            time: price["time"],
            position: 'belowBar',
            size: 1,
            color: 'red',
            shape: 'arrowUp',
          }
        });
        lineSeries.setMarkers(data.filter(Boolean));
      },
      displayChart() {
        const chart = createChart('chart', {width: 1000, height: 500});
        const lineSeries = chart.addLineSeries();
        this.setData(lineSeries);
        this.setMarkers(lineSeries);
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
