<template>
  <div>
    <h2>Usage Chart</h2>
    <canvas id="usageChart"></canvas>
  </div>
</template>

<script>
import { Chart } from 'chart.js'
export default {
  name: 'UsageChart',
  mounted() {
    const ctx = document.getElementById('usageChart').getContext('2d')
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
          label: 'Usage (kWh)',
          data: [120, 150, 170, 160, 180, 200],
          borderColor: 'rgba(75,192,192,1)',
          fill: false
        }]
      },
      options: { responsive: true }
    })
  }
}
</script>
