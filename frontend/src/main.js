/*!

=========================================================
* Vue Argon Dashboard - v1.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/argon-dashboard
* Copyright 2019 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/argon-dashboard/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import Vue from 'vue'
import App from './App.vue'
import router from './router'

import Vuex from 'vuex'
import store from "./store";
import './registerServiceWorker'
import ArgonDashboard from './plugins/argon-dashboard'
import GSignInButton from 'vue-google-signin-button'

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
