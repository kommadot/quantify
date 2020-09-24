<template>
  <v-container id="dashboard" fluid tag="section">
    <v-container fluid>
      <v-row>
        <!-- checkboxes -->
        <v-col cols="1.5">
          <v-checkbox
            v-model="selected"
            label="저변동성 전략"
            value="저변동성 전략"
            dark
          ></v-checkbox>
        </v-col>
        <v-col cols="1.5">
          <v-checkbox
            v-model="selected"
            label="모멘텀 전략"
            value="모멘텀 전략"
            dark
          ></v-checkbox>
        </v-col>
        <v-col cols="1.5">
          <v-checkbox
            v-model="selected"
            label="퀄리티 전략"
            value="퀄리티 전략"
            dark
          ></v-checkbox>
        </v-col>
        <v-col cols="1.5">
          <v-checkbox
            v-model="selected"
            label="밸류 전략"
            value="밸류 전략"
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
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
export default {
  name: "DashboardDashboard",

  data() {
    return {
      selected: [],
      date1: new Date().toISOString().substr(0, 10),
      date2: new Date().toISOString().substr(0, 10),
    };
  },
};
</script>
