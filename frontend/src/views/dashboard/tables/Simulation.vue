<template>
  <v-container id="regular-tables" fluid tag="section">
    <base-material-card
      color="#283593"
      dark
      icon="mdi-chart-line"
      title="모의투자현황"
      class="px-5 py-3"
    >
      <span class="d-flex justify-end">보유현금 : {{ this.budget }}원</span>
      <v-simple-table class="my-3" style="border: 1px solid #283593">
        <tbody>
          <tr>
            <td style="font-size: 130%">총평가금액</td>
            <td style="font-size: 130%">
              {{ EvaluatedPrice | numberWithCommas }}
            </td>

            <td style="font-size: 130%; border-left: 1px solid #283593">
              총평가손익
            </td>
            <td
              v-if="EvaluatedProfitLoss > 0"
              class="red--text"
              style="font-size: 130%"
            >
              {{ EvaluatedProfitLoss | numberWithCommas }}
            </td>
            <td v-if="EvaluatedProfitLoss == 0" style="font-size: 130%">
              {{ EvaluatedProfitLoss | numberWithCommas }}
            </td>
            <td
              v-if="EvaluatedProfitLoss < 0"
              class="blue--text"
              style="font-size: 130%"
            >
              {{ EvaluatedProfitLoss | numberWithCommas }}
            </td>

            <td style="font-size: 130%; border-left: 1px solid #283593">
              수익률
            </td>
            <td
              v-if="EarningsRate > 0"
              class="red--text"
              style="font-size: 130%"
            >
              {{ EarningsRate | DecimalPoint3 }}%
            </td>
            <td v-if="EarningsRate == 0" style="font-size: 130%">
              {{ EarningsRate | DecimalPoint3 }}%
            </td>
            <td
              v-if="EarningsRate < 0"
              class="blue--text"
              style="font-size: 130%"
            >
              {{ EarningsRate | DecimalPoint3 }}%
            </td>
          </tr>
        </tbody>
      </v-simple-table>

      <v-simple-table>
        <thead>
          <tr>
            <th style="font-size: 130%">종목명</th>
            <th class="text-right" style="font-size: 130%">평가손익</th>
            <th class="text-right" style="font-size: 130%">수익률</th>
            <th class="text-right" style="font-size: 130%">평가금액</th>
            <th class="text-right" style="font-size: 130%">보유수량</th>
            <th class="text-right" style="font-size: 130%">매수단가</th>
            <th class="text-right" style="font-size: 130%">현재가</th>
            <th style="width: 100px"></th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="item in stocks" :key="item.item_name">
            <td>{{ item.item_name }}</td>
            <td v-if="item.profit > 0" class="text-right red--text">
              {{ item.profit | numberWithCommas }}
            </td>
            <td v-if="item.profit == 0" class="text-right">
              {{ item.profit | numberWithCommas }}
            </td>
            <td v-if="item.profit < 0" class="text-right blue--text">
              {{ item.profit | numberWithCommas }}
            </td>
            <td v-if="item.rate > 0" class="text-right red--text">
              {{ item.rate | DecimalPoint3 }}%
            </td>
            <td v-if="item.rate == 0" class="text-right">
              {{ item.rate | DecimalPoint3 }}%
            </td>
            <td v-if="item.rate < 0" class="text-right blue--text">
              {{ item.rate | DecimalPoint3 }}%
            </td>
            <td class="text-right">{{ item.eval | numberWithCommas }}</td>
            <td class="text-right">{{ item.quantity | numberWithCommas }}</td>
            <td class="text-right">{{ item.price | numberWithCommas }}</td>
            <td class="text-right">{{ item.cur_price | numberWithCommas }}</td>
            <td>
              <v-btn
                depressed
                color="error"
                @click="deleteSimulationDetail(item._id, item.cur_price)"
              >
                팔기
              </v-btn>
            </td>
          </tr>
        </tbody>
      </v-simple-table>
    </base-material-card>

    <v-overlay :value="overlay">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
  </v-container>
</template>
<script>
import axios from "axios";
import http from "@/util/http-common";
import { mapState, mapActions } from "vuex";

export default {
  name: "",
  data() {
    return {
      stocks: [],
      overlay: false,
      budget: 0,
    };
  },
  computed: {
    EvaluatedPrice() {
      let cnt = 0;
      this.stocks.forEach((el) => {
        cnt += el.eval;
      });
      return cnt;
    },
    EvaluatedProfitLoss() {
      let cnt = 0;
      this.stocks.forEach((el) => {
        cnt += el.profit;
      });
      return cnt;
    },
    EarningsRate() {
      let a = 0;
      let b = 0;
      this.stocks.forEach((el) => {
        a += el.profit;
        b += el.price * el.quantity;
      });
      return (a / b) * 100;
    },
    ...mapState(["simulationlist"]),
  },
  filters: {
    DecimalPoint3(value) {
      return value.toFixed(3);
    },
    numberWithCommas(x) {
      return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },
  },
  created() {
    this.getSimulationList();
    this.getUserBudget();
  },
  methods: {
    ...mapActions(["getSimulationList"]),
    deleteSimulationDetail(_id, cur_price) {
      console.log(this.$store.state.token);
      const data = {
        sell_price: cur_price,
      };
      http
        .put("/simulations/simulation/" + _id, data, {
          headers: {
            Authorization: "JWT " + this.$store.state.token,
          },
        })
        .then((res) => {
          alert("매도되었습니다.");
          this.getUserBudget();
        });
      const idx = this.stocks.findIndex(function (item) {
        return item._id === _id;
      });
      if (idx > -1) this.stocks.splice(idx, 1);
    },
    setupdate() {
      this.stocks.forEach((el) => {
        http.get("/price/" + el.item_code).then((res) => {
          const cur_price = 1000;
          el.cur_price = cur_price;
          el.profit = el.quantity * cur_price - el.quantity * el.price;
          el.rate = ((cur_price - el.price) / el.price) * 100;
          el.eval = cur_price * el.quantity;
        });
      });
    },
    sadf() {
      setInterval(this.setupdate, 5000);
    },
    getUserBudget() {
      http
        .get("/simulations/budget", {
          headers: {
            Authorization: "JWT " + this.$store.state.token,
          },
        })
        .then((res) => {
          this.budget = res.data;
        });
    },
  },
  watch: {
    simulationlist(value) {
      this.overlay = true;
      let cnt = 0;
      let mcnt = 0;
      mcnt = value.length;
      if (value.length == 0) {
        this.overlay = false;
      }
      value.forEach((s) => {
        let cur_price = 0;
        http.get("/price/" + s.item_code).then((res) => {
          cur_price = res.data.price;
          const a = {};
          a["item_code"] = s.item_code;
          a["quantity"] = s.quantity;
          a["price"] = s.price;
          a["profit"] = s.quantity * cur_price - s.quantity * s.price;
          a["rate"] = ((cur_price - s.price) / s.price) * 100;
          a["cur_price"] = cur_price;
          a["item_name"] = s.item_name;
          a["eval"] = cur_price * s.quantity;
          a["_id"] = s._id;
          this.stocks.push(a);
          cnt += 1;
          if (cnt == mcnt) {
            this.overlay = false;
          }
        });
      });
    },
  },
};
</script>