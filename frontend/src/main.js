import Vue from "vue"
import App from "./App.vue"
import vuetify from "./plugins/vuetify"
import infiniteScroll from "vue-infinite-scroll"
import router from "./router"
import store from "./store"
import axios from 'axios'
import VueFullPage from 'vue-fullpage.js'
import VueCookies from 'vue-cookies'

Vue.config.productionTip = false
Vue.prototype.$http = axios
Vue.prototype.$EventBus = new Vue()
Vue.use(infiniteScroll)
Vue.use(VueFullPage)
Vue.use(VueCookies)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
