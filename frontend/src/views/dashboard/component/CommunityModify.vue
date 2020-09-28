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
        <v-btn block outlined color="blue" @click="modifyArticle"> 수정 </v-btn>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
import http from "@/util/http-common";
import { mapState } from "vuex";

export default {
  name: "CommunityModify",
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
    modifyArticle(number) {
      const requestHeaders = {
        headers: {
          Authorization: "JWT " + this.token,
        },
      };
      http
        .put(
          `/community/community/${this.$route.params.number}`,
          { title: this.title, content: this.content },
          requestHeaders
        )
        .then(() => {
          this.$router.push(`/detail/${this.$route.params.number}`);
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