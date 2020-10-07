<template>
  <div id="app" class="container">
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
    <v-btn outlined color="blue" @click="createArticle"> 등록 </v-btn>
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
          this.$router.push("/home/Community");
        })
        .catch((errors) => {
          console.log(errors.response.data);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
</style>