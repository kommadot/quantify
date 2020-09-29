<template>
  <v-container id="icons" fluid tag="section">
    <base-material-card color="success" dark>
      <template v-slot:heading>
        <div class="display-2 font-weight-light">{{ title }}</div>
      </template>
      <v-container>
        <div
          style="background-color: gray"
          class="tiptap-vuetify-editor__content mb-3"
          v-html="content"
        />
        <v-row class="mr-1">
          <v-col cols="10">
            <v-btn outlined color="primary" @click="listClick"> 목록 </v-btn>
          </v-col>
          <v-col cols="1" v-if="userProfile.user_id == user_id">
            <v-btn outlined color="primary" @click="deleteClick"> 삭제 </v-btn>
          </v-col>
          <v-col cols="1" v-if="userProfile.user_id == user_id">
            <v-btn outlined color="primary" @click="modifyClick"> 수정 </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </base-material-card>
  </v-container>
</template>

<script>
import http from "@/util/http-common";
import { mapState } from "vuex";

export default {
  name: "CommunityDetail",
  data() {
    return {
      title: "",
      content: "",
      username: "",
      user_id: "",
    };
  },
  created() {
    this.articleDetail();
  },
  computed: {
    ...mapState(["token", "userProfile"]),
  },
  methods: {
    articleDetail(number) {
      http
        .get(`/community/community/${this.$route.params.number}`)
        .then((data) => {
          console.log(data);
          this.title = data.data.title;
          this.content = data.data.content;
          this.user_id = data.data.user.user_id;
          this.username = data.data.username;
        });
    },
    listClick() {
      this.$router.push("/Community");
    },
    deleteClick(number) {
      http
        .delete(`/community/community/${this.$route.params.number}`, {
          headers: {
            Authorization: "JWT " + this.token,
          },
        })
        .then((response) => {
          console.log(response);
          this.$router.push("/Community");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    modifyClick() {
      this.$router.push({
        name: "CommunityModify",
        params: {
          number: this.$route.params.number,
        },
      });
    },
  },
};
</script>

<style>
</style>