<template>
  <div class="row justify-content-center">
    <div class="col-lg-5 col-md-7">
      <div class="card bg-secondary shadow border-0">
        <div class="card-header bg-transparent p-5" style="width: auto; height: 400px;">
          <div class="text-muted text-center mt-2 mb-3">
            <p class="mb-5" style="font-size: 150%;">Sign in with</p>
          </div>

          <!-- google login -->
          <div class="btn-wrapper text-center">
            <g-signin-button
              v-if="isEmpty(user)"
              :params="googleSignInParams"
              @success="onGoogleSignInSuccess"
              @error="onGoogleSignInError"
              style="cursor: pointer;"
            >
              <img src="@/assets/imgs/btn_google_signin_light_normal_web.png" />
            </g-signin-button>
          </div>
          <br />

          <!-- kakao login -->
          <div class="btn-wrapper text-center">
            <a @click="kakaologin" style="cursor: pointer;">
              <img src="@/assets/imgs/kakao_login_medium_narrow.png" style="width: 191px;" />
            </a>
          </div>
          <br />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapActions } from "vuex";

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
      jwt_token: "",
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
          const config = {
            "Content-Type": "application/json",
          };
          axios
            .post(
              "http://localhost:8000/login/",
              {
                username: resp.data.username,
                password: resp.data.social_id,
              },
              config
            )
            .then((json) => {
              // 발급 완료 되었다면 해당 토큰을 클라이언트 Session Storage에 저장
              // token = json.data.token;
              console.log(`token: ${json.data.token}`);
              sessionStorage.setItem("token", JSON.stringify(json.data.token));
              this.jwt_token = json.data.token;
            })
            .catch((error) => {
              console.log(error);
              window.gapi && window.gapi.auth2.getAuthInstance().signOut();
            });
          this.$router.push("/");
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
      const self = this;
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
              const config = {
                "Content-Type": "application/json",
              };
              axios
                .post(
                  "http://localhost:8000/login/",
                  {
                    username: res.data.username,
                    password: res.data.social_id,
                  },
                  config
                )
                .then((json) => {
                  // 발급 완료 되었다면 해당 토큰을 클라이언트 Local Storage에 저장
                  // token = json.data.token;
                  console.log(`token: ${json.data.token}`);
                  sessionStorage.setItem(
                    "token",
                    JSON.stringify(json.data.token)
                  );
                  this.getToken(json.data.token);
                })
                .catch((error) => {
                  console.log(error);
                  window.gapi && window.gapi.auth2.getAuthInstance().signOut();
                });
              self.$router.push("/");
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
    ...mapActions(["getToken"]),
  },
};
</script>
<style>
.g-signin-button {
  display: inline-block;
  margin-left: 10px;
  color: black;
}
</style>
