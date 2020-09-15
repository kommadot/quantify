<template>
  <div>
    <!--Tables-->
    <div class="row">
      <div class="col-xl-12 mb-5 mb-xl-0">
        <base-header type="gradient-success" class="pb-3 pb-3 pt-5 pt-md-8"></base-header>
        <div class="card">
          <div class="card-header border-0">
            <div class="row align-items-center">
              <div class="col">
                <h3 class="mb-0">저변동성 순위</h3>
              </div>
              <div class="col text-right">
                <a href="#!" class="btn btn-sm btn-primary">전체보기</a>
              </div>
            </div>
          </div>

          <div class="table-responsive">
            <base-table thead-classes="thead-light" :data="tableData">
              <template slot="columns">
                <th>순위</th>
                <th>기업명</th>
                <th>변동성</th>
              </template>

              <template slot-scope="{row}">
                <th scope="row">{{row.rank}}</th>
                <td>{{row.name}}</td>
                <td>{{row.variability}}</td>
              </template>
            </base-table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "low-variability-table",
  data: () => {
    return {
      tableData: [
        {
          rank: "1",
          name: "GS글로벌",
          variability: "0.457956",
        },
        {
          rank: "2",
          name: "HDC현대산업개발",
          variability: "0.54078",
        },
        {
          rank: "3",
          name: "DSR",
          variability: "0.545236",
        },
        {
          rank: "4",
          name: "LG이노텍",
          variability: "0.565614",
        },
        {
          rank: "5",
          name: "KEC",
          variability: "0.605653",
        },
      ],
    };
  },
  methods: {
    lowvarlist: function () {
      const self = this;
      let idx = 1;
      axios
        .get("http://localhost:8000/api/getlowvar")
        .then(function (res) {
          self.tableData = [];
          for (let i of res.data) {
            self.tableData.push({
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
  },
  created() {
    this.lowvarlist();
  },
};
</script>
<style>
</style>