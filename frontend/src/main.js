import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/base'
import './plugins/chartist'
import './plugins/vee-validate'
import vuetify from './plugins/vuetify'
import i18n from './i18n'
import GSignInButton from 'vue-google-signin-button'
Vue.config.productionTip = false
Vue.use(Vuex)
Vue.use(GSignInButton)
new Vue({
  created() {
    Kakao.init('e4263be1d8a351bad145638cb6ade0bd'),
    this.$store.dispatch("getCompany")
  },
  router,
  store,
  vuetify,
  i18n,
  render: h => h(App),
}).$mount('#app')
