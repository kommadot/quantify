<template>
  <v-container id="dashboard" fluid tag="section">
    <v-container fluid>
      <v-row>
        <!-- checkboxes -->
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

        <!-- <v-col cols="6">
          <v-overflow-btn
            class="my-2"
            v-model="dropdownselected"
            :items="dropdown_font"
            label="전략 선택"
            target="#dropdown-example"
            dark
          ></v-overflow-btn>
        </v-col> -->

        <!-- calendar -->
        <!-- startdate -->
        <!-- <v-col cols="3">
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
        </v-col> -->
        <!-- enddate -->
        <!-- <v-col cols="3">
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
        </v-col> -->
      </v-row>
      <v-data-table
        :headers="headers"
        :items="filtertable"
        :sort-desc="[false, true]"
        multi-sort
        class="elevation-1"
        dark
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
      dropdown_font: [
        "저변동성 전략",
        "모멘텀 전략",
        "퀄리티 전략",
        "밸류 전략",
      ],
      checked: [],
      dropdownselected: "",
      headers: [],
      lowvartable: [],
      // momentable: [],
      riskmomentable: [],
      qualitytable: [],
      valuetable: [],
      filtertable: [],
      menu1: false,
      menu2: false,
      date1: new Date().toISOString().substr(0, 10),
      date2: new Date().toISOString().substr(0, 10),
    };
  },
  watch: {
    // dropdownselected(value) {
    //   if (value == "저변동성 전략") {
    //     this.headers = [
    //       {
    //         text: "순위",
    //         align: "start",
    //         sortable: false,
    //         value: "rank",
    //       },
    //       { text: "기업명", value: "name" },
    //       { text: "변동성", value: "variability" },
    //     ];
    //     this.filtertable = this.lowvartable;
    //   }

    //   if (value == "모멘텀 전략") {
    //     this.headers = [
    //       {
    //         text: "순위",
    //         align: "start",
    //         sortable: false,
    //         value: "rank",
    //       },
    //       { text: "기업명", value: "name" },
    //       { text: "위험조정수익률", value: "riskmomentum" },
    //     ];
    //     this.filtertable = this.riskmomentable;
    //   }

    //   if (value == "퀄리티 전략") {
    //     this.headers = [
    //       {
    //         text: "순위",
    //         align: "start",
    //         sortable: false,
    //         value: "rank",
    //       },
    //       { text: "기업명", value: "name" },
    //       { text: "퀄리티 합계", value: "sum" },
    //     ];
    //     this.filtertable = this.qualitytable;
    //   }

    //   if (value == "밸류 전략") {
    //     this.headers = [
    //       {
    //         text: "순위",
    //         align: "start",
    //         sortable: false,
    //         value: "rank",
    //       },
    //       { text: "기업명", value: "name" },
    //       { text: "PER", value: "per" },
    //       { text: "PSR", value: "psr" },
    //       { text: "PBR", value: "pbr" },
    //       { text: "F-Score", value: "score" },
    //     ];
    //     this.filtertable = this.valuetable;
    //   }
    // },

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
            },
            { text: "기업명", value: "name" },
            { text: "변동성", value: "variability" },
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
            },
            { text: "기업명", value: "name" },
            { text: "위험조정수익률", value: "riskmomentum" },
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
            },
            { text: "기업명", value: "name" },
            { text: "퀄리티 합계", value: "sum" },
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
            },
            { text: "기업명", value: "name" },
            { text: "PER", value: "per" },
            { text: "PSR", value: "psr" },
            { text: "PBR", value: "pbr" },
            { text: "F-Score", value: "score" },
          ];
          this.filtertable = this.valuetable;
        }
      }

      // 선택된게 0개일때 초기화
      if (value.length == 0) {
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
          },
          { text: "기업명", value: "name" },
        ];
        this.filtertable = [];
        var temp_obj = {};
        // [{}]
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
              variability: i.variability,
            });
          }
        })
        .catch(function (err) {
          alert(err);
        });
    },

    // momenlist: function () {
    //   const self = this;
    //   let idx = 1;
    //   http
    //     .get("/strategy/momen")
    //     .then(function (res) {
    //       self.momentable = [];
    //       for (let i of res.data) {
    //         self.momentable.push({
    //           rank: idx++,
    //           name: i.name,
    //           momentum: i.momentum,
    //         });
    //       }
    //     })
    //     .catch(function (err) {
    //       alert(err);
    //     });
    // },

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
              riskmomentum: i.risk_momentum,
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
          // console.log(res.data);
          for (let i of res.data) {
            self.valuetable.push({
              rank: idx++,
              name: i.name,
              per: i.per,
              pbr: i.pbr,
              psr: i.psr,
              score: i.rank,
            });
          }
          // console.log(self.valuetable);
        })
        .catch(function (err) {
          alert(err);
        });
    },
  },
  created() {
    this.lowvarlist();
    // this.momenlist();
    this.riskmomenlist();
    this.qualitylist();
    this.valuelist();
  },
};
</script>
