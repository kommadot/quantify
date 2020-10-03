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
        <v-col cols="3">
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
        <v-col cols="3">
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
        <v-col>
          <v-btn @click="backtesting">
            백테스트 시작
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <div id="chart">
        </div>
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
      dropdown_font: [
        "저변동성 전략",
        "모멘텀 전략",
        "퀄리티 전략",
        "밸류 전략"
      ],
      dropdownselected: "",
      headers: [],
      lowvartable: [],
      momentable: [],
      riskmomentable: [],
      qualitytable: [],
      valuetable: [],
      filtertable: [],
      checked: [],
      chart:null,
      lineSeries:null,
      menu1: false,
      menu2: false,
      date1: new Date().toISOString().substr(0, 10),
      date2: new Date().toISOString().substr(0, 10)
    };
  },
  watch: {
  },
  methods: {
    backtesting(){
      http.post("/backtest/backtest",{
        start:this.date1,
        end:this.date2,
        budget:1000000,
        rebalance:6
      }).then(res=>{
        const a = []
        console.log(typeof res.data)
        const data = JSON.parse(res.data)
        data.forEach(r=>{
          // console.log(r)
          a.push({time:r[0],value:r[1]})
        })
        this.lineSeries.setData(a)
      })
    }
  },
  mounted() {
    this.chart = LightweightCharts.createChart(document.getElementById("chart"), {
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
});
this.lineSeries = this.chart.addLineSeries({
  color: 'rgba(33, 150, 243, 1)',
  lineWidth: 3,
});
  }
};
</script>
