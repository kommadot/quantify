import Vue from 'vue'
import App from './App.vue'
import router from './router'

import Vuex from 'vuex'
import store from "./store";
import './registerServiceWorker'
import ArgonDashboard from './plugins/argon-dashboard'
import GSignInButton from 'vue-google-signin-button'

// bootstrap
import { BootstrapVue } from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
Vue.use(BootstrapVue);

Vue.config.productionTip = false

Vue.use(GSignInButton)
Vue.use(Vuex)

Vue.use(ArgonDashboard)
new Vue({
  created() {
    Kakao.init('e4263be1d8a351bad145638cb6ade0bd')
  },
  router,
  store,
  render: h => h(App),

}).$mount('#app')
