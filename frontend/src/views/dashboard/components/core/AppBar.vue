<template>
  <v-app-bar id="app-bar" absolute app color="transparent" flat height="75">
    <!-- <v-btn class="mr-3" elevation="1" fab small @click="setDrawer(!drawer)">
      <v-icon v-if="value">mdi-view-quilt</v-icon>

      <v-icon v-else>mdi-dots-vertical</v-icon>
    </v-btn> -->

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
        <v-btn class="mt-n2" elevation="1" fab small @click="searchStock">
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </template>
    </v-text-field> -->
        <v-autocomplete
          v-model="searchModel"
          :items="items"
          :search-input.sync="search"

          hide-no-data
          hide-selected
          item-text="name"
          dark
          placeholder="종목 입력"
          prepend-icon="mdi-chart-line-variant"
          return-object
          
          
        ></v-autocomplete>
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
            searchModel:"",
      search:"",
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
    ...mapState(["drawer","company"]),
    ...mapGetters(["isLoggedIn"]),
    items () {
      return this.company.map(entry => {
        const Description = entry.name.length > this.descriptionLimit
          ? entry.name.slice(0, this.descriptionLimit) + '...'
          : entry.name

        return Object.assign({}, entry)
      })
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

  },
  watch:{
    searchModel(value){
      if(typeof(value)=="object"){
        this.$router.push({name:"Chart",params:{code:value.code}})
      }
    },

  }
};
</script>
