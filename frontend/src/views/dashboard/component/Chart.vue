<template>
  <v-container fill-height>
    <v-row justify="d-flex align-center space-between">
      <v-col style="padding: 0">
        <v-row>
          <div class="headline mr-3 white--text">
            {{ name }}
          </div>
          <div class="d-flex align-end mr-3 pb-0 white--text">
            현재가 : {{ cur_price }}원
          </div>
          <div class="d-flex align-end pb-0 white--text">
            시가총액 : {{ market_price }}억원
          </div>
        </v-row>
      </v-col>
      <v-col style="padding: 0" cols="4">
        <v-row>
          <v-text-field
            color="white"
            label="수량"
            v-model="buy_count"
            dark
          ></v-text-field>

          <v-btn depressed color="#283593" @click="postSimulationList">
            모의주식구매
          </v-btn>
        </v-row>
      </v-col>
    </v-row>
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
import axios from "axios";
import { mapState, mapActions, Store } from "vuex";
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

      name: "",
      market_price: 0,
      cur_price: 0,
      buy_count: null,
      temp_obj: [],

      stockName: "",
    };
  },




    };
  },
  mounted() {
      this.getStocks();
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
    getStocks() {},
    getStockPrice(code) {
      http.get(`/stockprice/${code}`).then((res) => {

        console.log(res);
        this.name = res.data.name;
        this.market_price = res.data.market_price;
        http.get("/price/" + this.$route.params.code).then((res) => {
          this.cur_price = res.data.price;
        });


        this.temp_obj = JSON.parse(res.data.data);
        this.stockName = res.data.name;
      });
    },

    postSimulationList(context) {
      const data = {
        code: this.$route.params.code,
        name: this.name,
        quantity: this.buy_count,
        price: this.cur_price,
      };
      http
        .post("/simulations/simulation", data, {
          headers: {
            Authorization: "JWT " + this.$store.state.token,
          },
        })
        .then(({ data }) => {
          this.$store.commit("setSimulationList", data);
          alert(
            this.name +
              " " +
              this.buy_count +
              "주가 " +
              this.cur_price +
              "원에 매수되었습니다."
          );
          this.buy_count = null;
        });

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