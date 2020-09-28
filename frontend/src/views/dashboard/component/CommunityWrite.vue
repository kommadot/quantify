<template>
  <v-form>
    <v-container>
      <v-row>
        <v-text-field
          :counter="50"
          label="제목"
          name="title"
          required
          v-model="title"
          maxlength="50"
          dark
        ></v-text-field>
      </v-row>
      <v-row>
        <v-textarea
          filled
          name="content"
          hint="내용을 입력해주세요."
          v-model="content"
          :counter="1000"
          maxlength="1000"
          dark
        ></v-textarea>
      </v-row>
      <v-row>
        <v-btn block outlined color="blue" @click="createArticle"> 등록 </v-btn>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
import http from "@/util/http-common";
import { mapState } from "vuex";

export default {
  name: "CommunityWrite",

  data() {
    return {
      title: "",
      content: "",
    };
  },
  computed: {
    ...mapState(["token"]),
  },
  methods: {
    createArticle() {
      const requestHeaders = {
        headers: {
          Authorization: "JWT " + this.token,
        },
      };
      http
        .post(
          "/community/community",
          { title: this.title, content: this.content },
          requestHeaders
        )
        .then(() => {
          this.$router.push("/Community");
        })
        .catch((errors) => {
          console.log(errors.response.data);
        });
    },
  },
};
</script>

<style>
</style>