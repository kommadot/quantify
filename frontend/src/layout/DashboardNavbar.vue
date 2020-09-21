<template>
  <base-nav class="navbar-top navbar-dark" id="navbar-main" :show-toggle-button="false" expand>
    <form class="navbar-search navbar-search-dark form-inline mr-3 d-none d-md-flex ml-lg-auto">
      <div class="form-group mb-0">
        <base-input
          placeholder="Search"
          class="input-group-alternative"
          alternative
          addon-right-icon="fas fa-search"
        ></base-input>
      </div>
    </form>
    <ul class="navbar-nav align-items-center d-none d-md-flex">
      <!-- Navbar items -->
      <!-- 로그인 안했을 때 -->
      <!-- <ul class="navbar-nav ml-auto"> -->
      <ul class="navbar-nav ml-auto" v-if="!token">
        <li class="nav-item">
          <router-link class="nav-link nav-link-icon" to="/register">
            <i class="ni ni-circle-08"></i>
            <span class="nav-link-inner--text">회원가입</span>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link nav-link-icon" to="/login">
            <i class="ni ni-key-25"></i>
            <span class="nav-link-inner--text">로그인</span>
          </router-link>
        </li>
      </ul>
      <!-- 로그인 했을 때 -->
      <!-- <ul class="navbar-nav ml-auto"> -->
      <ul class="navbar-nav ml-auto" v-if="token">
        <li class="nav-item">
          <i class="ni ni-key-25"></i>
          <span class="nav-link-inner--text" @click="logout">로그아웃</span>
        </li>
      </ul>
    </ul>
  </base-nav>
</template>
<script>
import { mapActions, mapState } from "vuex";

export default {
  data() {
    return {
      activeNotifications: false,
      showMenu: false,
      searchQuery: "",
    };
  },
  methods: {
    toggleSidebar() {
      this.$sidebar.displaySidebar(!this.$sidebar.showSidebar);
    },
    hideSidebar() {
      this.$sidebar.displaySidebar(false);
    },
    toggleMenu() {
      this.showMenu = !this.showMenu;
    },
    ...mapActions(["logout"]),
  },
  computed: {
    ...mapState(["token"]),
  },
};
</script>
