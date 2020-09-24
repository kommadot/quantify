<template>
  <v-container fill-height>
    <v-row style="width: 100%; height: 100%">
      <div
        id="home"
        class="home"
        style="vertical-align-center; width: 100%; height: 100%; margin: 0px;"
      ></div>
    </v-row>
  </v-container>
</template>

<script>
import http from "@/util/http-common";

export default {
  name: "Home",
  components: {},
  data() {
    return {
      chart: null,
      lineSeries: null,
      // lineSeries: [],
      //   code1: "155660",
      temp_obj: [], 
    };
  },
  mounted() {
    this.chart = LightweightCharts.createChart(
      document.getElementById("home"),
      {
        // width: 600,
        // height: 300,
        layout: {
          backgroundColor: "#000000",
          textColor: "rgba(255, 255, 255, 0.9)",
        },
        grid: {
          vertLines: {
            color: "rgba(197, 203, 206, 0.5)",
          },
          horzLines: {
            color: "rgba(197, 203, 206, 0.5)",
          },
        },
        crosshair: {
          mode: LightweightCharts.CrosshairMode.Normal,
        },
        rightPriceScale: {
          borderColor: "rgba(197, 203, 206, 0.8)",
        },
        timeScale: {
          borderColor: "rgba(197, 203, 206, 0.8)",
        },
      }
    );
    this.lineSeries = this.chart.addCandlestickSeries({		upColor: '#FE2A30',
		downColor: '#226FD8',
		wickUpColor: '#FE2A30',
		wickDownColor: '#226FD8',borderVisible: false,});
    this.getStockPrice(this.$route.params.code);
  },

  methods: {
    getStockPrice(code) {

      http.get(`/stockprice/${code}`).then((res) => {

        this.temp_obj = JSON.parse(res.data.data);
      });
    },
  },
  watch: {
    temp_obj(value) {
      this.lineSeries.setData(value);
    },
    $route(value) {

      this.getStockPrice(value.params.code);
    },
  },
};
</script>
<style scoped>
.tv-lightweight-charts {
  margin: 0px;
}
</style>