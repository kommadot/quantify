<template>
  <v-container
    id="icons"
    fluid
    tag="section"
    style="padding-left: 10%; padding-right: 10%"
  >
    <v-row justify no-gutters>
      <v-col>
        <p
          style="
            font-size: 30px;
            color: white;
            margin-top: auto;
            margin-bottom: auto;
          "
        >
          {{ title }}
        </p>
      </v-col>
    </v-row>
    <v-row>
      <v-spacer></v-spacer>
      <v-col style="padding-top: 0px; color: white" class="text-right">
        By {{ username }}
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <div
          style="background-color: gray; border-radius: 10px"
          class="tiptap-vuetify-editor__content mb-3"
          v-html="content"
        />
      </v-col>
    </v-row>
    <v-row class="mr-1">
      <v-col cols="9">
        <v-btn outlined color="blue" @click="listClick"> 목록 </v-btn>
      </v-col>
      <v-col
        class="text-right mr-0 pr-0"
        cols="1.5"
        v-if="userProfile.user_id == user_id"
      >
        <v-btn outlined color="blue" @click="deleteClick"> 삭제 </v-btn>
      </v-col>
      <v-col
        class="text-right mr-0 pr-0"
        cols="1.5"
        v-if="userProfile.user_id == user_id"
      >
        <v-btn outlined color="blue" @click="modifyClick"> 수정 </v-btn>
      </v-col>
    </v-row>
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
          this.title = data.data.title;
          this.content = data.data.content;
          this.user_id = data.data.user.user_id;
          this.username = data.data.user.username;
        });
    },
    listClick() {
      this.$router.push("/home/Community");
    },
    deleteClick(number) {
      http
        .delete(`/community/community/${this.$route.params.number}`, {
          headers: {
            Authorization: "JWT " + this.token,
          },
        })
        .then((response) => {
          this.$router.push("/home/Community");
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