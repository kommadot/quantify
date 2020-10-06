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
          title="BACKTEST LOG"
          class="px-5 py-3 mx-6"
        >
          <!-- datas = res.data -->
          <!-- <div v-for="data in datas.logs" :key="data.id"> -->
          <div v-for="log in datas.logs" :key="log.id">
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
            <span v-if="log.types == 'buy'"
              ><br />현재 평가 금액은 1000000원 입니다.</span
            >

            <span v-if="log.types == 'sell'"
              >정산 금액은 {{ log.datas | getTotalPrice }}원 입니다.</span
            >
          </div>
          <span
            >현재 평가 금액은
            {{ this.budget_data[this.budget_data.length - 1] }}원 입니다.
          </span>

          <!-- </div> -->
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
      budget_data: [],
      datas: {},
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
  },
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
          this.datas = res.data;
          console.log(res);
          const a = [];
          const data = res.data.data;
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
  created() {
    http
      .get("/backtest/backtest", {
        headers: {
          Authorization: "JWT " + this.$store.state.token,
        },
      })
      .then((res) => {
        console.log(res);
        this.datas = res.data;
        console.log(this.datas);
        const a = [];
        let data = res.data.data;
        console.log(data);
        data.forEach((r) => {
          a.push({ time: r["date"], value: r["budget"] });
          this.budget_data.push(r["budget"]);
        });
        console.log(this.budget_data);
        this.lineSeries.setData(a);
      });
  },
};
</script>
