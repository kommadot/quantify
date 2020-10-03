<template>
  <v-container fill-height>
    <v-row style="width: 100%; height: 100%">
      <div
        id="home"
        class="home"
        style="vertical-align-center; width: 100%; height: 100%; margin: 0px;"
      >
        <div id="tooltip" class="floating-tooltip-2"></div>
      </div>
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
      stockName: "",
    };
  },
  mounted() {
    var home = document.getElementById("home");
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
    this.lineSeries = this.chart.addCandlestickSeries({
      upColor: "#FE2A30",
      downColor: "#226FD8",
      wickUpColor: "#FE2A30",
      wickDownColor: "#226FD8",
      borderVisible: false,
    });
    this.getStockPrice(this.$route.params.code);

    var toolTipWidth = 80;
    var toolTipHeight = 120;
    var toolTipMargin = 15;

    var toolTip = document.getElementById("tooltip");
    // toolTip.className = "floating-tooltip-2";
    home.appendChild(toolTip);
    var bd = this.businessDayToString;
    var series = this.lineSeries;
    var sname = this.getStockName;
    this.chart.subscribeCrosshairMove(function (param) {
      if (
        param.point === undefined ||
        !param.time ||
        param.point.x < 0 ||
        param.point.x > home.clientWidth ||
        param.point.y < 0 ||
        param.point.y > home.clientHeight
      ) {
        toolTip.style.display = "none";
      } else {
        const dateStr = bd(param.time);
        toolTip.style.display = "block";

        var price = param.seriesPrices.get(series).close;
        toolTip.innerHTML =
          '<div style="color: #009688">' +
          sname() +
          '</div><div style="font-size: 12px; margin: 4px 0px; color: #21384d">' +
          "Close : " +
          Math.round(100 * price) / 100 +
          '</div><div style="font-size: 12px; color: #21384d">' +
          dateStr +
          "</div>";
        var coordinate = series.priceToCoordinate(price);
        var shiftedCoordinate = param.point.x - 50;
        if (coordinate === null) {
          return;
        }
        shiftedCoordinate = Math.max(
          0,
          Math.min(home.clientWidth - toolTipWidth, shiftedCoordinate)
        );
        var coordinateY =
          coordinate - toolTipHeight - toolTipMargin > 0
            ? coordinate - toolTipHeight - toolTipMargin
            : Math.max(
                0,
                Math.min(
                  home.clientHeight - toolTipHeight - toolTipMargin,
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
      http.get(`/stockprice/${code}`).then((res) => {
        this.temp_obj = JSON.parse(res.data.data);
        this.stockName = res.data.name;
      });
    },
    businessDayToString(businessDay) {
      return businessDay.year + "-" + businessDay.month + "-" + businessDay.day;
    },
    getStockName() {
      return this.stockName;
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

.floating-tooltip-2 {
  width: 105px;
  height: 90px;
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