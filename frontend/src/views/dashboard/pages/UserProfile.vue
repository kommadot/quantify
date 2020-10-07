<template>
  <v-container id="user-profile" fluid tag="section">
    <v-row justify="center">
      <v-col cols="12">
        <base-material-card color="#1F4E70">
          <template v-slot:heading>
            <div class="display-2 font-weight-light">Profile</div>
          </template>

          <v-form>
            <v-container class="mt-4">
              <v-row>
                <v-col cols="12" md="6">
                  <v-text-field
                    class="purple-input"
                    label="User Name"
                    v-model="userProfile.username"
                    color="#1F4E70"
                    readonly
                  />
                </v-col>
                <v-col cols="12" md="6">
                  <v-text-field
                    class="purple-input"
                    label="Login Platform"
                    v-model="userProfile.platform"
                    readonly
                    color="#1F4E70"
                  />
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    class="purple-input"
                    label="Budget"
                    v-model="budget"
                    color="#1F4E70"
                    readonly
                  />
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import http from "@/util/http-common";
import { mapState, mapActions } from "vuex";

export default {
  data() {
    return {
      userProfile: sessionStorage.getItem("userProfile")
        ? JSON.parse(sessionStorage.getItem("userProfile"))
        : [],
      budget: 0,
    };
  },
  created() {
    this.getUserBudget();
  },
  methods: {
    getUserBudget() {
      http
        .get("/simulations/budget", {
          headers: {
            Authorization: "JWT " + this.$store.state.token,
          },
        })
        .then((res) => {
          this.budget = res.data;
        });
    },
  },
};
</script>
