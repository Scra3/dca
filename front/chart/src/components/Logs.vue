<template>
    <div class="logs">
        <h2>Logs</h2>
        <label for="filter">Display only <span class="error">Error</span> and <span class="warning">Warning</span>errors</label>
        <input id="filter" type="checkbox" value="filtered" v-model="isFiltered"/>
        <section class="details">
            <ul>
                <li v-for="log in filteredLogs" :key="log.message" :class="log.type">
                    <span class="date">{{ convertTimestampToDate(log.timestamp)}}</span> -
                    {{log.message}}
                </li>
            </ul>

            <div v-if="filteredLogs.length === 0">
                No log to display
            </div>
        </section>
    </div>
</template>

<script>
  import logsData from '../../data/log.json'

  export default {
    name: 'Logs',
    data() {
      return {
        isFiltered: []
      }
    },
    methods: {
      convertTimestampToDate(timestamp) {
        const date = new Date(timestamp * 1000);
        return `${date.getDate()}/${date.getMonth()}/${date.getFullYear()}-${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`;
      }
    },
    computed: {
      logs() {
        return logsData.messages.map((message, index) => {
          return {message: message, timestamp: logsData.timestamps[index], type: logsData.types[index]}
        }).reverse()
      },
      filteredLogs() {
        return this.logs.filter(log => {
          return this.isFiltered.length > 0 ? (log.type === "error" || log.type === "warning") : true
        });
      }
    }
  }
</script>

<style scoped>
    .logs {
        word-wrap: break-word;
        background-color: #F6F6F6;
        padding: 10px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23);
        overflow-y: hidden;
        height: 100%;
    }

    h2 {
        display: flex;
        justify-content: center;
    }

    .details {
        overflow-y: scroll;
        height: 100%;
    }

    li {
        margin-bottom: 20px;
    }

    .date {
        font-size: 0.8em;
    }

    .error {
        color: red;
    }

    .warning {
        color: orange;
    }

    .info {
        color: black;
    }

    .success {
        color: green;
    }
</style>
