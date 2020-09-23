<template>
  <v-container id="regular-tables" fluid tag="section">
    <base-material-card color="success" dark icon="mdi-chart-line" title="모의투자현황" class="px-5 py-3">
      <v-simple-table class="my-3" style="border: 1px solid green;">
        <tbody>
          <tr>
            <td style="font-size: 130%;">총평가금액</td>
            <td style="font-size: 130%;">{{ EvaluatedPrice }}</td>

            <td style="font-size: 130%; border-left: 1px solid green;">총평가손익</td>
            <td
              v-if="EvaluatedProfitLoss > 0"
              class="red--text"
              style="font-size: 130%;"
            >{{ EvaluatedProfitLoss }}</td>
            <td v-if="EvaluatedProfitLoss == 0" style="font-size: 130%;">{{ EvaluatedProfitLoss }}</td>
            <td
              v-if="EvaluatedProfitLoss < 0"
              class="blue--text"
              style="font-size: 130%;"
            >{{ EvaluatedProfitLoss }}</td>

            <td style="font-size: 130%; border-left: 1px solid green;">수익률</td>
            <td
              v-if="EarningsRate > 0"
              class="red--text"
              style="font-size: 130%;"
            >{{ EarningsRate | DecimalPoint3 }}%</td>
            <td
              v-if="EarningsRate == 0"
              style="font-size: 130%;"
            >{{ EarningsRate | DecimalPoint3 }}%</td>
            <td
              v-if="EarningsRate < 0"
              class="blue--text"
              style="font-size: 130%;"
            >{{ EarningsRate | DecimalPoint3 }}%</td>
          </tr>
        </tbody>
      </v-simple-table>

      <v-simple-table>
        <thead>
          <tr>
            <th style="font-size: 130%;">종목명</th>
            <th class="text-right" style="font-size: 130%;">평가손익</th>
            <th class="text-right" style="font-size: 130%;">수익률</th>
            <th class="text-right" style="font-size: 130%;">평가금액</th>
            <th class="text-right" style="font-size: 130%;">보유수량</th>
            <th class="text-right" style="font-size: 130%;">매수단가</th>
            <th class="text-right" style="font-size: 130%;">현재가</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="item in stocks" :key="item.종목명">
            <td>{{ item.종목명 }}</td>
            <td v-if="item.평가손익 > 0" class="text-right red--text">{{ item.평가손익 }}</td>
            <td v-if="item.평가손익 == 0" class="text-right">{{ item.평가손익 }}</td>
            <td v-if="item.평가손익 < 0" class="text-right blue--text">{{ item.평가손익 }}</td>
            <td v-if="item.수익률 > 0" class="text-right red--text">{{ item.수익률 | DecimalPoint3 }}%</td>
            <td v-if="item.수익률 == 0" class="text-right">{{ item.수익률 | DecimalPoint3 }}%</td>
            <td v-if="item.수익률 < 0" class="text-right blue--text">{{ item.수익률 | DecimalPoint3 }}%</td>
            <td class="text-right">{{ item.평가금액 }}</td>
            <td class="text-right">{{ item.보유수량 }}</td>
            <td class="text-right">{{ item.매수단가 }}</td>
            <td class="text-right">{{ item.현재가 }}</td>
          </tr>
        </tbody>
      </v-simple-table>
    </base-material-card>
  </v-container>
</template>
<script>
export default {
  name: "",
  data() {
    return {
      stocks: [
        {
          종목명: "삼성전자",
          평가손익: (58000 - 48000) * 10,
          수익률: ((58000 - 48000) / 48000) * 100,
          평가금액: 58000 * 10,
          보유수량: 10,
          매수단가: 48000,
          현재가: 58000,
        },
        {
          종목명: "카카오",
          평가손익: (360000 - 340000) * 20,
          수익률: ((360000 - 340000) / 340000) * 100,
          평가금액: 7200000,
          보유수량: 20,
          매수단가: 340000,
          현재가: 360000,
        },
        {
          종목명: "현대차",
          평가손익: (180000 - 190000) * 15,
          수익률: ((180000 - 190000) / 190000) * 100,
          평가금액: 2700000,
          보유수량: 15,
          매수단가: 190000,
          현재가: 180000,
        },
      ],
    };
  },
  computed: {
    EvaluatedPrice() {
      let cnt = 0;
      this.stocks.forEach((el) => {
        cnt += el.평가금액;
      });
      return cnt;
    },
    EvaluatedProfitLoss() {
      let cnt = 0;
      this.stocks.forEach((el) => {
        cnt += el.평가손익;
      });
      return cnt;
    },
    EarningsRate() {
      let a = 0;
      let b = 0;
      this.stocks.forEach((el) => {
        a += el.평가손익;
        b += el.매수단가 * el.보유수량;
      });
      return (a / b) * 100;
    },
  },
  filters: {
    DecimalPoint3(value) {
      return value.toFixed(3);
    },
  },
};
</script>