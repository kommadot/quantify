<template>
  <v-container id="dashboard" fluid tag="section">
    <v-container fluid>
      <!-- filter -->
      <v-row>
        <!-- 저변동성 전략 -->
        <v-col class="d-flex flex-nowrap justify-center">
          <v-checkbox
            v-model="checked"
            label="저변동성 전략"
            value="lowvar"
            dark
          >
          </v-checkbox>
          <v-tooltip bottom max-width="1150px" nudge-right="235px;">
            <template v-slot:activator="{ on, attrs }">
              <span
                v-bind="attrs"
                v-on="on"
                style="color: white; margin: 15px 0px 30px 5px"
                >?</span
              >
            </template>
            <span>
              <p>
                <br />
                전통적 금융 이론에서는 수익률의 변동성이 클수록 위험이 크고,
                이런 위험에 대한 보상으로 기대수익률이 높아야 한다고 보았습니다.
              </p>
              <p>
                따라서 고변동성 종목의 기대수익률이 크고, 저변동성 종목의
                기대수익률이 낮은 고위험 고수익이 당연한 믿음이었습니다.
              </p>
              <p>
                그러나 현실에서는 오히려 변동성이 낮은 종목들의 수익률이
                변동성이 높은 종목들의 수익률보다 높은,
                <strong>저변동성 효과</strong>가 발견되고 있습니다.
              </p>
              <p>
                따라서 <strong>변동성이 적은 주식</strong>은 장기적으로 시장에
                영향을 많이 받는 주식들보다
                <strong>수익률이 좋고 보다 안정적인 수익을 기대</strong>할 수
                있습니다.
              </p>
            </span>
          </v-tooltip>
        </v-col>

        <!-- 모멘텀 전략 -->
        <v-col class="d-flex flex-nowrap justify-center">
          <v-checkbox
            v-model="checked"
            label="모멘텀 전략"
            value="momentum"
            dark
          ></v-checkbox>
          <v-tooltip bottom max-width="1150px" nudge-right="0px;">
            <template v-slot:activator="{ on, attrs }">
              <span
                v-bind="attrs"
                v-on="on"
                style="color: white; margin: 15px 0px 30px 5px"
                >?</span
              >
            </template>
            <span>
              <p>
                <br />
                투자에서 모멘텀이란 주가 혹은 이익의 추세로서,
                <strong>상승 추세의 주식은 지속적으로 상승하는 경향</strong>을
                보입니다.
              </p>
              <p>
                1년간의 수익률과 변동성을 고려한
                <strong>위험조정 수익률</strong>을 제공합니다.
              </p>
            </span>
          </v-tooltip>
        </v-col>

        <!-- 퀄리티 전략 -->
        <v-col class="d-flex flex-nowrap justify-center">
          <v-checkbox
            v-model="checked"
            label="퀄리티 전략"
            value="quality"
            dark
          ></v-checkbox>
          <v-tooltip bottom max-width="1150px" nudge-right="0px;">
            <template v-slot:activator="{ on, attrs }">
              <span
                v-bind="attrs"
                v-on="on"
                style="color: white; margin: 15px 0px 30px 5px"
                >?</span
              >
            </template>
            <span>
              <p>
                <br />
                퀄리티 전략은 기업의 재무제표 데이터를 활용하여
                <strong>기업의 우량성 정도</strong>를 나타내는
                <strong>F-score</strong>를 계산합니다.
              </p>
              <p>
                <strong
                  >수익성, 수익의 안정성, 기업 구조, 수익의 성장성, 회계적
                  우량성, 배당, 투자</strong
                >등의 가치를 종합적으로 분석합니다.
              </p>
            </span>
          </v-tooltip>
        </v-col>

        <!-- 밸류 전략 -->
        <v-col class="d-flex flex-nowrap justify-center">
          <v-checkbox
            v-model="checked"
            label="밸류 전략"
            value="value"
            dark
          ></v-checkbox>
          <v-tooltip bottom max-width="1150px" nudge-right="0px;">
            <template v-slot:activator="{ on, attrs }">
              <span
                v-bind="attrs"
                v-on="on"
                style="color: white; margin: 15px 0px 30px 5px"
                >?</span
              >
            </template>
            <span>
              <p>
                <br />
                밸류 전략은
                <strong>내재 가치 대비 낮은 가격의 주식(저PER, 저PBR 등)</strong
                >이, 내재 가치 대비 비싼 주식보다
                <strong>수익률이 높은 현상</strong>을 이용합니다.
              </p>
              <p>
                <strong>PER, PBR, PSR</strong>에 각 기업의 순위를 매겨 종합
                순위가 낮은 주식을 추천합니다.
              </p>
            </span>
          </v-tooltip>
        </v-col>
      </v-row>

      <!-- table -->
      <v-data-table
        :headers="headers"
        :items="filtertable"
        :sort-desc="[false, true]"
        multi-sort
        class="elevation-1"
        dark
        no-data-text="전략을 선택해 주세요"
      ></v-data-table>
    </v-container>
  </v-container>
</template>

<script>
import http from "@/util/http-common";

