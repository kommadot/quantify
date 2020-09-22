import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: sessionStorage.getItem('token'),
    userProfile:sessionStorage.getItem("userProfile")?JSON.parse(sessionStorage.getItem("userProfile")):[],
    barColor: 'rgba(0, 0, 0, .8), rgba(0, 0, 0, .8)',
    barImage: 'https://demos.creative-tim.com/material-dashboard/assets/img/sidebar-1.jpg',
    drawer: null,
    },
  getters: {
    isLoggedIn(state){
      if(state.userProfile!=null && state.userProfile && state.userProfile!="" && state.userProfile!="null"){
        return true
      }
      return false
    }
  },
  mutations: {
    setToken(state, payload) {
      state.token = payload;
      sessionStorage.setItem("token",payload)
    },
    logout(state) {
      state.token = ''
      state.userProfile = []
      sessionStorage.clear()
    },
    setUserProfile(state,payload){
      state.userProfile=payload
      sessionStorage.setItem("userProfile",JSON.stringify(payload))
    },
    SET_BAR_IMAGE (state, payload) {
        state.barImage = payload
      },
      SET_DRAWER (state, payload) {
        state.drawer = payload
      },
  },
  actions: {
    setToken(context, payload) {
      context.commit("setToken", payload);
    },
    logout(context) {
      context.commit("logout");
    },
    setUserProfile(context,payload){
      context.commit("setUserProfile",payload)
    }
  },
  modules: {},
});
