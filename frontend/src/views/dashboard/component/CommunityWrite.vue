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
    <v-btn @click="createArticle"> submit </v-btn>
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
        // Render in the Bubble menu
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
            // extension's options
            options: {
              levels: [1, 2, 3],
            },
          },
        ],
        // Render in the toolbar
        [
          Blockquote,
          {
            renderIn: "toolbar",
          },
        ],
        // You can use a short form, the default "renderIn" is "'toolbar'"
        History,
        Strike,
        Italic,
        ListItem, // if you need to use a list (BulletList, OrderedList)
        BulletList,
        OrderedList,
        [
          Heading,
          {
            // Options that fall into the tiptap's extension
            options: {
              levels: [1, 2, 3],
            },
          },
        ],
        Code,
        HorizontalRule,
        Paragraph,
        HardBreak, // line break on Shift + Ctrl + Enter
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