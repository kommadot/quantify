<template>
  <div class="control-section">
    <div>
      <ejs-stockchart
        style="display:block"
        id="stockchartcontainerdefault"
        :primaryXAxis="primaryXAxis"
        :primaryYAxis="primaryYAxis"
        :chartArea="chartArea"
        :tooltip="tooltip"
        :crosshair="crosshair"
        :tooltipRender="tooltipRender"
        :title="title"
        :border="border"
        :enablePeroiSelector="enablePeroiSelector"
        :theme="theme"
      >
        <e-stockchart-series-collection>
          <e-stockchart-series
            :dataSource="seriesData"
            type="Candle"
            volume="volume"
            xName="x"
            low="low"
            high="high"
            open="open"
            close="close"
          ></e-stockchart-series>
        </e-stockchart-series-collection>
      </ejs-stockchart>
    </div>
  </div>
</template>
<script>
import Vue from "vue";
import { Browser } from "@syncfusion/ej2-base";
import { chartData } from "./indicator-data";
import {
  StockChartPlugin,
  DateTime,
  CandleSeries,
  Tooltip,
  Crosshair,
  RangeTooltip,
  LineSeries,
  SplineSeries,
  HiloOpenCloseSeries,
  HiloSeries,
  RangeAreaSeries,
  Trendlines,
  EmaIndicator,
  RsiIndicator,
  BollingerBands,
  TmaIndicator,
  MomentumIndicator,
  SmaIndicator,
  AtrIndicator,
  AccumulationDistributionIndicator,
  MacdIndicator,
  StochasticIndicator,
  Export,
} from "@syncfusion/ej2-vue-charts";

Vue.use(StockChartPlugin);

let selectedTheme = location.hash.split("/")[1];
selectedTheme = selectedTheme ? selectedTheme : "Material";
let theme = (
  selectedTheme.charAt(0).toUpperCase() + selectedTheme.slice(1)
).replace(/-dark/i, "Dark");

export default Vue.extend({
  data: function () {
    return {
      seriesData: chartData,
      theme: theme,
      //Initializing Primary X Axis
      primaryXAxis: {
        valueType: "DateTime",
        majorGridLines: { color: "transparent" },
        crosshairTooltip: { enable: true },
      },

      //Initializing Primary Y Axis
      primaryYAxis: {
        lineStyle: { color: "transparent" },
        majorTickLines: { color: "transparent", width: 0 },
      },
      crosshair: {
        enable: true,
      },
      title: "AAPL Stock Price",
      chartArea: {
        border: {
          width: 0,
        },
      },
      border: { width: 0 },
      enablePeroiSelector: true,
      tooltip: { enable: true },
    };
  },
  provide: {
    stockChart: [
      DateTime,
      Tooltip,
      Crosshair,
      RangeTooltip,
      LineSeries,
      SplineSeries,
      CandleSeries,
      HiloOpenCloseSeries,
      HiloSeries,
      RangeAreaSeries,
      Trendlines,
      EmaIndicator,
      RsiIndicator,
      BollingerBands,
      TmaIndicator,
      MomentumIndicator,
      SmaIndicator,
      AtrIndicator,
      AccumulationDistributionIndicator,
      MacdIndicator,
      StochasticIndicator,
      Export,
    ],
  },
  methods: {
    tooltipRender: function (args) {
      if (args.text.split("<br/>")[4]) {
        let target = parseInt(
          args.text.split("<br/>")[4].split("<b>")[1].split("</b>")[0]
        );
        let value = (target / 100000000).toFixed(1) + "B";
        args.text = args.text.replace(
          args.text.split("<br/>")[4].split("<b>")[1].split("</b>")[0],
          value
        );
      }
    },
  },
});
</script>
