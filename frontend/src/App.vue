<template>
  <v-app>
    <Header></Header>
    <v-content>
      <router-view @submit-login-data="login"></router-view>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import store from "./store";
import axios from "axios";
const BACK_URL = "http://127.0.0.1:8000";

export default {
  name: "App",
  data() {
    return {
      isLogin: false,
    };
  },
  created() {
    if (this.$cookies.isKey("auth-token")) {
      this.isLogin = true;
    } else {
      this.isLogin = false;
    }
  },
  methods: {
    setCookie(key) {
      this.$cookies.set("auth-token", key);
      this.isLogin = true;
    },
    login(loginData) {
      axios
        .post(`${BACK_URL}/rest-auth/login/`, loginData)
        .then((response) => {
          // console.log(response)
          this.setCookie(response.data.key);
          this.$router.push("/");
        })
        .catch((error) => {
          console.log(error.response.data);
        });
    },
    logout() {
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`,
        },
      };
      axios
        .post(`${BACK_URL}/rest-auth/logout/`, null, requestHeader)
        .then(() => {
          this.$cookies.remove("auth-token");
          this.isLogin = false;
          this.$router.push("/");
        });
    },
  },
  mounted() {
    // Kakao.init("b9b23d9b337a41dca3e1632a4677e0af");
    // this.$store.commit("urlSave", "http://54.180.148.99:8000/");
  },
  components: {
    Header,
    Footer,
  },
  store,
};
</script>
