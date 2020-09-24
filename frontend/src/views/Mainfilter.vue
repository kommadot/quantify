<template>
  <div>
    <!--Tables-->
    <div class="row">
      <div class="col-xl-12 mb-5 mb-xl-0">
        <!-- header -->
        <base-header type="gradient-success" class="pb-3 pb-3 pt-5 pt-md-8"></base-header>

        <!-- filter -->
        <div
          id="filter-division"
          class="row align-items-center text-center my-4 mx-0 py-2 bg-gradient-success"
          style="width:100%; border-radius:5px"
        >
          <!-- Report Condition Check Boxes -->
          <v-row justify="space-around">
            <v-checkbox v-model="lowval" class="mx-2" label="저변동성 전략"></v-checkbox>
            <v-checkbox v-model="momentum" class="mx-2" label="모멘텀 전략"></v-checkbox>
            <v-checkbox v-model="value" class="mx-2" label="밸류 전략"></v-checkbox>
            <v-checkbox v-model="quality" class="mx-2" label="퀄리티 전략"></v-checkbox>
          </v-row>

          <!-- find term calendar -->
          <div class="col-9 col-lg-5 d-flex">
            <b-form-group id="input-group-3" class="pl-0 pr-1 my-auto col-6">
              <b-form-datepicker
                id="example-datepicker1"
                v-model="startdate"
                @input="optionController"
                label-help
                label-no-date-selected="시작일"
                :max="maxdate"
                today-button
                reset-button
                close-button
                :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
              ></b-form-datepicker>
            </b-form-group>
            <b-form-group id="input-group-3" class="pl-1 pr-0 my-auto col-6">
              <b-form-datepicker
                id="example-datepicker2"
                v-model="enddate"
                class
                @input="optionController"
                label-help
                label-no-date-selected="종료일"
                :min="startdate"
                :max="today"
                today-button
                reset-button
                close-button
                :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
              ></b-form-datepicker>
            </b-form-group>
          </div>

          <!-- button -->
          <div class="col-3 col-lg-2">
            <b-button pill variant="info">검색</b-button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import http from "@/util/http-common";

export default {
  name: "main-filter",
  data: () => {
    return {
      selected: [],
      options: [
        { item: 0, name: "저변동성 전략" },
        { item: 1, name: "모멘텀 전략" },
        { item: 2, name: "밸류 전략" },
        { item: 3, name: "퀄리티 전략" },
      ],
      startdate: "",
      enddate: "",
      maxdate: "",
      today: "",
    };
  },
  mounted() {
    this.getToday();
  },
  methods: {
    getToday() {
      var today = new Date();
      var dd = today.getDate();
      var mm = today.getMonth() + 1;
      var yyyy = today.getFullYear();

      if (dd < 10) {
        dd = "0" + dd;
      }

      if (mm < 10) {
        mm = "0" + mm;
      }

      today = yyyy + "-" + mm + "-" + dd;
      this.today = today;
      this.maxdate = today;
    },
  },
};
</script>
<style>
</style>