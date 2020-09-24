<template>
  <v-app-bar id="app-bar" absolute app color="transparent" flat height="75">
    <!-- <v-btn class="mr-3" elevation="1" fab small @click="setDrawer(!drawer)">
      <v-icon v-if="value">mdi-view-quilt</v-icon>

      <v-icon v-else>mdi-dots-vertical</v-icon>
    </v-btn> -->

    <v-spacer />

    <v-text-field
      :label="$t('search')"
      hide-details
      style="max-width: 500px"
      dark
      v-model="searchInput"
    >
      <template v-if="$vuetify.breakpoint.mdAndUp" v-slot:append-outer>
        <v-btn class="mt-n2" elevation="1" fab small @click="searchStock">
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </template>
    </v-text-field>

    <div class="mx-3" />

    <!-- login -->
    <v-btn
      v-if="!this.isLoggedIn"
      class="ml-2"
      min-width="0"
      text
      @click="login"
      dark
    >
      <!-- <v-icon>mdi-account</v-icon> -->
      login
    </v-btn>
    <login-form :dialog="dialog" @closeForm="dialog = false" />

    <!-- profile -->
    <v-btn
      v-if="this.isLoggedIn"
      class="ml-2"
      min-width="0"
      text
      @click="login"
      dark
    >
      <!-- <v-icon>mdi-account</v-icon> -->
      profile
    </v-btn>
    <login-form :dialog="dialog" @closeForm="dialog = false" />

    <!-- logout -->
    <v-btn
      v-if="this.isLoggedIn"
      class="ml-2"
      min-width="0"
      text
      @click="logout2"
      dark
    >
      <!-- <v-icon>mdi-account-off</v-icon> -->
      logout
    </v-btn>
  </v-app-bar>
</template>

<script>
import LoginForm from "@/components/base/LoginForm.vue";
import { mapState, mapMutations, mapGetters, mapActions } from "vuex";

export default {
  name: "DashboardCoreAppBar",
  components: {
    LoginForm,
  },
  props: {
    value: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      dialog: false,
      login_profile: "login",
      searchInput: "",
    };
  },
  computed: {
    ...mapState(["drawer"]),
    ...mapGetters(["isLoggedIn"]),
  },

  methods: {
    ...mapMutations({
      setDrawer: "SET_DRAWER",
    }),
    login() {
      if (this.isLoggedIn) {
        this.$router.push("/pages/user");
        this.login_profile = "profile";
      } else {
        this.dialog = true;
      }
    },
    ...mapActions(["logout"]),
    logout2() {
      if (this.isLoggedIn) {
        this.logout();
        this.login_profile = "login";
        this.$router.push("/");
      }
    },
    searchStock() {
      this.stocks[this.searchInput];
      this.$router.push({
        name: "chart",
        params: { code: this.stocks[this.searchInput] },
      });
    },
  },
};
</script>
