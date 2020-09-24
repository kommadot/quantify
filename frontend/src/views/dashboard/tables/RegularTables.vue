<template>
  <v-container id="regular-tables" fluid tag="section">
    <base-material-card
      color="success"
      dark
      icon="mdi-chart-line"
      title="모의투자현황"
      class="px-5 py-3"
    >
      <v-simple-table class="my-3" style="border: 1px solid green">
        <tbody>
          <tr>
            <td style="font-size: 130%">총평가금액</td>
            <td style="font-size: 130%">
              {{ EvaluatedPrice | numberWithCommas }}
            </td>

            <td style="font-size: 130%; border-left: 1px solid green">
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

            <td style="font-size: 130%; border-left: 1px solid green">
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
          </tr>
        </tbody>
      </v-simple-table>
    </base-material-card>
    <v-btn small @click="getSimulationList">list</v-btn>
    <v-btn small @click="sadf">update</v-btn>
    <div v-for="s in simulationlist" :key="s._id">
      <p>{{ s }}</p>
    </div>
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
  /*
          item_name: "",
          평가손익: (현재가 - 매수단가) * 보유수량,
          수익률: ((현재가 - 매수단가) / 매수단가) * 100,
          평가금액: 현재가 * 보유수량,
          보유수량: 0,
          매수단가: 0,
          현재가: 0,
  */
  methods: {
    ...mapActions(["getSimulationList"]),
    // getStocks() {
    //   for (s in simulationlist) {
    //     let cur_price = 0;
    //     http.get("/api/price" + s.item_code).then((res) => {
    //       cur_price = res.data;
    //     });
    //     const a = {};
    //     a["quantity"] = s.quantity;
    //     a["price"] = s.price;
    //     a["profit"] = s.quantity * cur_price - s.quantity * s.price;
    //     a["rate"] = ((cur_price - s.price) / s.price) * 100;
    //     a["cur_price"] = cur_price;
    //     a["item_name"] = s.name;
    //     a["eval"] = cur_price * s.quantity;
    //     this.stocks.push(a);
    //   }
    //   console.log(this.stocks);
    // },
    setupdate() {
      this.stocks.forEach((el) => {
        http.get("/price/" + el.item_code).then((res) => {
          // const cur_price = res.data.price;
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
  },
  watch: {
    simulationlist(value) {
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
          this.stocks.push(a);
        });
      });
      console.log(this.stocks);
    },
  },
};
</script>