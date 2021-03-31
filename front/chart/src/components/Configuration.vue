<template>
    <div class="config">
        <h2>Configuration</h2>
        <p>Price initialisation: {{ configurationData["price_initialisation"] }}</p>
        <p>Traded pair: {{ configurationData["traded_pair"] }}</p>
        <p>Step price: {{ configurationData["step_price"] }}</p>
        <p>Force buy under price: {{ configurationData["force_buy_under_price"] }}</p>
        <p>Max amount to spend: {{ configurationData["max_amount_to_spend"] }}</p>
        <p>Max total amount to spend: {{ configurationData["max_total_amount_to_spend"] }}</p>
    </div>
</template>

<script>
  import configuration from '../../data/configuration.json'

  export default {
    name: 'Configuration',
    computed: {
      configurationData() {
        return configuration;
      }
    }
  }
</script>

<style scoped>
    h2 {
        display: flex;
        justify-content: center;
    }

    p {
        margin: 2px;
    }

    .config {
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23);
        padding: 10px;
        background-color: #F6F6F6;
    }
</style>