export default {
  name: "Strategy",

  data() {
    return {
      checked: [],
      headers: [],
      lowvartable: [],
      riskmomentable: [],
      qualitytable: [],
      valuetable: [],
      filtertable: [],
    };
  },
  watch: {
    checked(value) {
      // 선택된게 1개일때
      if (value.length == 1) {
        if (value[0] == "lowvar") {
          this.headers = [
            {
              text: "순위",
              align: "start",
              sortable: false,
              value: "rank",
              width: "33%",
            },
            { text: "기업명", sortable: false, value: "name", width: "33%" },
            {
              text: "변동성",
              sortable: false,
              value: "variability",
              width: "33%",
            },
          ];
          this.filtertable = this.lowvartable;
        }
        if (value[0] == "momentum") {
          this.headers = [
            {
              text: "순위",
              align: "start",
              sortable: false,
              value: "rank",
              width: "33%",
            },
            { text: "기업명", sortable: false, value: "name", width: "33%" },
            {
              text: "위험조정수익률",
              sortable: false,
              value: "riskmomentum",
              width: "33%",
            },
          ];
          this.filtertable = this.riskmomentable;
        }
        if (value[0] == "quality") {
          this.headers = [
            {
              text: "순위",
              align: "start",
              sortable: false,
              value: "rank",
              width: "33%",
            },
            { text: "기업명", sortable: false, value: "name", width: "33%" },
            {
              text: "퀄리티 합계",
              sortable: false,
              value: "sum",
              width: "33%",
            },
          ];
          this.filtertable = this.qualitytable;
        }
        if (value[0] == "value") {
          this.headers = [
            {
              text: "순위",
              align: "start",
              sortable: false,
              value: "rank",
              width: "10%",
            },
            { text: "기업명", sortable: false, value: "name", width: "15%" },
            { text: "PER", value: "per", width: "15%" },
            { text: "PSR", value: "psr", width: "15%" },
            { text: "PBR", value: "pbr", width: "15%" },
            { text: "F-Score", sortable: false, value: "score", width: "15%" },
          ];
          this.filtertable = this.valuetable;
        }
      }

      // 선택된게 0개일때 초기화
      if (value.length == 0) {
        this.headers = [];
        this.filtertable = [];
      }

      // 선택된게 2개 이상일때
      if (value.length > 1) {
        this.headers = [
          {
            text: "순위",
            align: "start",
            sortable: false,
            value: "rank",
            width: "25%",
          },
          { text: "기업명", sortable: false, value: "name", width: "50%" },
        ];
        this.filtertable = [];
        var temp_obj = {};
        if (value.includes("lowvar")) {
          for (let i of this.lowvartable) {
            if (i.name in temp_obj) {
              temp_obj[i.name].rank += i.rank;
              temp_obj[i.name].num += 1;
            } else {
              temp_obj[i.name] = { name: i.name, rank: i.rank, num: 1 };
            }
          }
        }
        if (value.includes("momentum")) {
          for (let i of this.riskmomentable) {
            if (i.name in temp_obj) {
              temp_obj[i.name].rank += i.rank;
              temp_obj[i.name].num += 1;
            } else {
              temp_obj[i.name] = { name: i.name, rank: i.rank, num: 1 };
            }
          }
        }
        if (value.includes("quality")) {
          for (let i of this.qualitytable) {
            if (i.name in temp_obj) {
              temp_obj[i.name].rank += i.rank;
              temp_obj[i.name].num += 1;
            } else {
              temp_obj[i.name] = { name: i.name, rank: i.rank, num: 1 };
            }
          }
        }
        if (value.includes("value")) {
          for (let i of this.valuetable) {
            if (i.name in temp_obj) {
              temp_obj[i.name].rank += i.rank;
              temp_obj[i.name].num += 1;
            } else {
              temp_obj[i.name] = { name: i.name, rank: i.rank, num: 1 };
            }
          }
        }
        this.filtertable = Object.values(temp_obj);
        for (let i of this.filtertable) {
          i.rank /= i.num;
        }
        this.filtertable.sort(function (a, b) {
          return a["rank"] - b["rank"];
        });
        var cnt = 0;
        for (let i of this.filtertable) {
          cnt += 1;
          i.rank = cnt;
        }
      }
    },
  },

  methods: {
    lowvarlist: function () {
      const self = this;
      let idx = 1;
      http
        .get("/strategy/lowvar")
        .then(function (res) {
          self.lowvartable = [];
          for (let i of res.data) {
            self.lowvartable.push({
              rank: idx++,
              name: i.name,
              variability: i.variability.toFixed(3),
            });
          }
        })
        .catch(function (err) {
          alert(err);
        });
    },

    riskmomenlist: function () {
      const self = this;
      let idx = 1;
      http
        .get("/strategy/riskmomen")
        .then(function (res) {
          self.riskmomentable = [];
          for (let i of res.data) {
            self.riskmomentable.push({
              rank: idx++,
              name: i.name,
              riskmomentum: i.risk_momentum.toFixed(3),
            });
          }
        })
        .catch(function (err) {
          alert(err);
        });
    },

    qualitylist: function () {
      const self = this;
      let idx = 1;
      http
        .get("/strategy/quality")
        .then(function (res) {
          self.qualitytable = [];
          for (let i of res.data) {
            self.qualitytable.push({
              rank: idx++,
              name: i.name,
              sum: i.sum,
            });
          }
        })
        .catch(function (err) {
          alert(err);
        });
    },

    valuelist: function () {
      let self = this;
      let idx = 1;
      http
        .get("/strategy/value")
        .then(function (res) {
          self.valuetable = [];
          for (let i of res.data) {
            self.valuetable.push({
              rank: idx++,
              name: i.name,
              per: i.per.toFixed(3),
              pbr: i.pbr.toFixed(3),
              psr: i.psr.toFixed(3),
              score: i.rank,
            });
          }
        })
        .catch(function (err) {
          alert(err);
        });
    },
  },
  created() {
    this.lowvarlist();
    this.riskmomenlist();
    this.qualitylist();
    this.valuelist();
  },
  filters: {
    DecimalPoint3(value) {
      return value.toFixed(3);
    },
    numberWithCommas(x) {
      return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },
  },
};
</script>

<style scoped>
</style>