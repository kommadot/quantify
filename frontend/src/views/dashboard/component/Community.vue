<template>
  <v-container id="icons" fluid tag="section">
    <base-material-card color="success" dark>
      <template v-slot:heading>
        <div class="display-2 font-weight-light">커뮤니티</div>
      </template>
      <br />
      <v-data-table
        :headers="headers"
        :items="desserts"
        :items-per-page="5"
        class="elevation-1"
        @click:row="rowClick"
        dark
      >
      </v-data-table>
      <br />
      <v-row>
        <v-btn outlined color="blue" @click="writeClick"> 작성 </v-btn>
      </v-row>
    </base-material-card>
  </v-container>
</template>
<script>
import http from "@/util/http-common";

export default {
  name: "Community",
  data() {
    return {
      headers: [
        {
          text: "Number",
          align: "left",
          sortable: false,
          value: "number",
        },
        { text: "Title", value: "title" },
        { text: "Username", value: "username" },
        { text: "Reg Date", value: "regDt" },
      ],
      desserts: [],
    };
  },
  created() {
    this.getCommunity();
  },
  methods: {
    getCommunity() {
      http
        .get("/community/community")
        .then((response) => {
          console.log(response);
          response.data.forEach((res) => {
            const r = new Date(res.created_at);
            const reg =
              "" +
              (r.getMonth() + 1) +
              "월 " +
              r.getDate() +
              "일 " +
              r.getHours() +
              ":" +
              r.getMinutes();
            this.desserts.push({
              number: res.id,
              username: res.user.username,
              title: res.title,
              regDt: reg,
            });
          });

          console.log(this.desserts);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    writeClick() {
      this.$router.push("/CommunityWrite");
    },
    rowClick(item) {
      this.$router.push({
        name: "CommunityDetail",
        params: { number: item.number },
      });
    },
  },
};
</script>
