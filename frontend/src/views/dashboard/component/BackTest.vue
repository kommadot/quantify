<template>
  <v-container id="dashboard" fluid tag="section">
    <v-container fluid>
      <v-row>
        <v-radio-group v-model="strategy" row>
          <v-radio label="저변동성 전략" value="1" dark></v-radio>
          <v-radio label="모멘텀 전략" value="2" dark></v-radio>
        </v-radio-group>

        <v-col cols="1.5">
          <p class="text-left mb-0" style="color: white">리밸런싱 기간(개월)</p>
          <v-slider
            v-model="rebalance"
            :tick-labels="ticksLabels"
            :max="5"
            step="1"
            ticks="always"
            tick-size="3"
            dark
          ></v-slider>
        </v-col>

        <v-col cols="1.5">
          <v-text-field v-model="budget" label="투자 자본" dark></v-text-field>
        </v-col>

        <!-- calendar -->
        <!-- startdate -->
        <v-col cols="2">
          <v-menu
            v-model="menu1"
            :close-on-content-click="false"
            :nudge-right="0"
            transition="scale-transition"
            offset-y
            min-width="290px"
            dark
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="date1"
                label="시작일"
                readonly
                v-bind="attrs"
                v-on="on"
                dark
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="date1"
              @input="menu1 = false"
            ></v-date-picker>
          </v-menu>
        </v-col>
        <!-- enddate -->
        <v-col cols="2">
          <v-menu
            v-model="menu2"
            :close-on-content-click="false"
            :nudge-right="0"
            transition="scale-transition"
            offset-y
            min-width="290px"
            dark
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="date2"
                label="종료일"
                readonly
                v-bind="attrs"
                v-on="on"
                max-width="100px"
                dark
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="date2"
              @input="menu2 = false"
            ></v-date-picker>
          </v-menu>
        </v-col>
        <v-col cols="2">
          <v-btn color="#283593" @click="backtesting"> 백테스트 시작 </v-btn>
        </v-col>
      </v-row>

      <!-- chart -->
      <v-row>
        <v-col cols="7">
          <div id="chart"></div>
        </v-col>
        <v-col cols="5">
          <v-row>
            <v-spacer></v-spacer>
            <div class="text-center">
              <v-menu offset-y>
                <template v-slot:activator="{ on, attrs }">
                  <v-btn color="#283593" dark v-bind="attrs" v-on="on">
                    BACKTEST RESULTS
                  </v-btn>
                </template>
                <div
                  class="d-flex flex-column align-center py-3"
                  style="
                    background-color: #0c154a;
                    overflow: auto;
                    width: 400px;
                    height: 300px;
                  "
                >
                  <v-card
                    color="#192DA1"
                    class="py-2"
                    style="width: 90%; margin-top: 3px"
                    dark
                    @click="clickCard(data)"
                    v-for="data in datas"
                    :key="data.id"
                  >
                    <v-card-title v-if="data.strategy == 1"
                      >저변동성 전략</v-card-title
                    >
                    <v-card-title v-else>모멘텀 전략</v-card-title>
                    <v-card-title
                      >{{ data.logs[0].date }} ~
                      {{ data.logs[1].date }}</v-card-title
                    >
                    <v-card-title
                      >수익률 : {{ data.datas | earningRate }}%</v-card-title
                    >
                  </v-card>
                </div>
              </v-menu>
            </div>
          </v-row>
          <v-row>
            <base-material-card
              color="#435965"
              dark
              title="BACKTEST LOG"
              style="width: 100%"
            >
              <div style="margin-top: 33px; overflow: auto; height: 200px">
                <div v-for="log in logs" :key="log.id">
                  <span>{{ log.date }}에 </span>
                  <div v-for="log_data in log.datas" :key="log_data.id">
                    <span>{{ log_data.name }} </span>
                    <span>{{ log_data.quantity }}주를 </span>
                    <span>{{ log_data.price }}원에 </span>
                    <span v-if="log.types == 'buy'" style="color: red">{{
                      log.types
                    }}</span>
                    <span v-else style="color: skyblue">{{ log.types }}</span>
                  </div>
                  <span v-if="log.types == 'buy'"
                    >주문 금액은 {{ log.datas | getTotalPrice }}원 입니다.</span
                  >
                  <span v-if="log.types == 'sell'"
                    >정산 금액은 {{ log.datas | getTotalPrice }}원 입니다.</span
                  >
                </div>
                <br />
                <span
                  >현재 평가 금액은
                  {{ this.budget_data[this.budget_data.length - 1] }}원 입니다.
                </span>
              </div>
            </base-material-card>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
import http from "@/util/http-common";

export default {
  name: "BackTest",

  data() {
    return {
      checked: [],
      chart: null,
      lineSeries: null,
      menu1: false,
      menu2: false,
      date1: new Date().toISOString().substr(0, 10),
      date2: new Date().toISOString().substr(0, 10),
      budget_data: [],
      datas: {},
      logs: {},
      strategy: null,
      items: [
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me 2" },
      ],
      ticksLabels: [1, 2, 3, 4, 5, 6],
      rebalance: 0,
      budget: 1000000,
    };
  },
  watch: {},
  filters: {
    getTotalPrice(value) {
      let price = 0;
      for (let v of value) {
        price += v.price * v.quantity;
      }
      return price;
    },
    earningRate(value) {
      return (
        ((value[value.length - 1].budget - value[0].budget) / value[0].budget) *
        100
      );
    },
  },
  methods: {
    backtesting() {
      http
        .post("/backtest/backtest", {
          start: this.date1,
          end: this.date2,
          strategy: this.strategy,
          budget: this.budget,
          rebalance: this.rebalance,
        })
        .then((res) => {
          this.logs = res.data.logs;
          console.log(res);
          const a = [];
          const data = res.data.data;
          data.forEach((r) => {
            a.push({ time: r["date"], value: r["budget"] });
            this.budget_data.push(r["budget"]);
          });
          this.lineSeries.setData(a);
        });
    },
    clickCard(data) {
      console.log(data);
      this.logs = data.logs;
      const a = [];
      data.datas.forEach((r) => {
        a.push({ time: r["date"], value: r["budget"] });
        this.budget_data.push(r["budget"]);
      });
      console.log(this.budget_data);
      this.lineSeries.setData(a);
    },
  },
  mounted() {
    this.chart = LightweightCharts.createChart(
      document.getElementById("chart"),
      {
        width: 650,
        height: 350,
        layout: {
          backgroundColor: "#000000",
          textColor: "rgba(255, 255, 255, 0.9)",
        },
        rightPriceScale: {
          scaleMargins: {
            top: 0.1,
            bottom: 0.1,
          },
        },
      }
    );
    this.lineSeries = this.chart.addLineSeries({
      color: "rgba(33, 150, 243, 1)",
      lineWidth: 3,
    });
  },
  created() {
    http.get("/backtest/backtest").then((res) => {
      console.log(res);
      this.datas = res.data;
      console.log(this.datas);
    });
  },
};
</script>
