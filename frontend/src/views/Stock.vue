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
    var home = document.getElementById("home");
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

    var toolTipWidth = 80;
    var toolTipHeight = 80;
    var toolTipMargin = 15;

    var toolTip = document.getElementById("home");
    toolTip.className = "floating-tooltip-2";
    home.appendChild(toolTip);

    chart.subscribeCrosshairMove(function (param) {
      if (
        param.point === undefined ||
        !param.time ||
        param.point.x < 0 ||
        param.point.x > container.clientWidth ||
        param.point.y < 0 ||
        param.point.y > container.clientHeight
      ) {
        toolTip.style.display = "none";
      } else {
        const dateStr = businessDayToString(param.time);
        toolTip.style.display = "block";
        var price = param.seriesPrices.get(series);
        toolTip.innerHTML =
          '<div style="color: #009688">Apple Inc.</div><div style="font-size: 24px; margin: 4px 0px; color: #21384d">' +
          Math.round(100 * price) / 100 +
          '</div><div style="color: #21384d">' +
          dateStr +
          "</div>";
        var coordinate = series.priceToCoordinate(price);
        var shiftedCoordinate = param.point.x - 50;
        if (coordinate === null) {
          return;
        }
        shiftedCoordinate = Math.max(
          0,
          Math.min(container.clientWidth - toolTipWidth, shiftedCoordinate)
        );
        var coordinateY =
          coordinate - toolTipHeight - toolTipMargin > 0
            ? coordinate - toolTipHeight - toolTipMargin
            : Math.max(
                0,
                Math.min(
                  container.clientHeight - toolTipHeight - toolTipMargin,
                  coordinate + toolTipMargin
                )
              );
        toolTip.style.left = shiftedCoordinate + "px";
        toolTip.style.top = coordinateY + "px";
      }
    });
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
    businessDayToString(businessDay) {
      return businessDay.year + "-" + businessDay.month + "-" + businessDay.day;
    },
  },
  watch: {
    temp_obj(value) {
      this.lineSeries.setData(value);
    },
  },
};
</script>


<style scoped>
.floating-tooltip-2 {
  width: 96px;
  height: 80px;
  position: absolute;
  display: none;
  padding: 8px;
  box-sizing: border-box;
  font-size: 12px;
  color: #131722;
  background-color: rgba(255, 255, 255, 1);
  text-align: left;
  z-index: 1000;
  top: 12px;
  left: 12px;
  pointer-events: none;
  border: 1px solid rgba(0, 150, 136, 1);
  border-radius: 2px;
}
</style>