import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: sessionStorage.getItem('token'),
  },
  getters: {

  },
  mutations: {
    setToken(state, payload) {
      state.token = payload;
    },
    logout(state) {
      state.token = ''
      sessionStorage.clear()
    }
  },
  actions: {
    getToken(context, payload) {
      context.commit("setToken", payload);
    },
    logout(context) {
      context.commit("logout");
    }
  },
  modules: {},
});
