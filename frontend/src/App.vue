<template>
  <div id="app">
    <h1>Gas Sales System Dashboard</h1>
    <UsageChart />
  </div>
</template>

<script>
import UsageChart from './components/UsageChart.vue'
export default {
  name: 'App',
  components: { UsageChart }
}
</script>
