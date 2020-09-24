<template>
  <v-container id="dashboard" fluid tag="section">
    <v-row justify="space-around">
      <v-col cols="12" sm="6" md="6">
        <v-row>
          <v-checkbox v-model="lowval" class="mx-2 red--text" label="저변동성 전략"></v-checkbox>
          <v-checkbox v-model="momentum" class="mx-2" label="모멘텀 전략"></v-checkbox>
          <v-checkbox v-model="value" class="mx-2" label="밸류 전략"></v-checkbox>
          <v-checkbox v-model="quality" class="mx-2" label="퀄리티 전략"></v-checkbox>
        </v-row>
      </v-col>

      <v-col cols="12" sm="6" md="3">
        <v-menu
          v-model="menu2"
          :close-on-content-click="false"
          :nudge-right="40"
          transition="scale-transition"
          offset-y
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field v-model="date" label="시작일" readonly v-bind="attrs" v-on="on"></v-text-field>
          </template>
          <v-date-picker v-model="date" @input="menu2 = false"></v-date-picker>
        </v-menu>
      </v-col>
      <v-col cols="12" sm="6" md="3">
        <v-menu
          v-model="menu2"
          :close-on-content-click="false"
          :nudge-right="40"
          transition="scale-transition"
          offset-y
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="date"
              label="종료일"
              readonly
              v-bind="attrs"
              v-on="on"
              max-width="100px"
            ></v-text-field>
          </template>
          <v-date-picker v-model="date" @input="menu2 = false"></v-date-picker>
        </v-menu>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "DashboardDashboard",

  data() {
    return {
      dailySalesChart: {
        data: {
          labels: ["M", "T", "W", "T", "F", "S", "S"],
          series: [[12, 17, 7, 17, 23, 18, 38]],
        },
        options: {
          lineSmooth: this.$chartist.Interpolation.cardinal({
            tension: 0,
          }),
          low: 0,
          high: 50, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
          chartPadding: {
            top: 0,
            right: 0,
            bottom: 0,
            left: 0,
          },
        },
      },
    };
  },
  methods: {
    complete(index) {
      this.list[index] = !this.list[index];
    },
  },
};
</script>
