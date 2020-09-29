<template>
  <v-form>
    <v-container>
      <v-row> 제목 </v-row>
      <v-row> {{ title }} </v-row>
      <div style="background-color:gray" class="tiptap-vuetify-editor__content" v-html="content"/>
      <v-row>
        <v-btn block outlined color="blue" @click="listClick"> 목록 </v-btn>
      </v-row>
      <v-row v-if="userProfile.user_id==user_id">
        <v-col>

        <v-btn @click="deleteClick"> 삭제 </v-btn>
        </v-col>
        <v-col>
          <v-btn @click="modifyClick"> 수정 </v-btn>
        </v-col>
      </v-row>

    </v-container>
    
  </v-form>
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
      user_id:"",
    };
  },
  created() {
    this.articleDetail();
  },
  computed: {
    ...mapState(["token",'userProfile']),
  },
  methods: {
    articleDetail(number) {
      http
        .get(`/community/community/${this.$route.params.number}`
        )
        .then((data) => {
          console.log(data);
          this.title = data.data.title;
          this.content = data.data.content;
          this.user_id = data.data.user.user_id
          this.username = data.data.username
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