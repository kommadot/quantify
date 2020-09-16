<template>
  <div class="row justify-content-center">
    <div class="col-lg-5 col-md-7">
      <div class="card bg-secondary shadow border-0">
        <div class="card-header bg-transparent pb-5">
          <div class="text-muted text-center mt-2 mb-3">
            <small>Sign in with</small>
          </div>
          <div class="btn-wrapper text-center">
            <a @click="kakaologin" class="btn btn-neutral btn-icon">
              <span class="btn-inner--icon">
                <img src="img/icons/common/github.svg" />
              </span>
              <span class="btn-inner--text">Github</span>
            </a>
            <div class="btn btn-neutral btn-icon">
              <span class="btn-inner--icon">
                <img src="img/icons/common/google.svg" />
              </span>
              <!-- <span class="btn-inner--text">Google</span> -->
              <g-signin-button
                v-if="isEmpty(user)"
                :params="googleSignInParams"
                @success="onGoogleSignInSuccess"
                @error="onGoogleSignInError"
              >
                <span class="btn-inner--text">Google</span>
              </g-signin-button>
            </div>
          </div>
        </div>
        <!-- <div class="card-body px-lg-5 py-lg-5">
                        <div class="text-center text-muted mb-4">
                            <small>Or sign in with credentials</small>
                        </div>
                        <form role="form">
                            <base-input class="input-group-alternative mb-3"
                                        placeholder="Email"
                                        addon-left-icon="ni ni-email-83"
                                        v-model="model.email">
                            </base-input>

                            <base-input class="input-group-alternative"
                                        placeholder="Password"
                                        type="password"
                                        addon-left-icon="ni ni-lock-circle-open"
                                        v-model="model.password">
                            </base-input>

                            <base-checkbox class="custom-control-alternative">
                                <span class="text-muted">Remember me</span>
                            </base-checkbox>
                            <div class="text-center">
                                <base-button type="primary" class="my-4">Sign in</base-button>
                            </div>
                        </form>
        </div>-->
      </div>
      <!-- <div class="row mt-3">
                    <div class="col-6">
                        <a href="#" class="text-light"><small>Forgot password?</small></a>
                    </div>
                    <div class="col-6 text-right">
                        <router-link to="/register" class="text-light"><small>Create new account</small></router-link>
                    </div>
      </div>-->
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "login",
  components: {},
  data() {
    return {
      user: {},
      googleSignInParams: {
        client_id:
          "439204260274-d7c8mbutib6d444ekiopiu54jh1ps02b.apps.googleusercontent.com",
      },
    };
  },
  methods: {
    onGoogleSignInSuccess(resp) {
      const token = resp.getAuthResponse(true).access_token;
      axios
        .post("http://localhost:8000/auth/google", {
          access_token: token,
        })
        .then((resp) => {
          console.log(resp);
          // this.user = resp.data.user;
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    onGoogleSignInError(error) {
      console.log("OH NOES", error);
    },
    isEmpty(obj) {
      return Object.keys(obj).length === 0;
    },
    kakaologin() {
      Kakao.Auth.login({
        success: function (res) {
          console.log(res);
          const token = res.access_token;
          axios
            .post("http://localhost:8000/auth/kakao", {
              access_token: token,
            })
            .then((res) => {
              console.log(res);
              // this.user = resp.data.user;
            })
            .catch((err) => {
              console.log(err.response);
            });
        },
        fail: function (error) {
          console.log(error);
        },
      });
    },
  },
};
</script>
<style>
</style>
