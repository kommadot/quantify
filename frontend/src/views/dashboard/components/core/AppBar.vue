<template>
  <v-app-bar id="app-bar" absolute app color="transparent" flat height="75">
    <v-btn class="mr-3" elevation="1" fab small @click="setDrawer(!drawer)">
      <v-icon v-if="value">mdi-view-quilt</v-icon>

      <v-icon v-else>mdi-dots-vertical</v-icon>
    </v-btn>

    <v-spacer />

    <!-- <v-autocomplete
      :items="items"
      v-model="item"
      :get-label="getLabel"
      :component-item="template"
      @update-items="updateItems"
    ></v-autocomplete>-->
    <v-text-field
      :label="$t('기업 검색')"
      color="primary"
      v-model="search"
      hide-details
      style="max-width: 500px;"
    >
      <template v-if="$vuetify.breakpoint.mdAndUp" v-slot:append-outer>
        <v-btn class="mt-n2" elevation="1" fab small>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </template>
    </v-text-field>

    <div class="mx-3" />

    <!-- login -->
    <v-btn v-if="!this.isLoggedIn" class="ml-2" min-width="0" text @click="login" dark>
      <!-- <v-icon>mdi-account</v-icon> -->
      login
    </v-btn>
    <login-form :dialog="dialog" @closeForm="dialog=false" />

    <!-- profile -->
    <v-btn v-if="this.isLoggedIn" class="ml-2" min-width="0" text @click="login" dark>
      <!-- <v-icon>mdi-account</v-icon> -->
      profile
    </v-btn>
    <login-form :dialog="dialog" @closeForm="dialog=false" />

    <!-- logout -->
    <v-btn v-if="this.isLoggedIn" class="ml-2" min-width="0" text @click="logout2" dark>
      <!-- <v-icon>mdi-account-off</v-icon> -->
      logout
    </v-btn>
  </v-app-bar>
</template>

<script>
import LoginForm from "@/components/base/LoginForm.vue";
import { mapState, mapMutations, mapGetters, mapActions } from "vuex";
import UserApi from "../../../../api/CompanyApi";

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
      keyword: "",
      users: [],
      items: [],
      active: [],
      temp: [],
      open: [1, 2],
      search: null,
    };
  },
  created() {
    let data = {
      token: localStorage.getItem("token"),
    };

    CompanyApi.findComAll(
      data,
      (res) => {
        this.temp = res.data;
        for (var i = 0; i < this.temp.length; i++) {
          this.items.push({
            id: i + 1,
            name: this.temp[i].userId,
          });
        }
      },
      (error) => {
        alert(error);
      }
    );
  },
  computed: {
    ...mapState(["drawer"]),
    ...mapGetters(["isLoggedIn"]),
    filter() {
      return this.caseSensitive
        ? (item, search, textKey) => item[textKey].indexOf(search) > -1
        : undefined;
    },
    selected() {
      // 여기 눌리면 오는 곳
      return "안녕하세요";
    },
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
    // getLabel(item) {
    //   return item.name;
    // },
    // updateItems(text) {
    //   yourGetItemsMethod(text).then((response) => {
    //     this.items = response;
    //   });
    // },
    onChange(selection) {
      var userId = null;

      for (var i = 0; i < this.items.length; i++) {
        if (this.items[i].id === selection[0]) {
          userId = this.items[i].name;
          break;
        }
      }
      this.$router.push("/ItemTemplate/");
    },
  },
  watch: {
    keyword: function (v) {
      if (v.length > 0) {
        CompanyApi.findComBykeyword(
          v,
          (response) => {
            this.users = response.data;
          },
          (error) => {
            alert("기업 목록 조회에 실패했습니다.");
          }
        );
      } else {
        this.users = [];
      }
    },
    selected: "randomAvatar",
  },
};
</script>
