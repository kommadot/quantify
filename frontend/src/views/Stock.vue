<template>
  <div class="container">
    <v-btn @click="getStockPrice"></v-btn>
    <div id="home" class="home" style="vertical-align-center"></div>
  </div>
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
      code1: "155660",
      temp_obj: [],
    };
  },
  mounted() {
    this.chart = LightweightCharts.createChart(
      document.getElementById("home"),
      {
        width: 600,
        height: 300,
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
    this.lineSeries = this.chart.addCandlestickSeries();
    this.lineSeries.setData([temp_obj]);
  },
  methods: {
    getStockPrice(code) {
      code = this.code1;
      http.get(`/stockprice/${code}`).then((res) => {
        console.log(JSON.parse(res.data.data));
        this.temp_obj = JSON.parse(res.data.data);
        // alert(typeof JSON.parse(res.data.data));
        // this.lineSeries.push(JSON.parse(res.data.data))
      });
    },
  },
  watch: {
    temp_obj(value) {
      this.lineSeries.setData(value);
    },
  },
};
</script>