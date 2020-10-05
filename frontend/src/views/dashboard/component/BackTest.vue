<template>
  <v-container id="dashboard" fluid tag="section">
    <v-container fluid>
      <v-row>
        <v-col cols="1.5">
          <v-checkbox
            v-model="checked"
            label="저변동성 전략"
            value="lowvar"
            dark
          ></v-checkbox>
        </v-col>
        <v-col cols="1.5">
          <v-checkbox
            v-model="checked"
            label="모멘텀 전략"
            value="momentum"
            dark
          ></v-checkbox>
        </v-col>
        <v-col cols="1.5">
          <v-checkbox
            v-model="checked"
            label="퀄리티 전략"
            value="quality"
            dark
          ></v-checkbox>
        </v-col>
        <v-col cols="1.5">
          <v-checkbox
            v-model="checked"
            label="밸류 전략"
            value="value"
            dark
          ></v-checkbox>
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
          <v-btn @click="backtesting"> 백테스트 시작 </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <div id="chart"></div>
        <base-material-card
          color="#283593"
          dark
          title="퀀트 투자의 시작 QUANTIFY"
          class="px-5 py-3 mx-6"
        >
          <div v-for="ld in log_data" :key="ld.id">
            <span>{{ ld.date }}에 </span>
            <br />
            <div v-for="data in ld.datas" :key="data.id">
              <span>{{ data.code }}종목 </span>
              <span>{{ data.quantify }}주를 </span>
              <span>{{ data.price }}원에 </span>
            </div>
            <span>{{ ld.types }}</span>
          </div>
        </base-material-card>
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
      log_data: [],
    };
  },
  watch: {},
  methods: {
    backtesting() {
      http
        .post(
          "/backtest/backtest",
          {
            start: this.date1,
            end: this.date2,
            budget: 1000000,
            rebalance: 6,
          },
          {
            headers: {
              Authorization: "JWT " + this.$store.state.token,
            },
          }
        )
        .then((res) => {
          this.log_data = res.data.log;
          console.log(res);
          const a = [];
          const data = JSON.parse(res.data.data);
          data.forEach((r) => {
            a.push({ time: r[0], value: r[1] });
          });
          this.lineSeries.setData(a);
        });
    },
  },
  mounted() {
    this.chart = LightweightCharts.createChart(
      document.getElementById("chart"),
      {
        width: 600,
        height: 300,
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
};
</script>
