<template>
    <div class="logs">
        <h2>Logs</h2>

        <ul>
            <li v-for="log in logs" :key="log.message" :class="log.type">
                <span class="date">{{ convertTimestampToDate(log.timestamp)}}</span> -
                {{log.message}}
            </li>
        </ul>

    </div>
</template>

<script>
  import logsData from '../../data/log_pickle_db_test.json'

  export default {
    name: 'Logs',
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
        })
      }
    }
  }
</script>

<style scoped>
    h2 {
        display: flex;
        justify-content: center;
    }

    .logs {
        width: 25em;
        word-wrap: break-word;
        padding: 10px;
        overflow-y: scroll;
        background-color: #F6F6F6;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23);
        height: 900px;
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
