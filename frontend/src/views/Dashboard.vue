<template>
  <div>
    <!--Tables-->
    <div class="row">
      <div class="col-xl-12 mb-5 mb-xl-0">
        <low-variability-table></low-variability-table>
      </div>
    </div>
    <!--End tables-->
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {};
  },
  methods: {
    initBigChart(index) {
      let chartData = {
        datasets: [
          {
            label: "Performance",
            data: this.bigLineChart.allData[index],
          },
        ],
        labels: ["May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
      };
      this.bigLineChart.chartData = chartData;
      this.bigLineChart.activeIndex = index;
    },
  },
  mounted() {
    this.initBigChart(0);
  },
};
</script>
<style></style>
