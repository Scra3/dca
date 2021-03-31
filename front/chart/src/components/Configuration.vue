<template>
    <div class="config">
        <h2>Configuration</h2>
        <section>
            <p>Price initialisation: {{ configurationData["price_initialisation"] }}</p>
            <p>Traded pair: {{ configurationData["traded_pair"] }}</p>
            <p>Step price: {{ configurationData["step_price"] }}</p>
            <p>Force buy under price: {{ configurationData["force_buy_under_price"] }}</p>
            <p>Max amount to spend: {{ configurationData["max_amount_to_spend"] }}</p>
            <p>Max total amount to spend: {{ configurationData["max_total_amount_to_spend"] }}</p>
        </section>
    </div>
</template>

<script>
  import {getConfigurationData} from "../../api";

  export default {
    name: 'Configuration',
    computed: {
      configurationData() {
        return getConfigurationData();
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
    }

    section {
        display: flex;
        justify-content: center;
        flex-direction: column;
    }
</style>
