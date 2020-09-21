<template>
  <div>
    <!--Tables-->
    <div class="row">
      <base-header type="gradient-success" class="col-xl-12 mb-5 mb-xl-0 pb-3 pb-3 pt-5 pt-md-8"></base-header>
      <div class="col-xl-6 mb-5 mb-xl-0">
        <div class="card">
          <div class="card-header border-0">
            <div class="row align-items-center">
              <div class="col">
                <h3 class="mb-0">누적수익률 순위</h3>
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
                <th>누적수익률</th>
              </template>

              <template slot-scope="{row}">
                <th scope="row">{{row.rank}}</th>
                <td>{{row.name}}</td>
                <td>{{row.momentum}}</td>
              </template>
            </base-table>
          </div>
        </div>
      </div>

      <div class="col-xl-6 mb-5 mb-xl-0">
        <div class="card">
          <div class="card-header border-0">
            <div class="row align-items-center">
              <div class="col">
                <h3 class="mb-0">위험조정수익률 순위</h3>
              </div>
              <div class="col text-right">
                <a href="#!" class="btn btn-sm btn-primary">전체보기</a>
              </div>
            </div>
          </div>

          <div class="table-responsive">
            <base-table thead-classes="thead-light" :data="tableData2">
              <template slot="columns">
                <th>순위</th>
                <th>기업명</th>
                <th>위험조정수익률</th>
              </template>

              <template slot-scope="{row}">
                <th scope="row">{{row.rank}}</th>
                <td>{{row.name}}</td>
                <td>{{row.riskmomentum}}</td>
              </template>
            </base-table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import http from "@/util/http-common";

export default {
  name: "momentum-table",
  data: () => {
    return {
      tableData: [],
      tableData2: [],
    };
  },
  methods: {
    momenlist: function () {
      const self = this;
      let idx = 1;
      http
        .get("/strategy/getmomen")
        .then(function (res) {
          self.tableData = [];
          for (let i of res.data) {
            self.tableData.push({
              rank: idx++,
              name: i.name,
              momentum: i.momentum,
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
      axios
        .get("http://localhost:8000/api/getriskmomen")
        .then(function (res) {
          self.tableData2 = [];
          for (let i of res.data) {
            self.tableData2.push({
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
  },
  created() {
    this.momenlist();
    this.riskmomenlist();
  },
};
</script>
<style>
</style>