<template>
  <div id="app">
    <v-text-field
      :counter="50"
      label="제목"
      name="title"
      required
      v-model="title"
      maxlength="50"
      dark
    ></v-text-field>
    <tiptap-vuetify v-model="content" :extensions="extensions" />
    <v-btn color="blue" @click="createArticle"> submit </v-btn>
  </div>
</template>

<script>
import http from "@/util/http-common";
import { mapState } from "vuex";
import {
  TiptapVuetify,
  Heading,
  Bold,
  Italic,
  Strike,
  Underline,
  Code,
  Paragraph,
  BulletList,
  OrderedList,
  ListItem,
  Link,
  Blockquote,
  HardBreak,
  HorizontalRule,
  History,
} from "tiptap-vuetify";
export default {
  name: "CommunityWrite",
  components: { TiptapVuetify },
  data() {
    return {
      title: "",
      extensions: [
        [
          Link,
          {
            renderIn: "bubbleMenu",
          },
        ],
        [
          Underline,
          {
            renderIn: "bubbleMenu",
          },
        ],
        [
          Strike,
          {
            renderIn: "bubbleMenu",
          },
        ],
        [
          Bold,
          {
            renderIn: "bubbleMenu",
            options: {
              levels: [1, 2, 3],
            },
          },
        ],
        [
          Blockquote,
          {
            renderIn: "toolbar",
          },
        ],
        History,
        Strike,
        Italic,
        ListItem,
        BulletList,
        OrderedList,
        [
          Heading,
          {
            options: {
              levels: [1, 2, 3],
            },
          },
        ],
        Code,
        HorizontalRule,
        Paragraph,
        HardBreak,
      ],
      content: "",
    };
  },
  computed: {
    ...mapState(["token"]),
  },
  created() {
    this.articleDetail();
  },
  methods: {
    createArticle() {
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
          this.$router.push("/home/Community");
        })
        .catch((errors) => {
          console.log(errors.response.data);
        });
    },
    articleDetail(number) {
      http
        .get(`/community/community/${this.$route.params.number}`)
        .then((data) => {
          console.log(data);
          this.title = data.data.title;
          this.content = data.data.content;
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
          console.log(response);
          this.$router.push("/home/Community");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    modifyClick(item) {
      this.$router.push({
        name: "CommunityModify",
        params: {
          number: item.number,
        },
      });
    },
  },
};
</script>

<style lang="scss" scoped>
</style>