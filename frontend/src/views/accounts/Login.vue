<template>
  <div>
    <h1>Login</h1>username :
    <input type="text" v-model="loginData.username" />
    <br />password :
    <input type="password" v-model="loginData.password" />
    <br />
    <button @click="login">Login</button>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      loginData: {
        username: null,
        password: null,
      },
    };
  },
  created() {
    if (this.$cookies.isKey("auth-token")) {
      this.$router.push("/");
    }
  },
  methods: {
    login() {
      this.$emit("submit-login-data", this.loginData);
    },
  },
};
</script>