<template>
    <div class="card">
        <slot></slot>
    </div>
</template>

<script>

  export default {
    name: 'Card'
  }
</script>

<style scoped>
    .card {
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23);
        padding: 10px;
        background-color: #F6F6F6;
    }
</style>
