<template>
    <div class="app">
        <div class="system-info">
            <Configuration class="configuration"/>
            <Logs class="logs"/>
        </div>
        <Chart/>
    </div>
</template>

<script>
  import Chart from './components/Chart.vue'
  import Logs from './components/Logs.vue'
  import Configuration from "./components/Configuration";

  export default {
    name: 'App',
    components: {
      Configuration,
      Chart,
      Logs
    }
  }
</script>

<style scoped>
    .app {
        display: flex;
        justify-content: space-evenly;
        height: 100%;
    }

    .system-info {
        display: flex;
        justify-content: space-between;
        flex-direction: column;
        width: 35em;
    }

    .configuration {
        margin-bottom: 30px;
        height: 15em;
    }

    .logs {
        flex-grow: 1;
        max-height: 35em;
    }
</style>