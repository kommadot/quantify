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
                <h3 class="mb-0">밸류지수 순위</h3>
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
                <th>PER</th>
                <th>PBR</th>
                <th>PSR</th>
                <th>종합순위지표</th>
              </template>

              <template slot-scope="{row}">
                <th scope="row">{{row.rank}}</th>
                <td>{{row.name}}</td>
                <td>{{row.per}}</td>
                <td>{{row.pbr}}</td>
                <td>{{row.psr}}</td>
                <td>{{row.score}}</td>
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
  name: "value-table",
  data: () => {
    return {
      tableData: [],
    };
  },
  methods: {
    valuelist: function () {
      const self = this;
      let idx = 1;
      http
        .get("/strategy/getvalue")
        .then(function (res) {
          self.tableData = [];
          for (let i of res.data) {
            self.tableData.push({
              rank: idx++,
              name: i.name,
              per: i.per,
              pbr: i.pbr,
              psr: i.psr,
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
    this.valuelist();
  },
};
</script>
<style>
</style>