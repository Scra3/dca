<template>
    <div class="app">
        <Logs/>
        <Chart/>
    </div>
</template>

<script>
  import Chart from './components/Chart.vue'
  import Logs from './components/Logs.vue'

  export default {
    name: 'App',
    components: {
      Chart, Logs
    }
  }
</script>

<style scoped>
    .app {
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
    }
</style>