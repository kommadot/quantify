import Vue from "vue";
import Vuex from "vuex";
import http from "@/util/http-common";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: sessionStorage.getItem('token'),
    userProfile: sessionStorage.getItem("userProfile") ? JSON.parse(sessionStorage.getItem("userProfile")) : [],
    barColor: 'rgba(0, 0, 0, .8), rgba(0, 0, 0, .8)',
    barImage: 'https://demos.creative-tim.com/material-dashboard/assets/img/sidebar-1.jpg',
    drawer: null,

    simulationlist: [],
    simulationdetail: {},
    simulationbreakdownlist: [],
    simulationbreakdowndetail: {},
  },
  getters: {
    isLoggedIn(state) {
      if (state.userProfile != null && state.userProfile && state.userProfile != "" && state.userProfile != "null") {
        return true
      }
      return false
    },

    simulationlist(state) {
      return state.simulationlist
    },
    simulationdetail(state) {
      return state.simulationdetail
    },
    simulationbreakdowndetail(state) {
      return state.simulationbreakdowndetail
    },
    simulationbreakdowndetail(state) {
      return state.simulationbreakdowndetail
    },
  },
  mutations: {
    setToken(state, payload) {
      state.token = payload;
      sessionStorage.setItem("token", payload)
    },
    logout(state) {
      state.token = ''
      state.userProfile = []
      sessionStorage.clear()
    },
    setUserProfile(state, payload) {
      state.userProfile = payload
      sessionStorage.setItem("userProfile", JSON.stringify(payload))
    },
    SET_BAR_IMAGE(state, payload) {
      state.barImage = payload
    },
    SET_DRAWER(state, payload) {
      state.drawer = payload
    },

    setSimulationList(state, payload) {
      state.simulationlist = payload
    },

    setSimulationDetail(state, payload) {
      state.simulationdetail = payload
    },

    setSimulationBreakdownList(state, payload) {
      state.simulationbreakdownlist = payload
    },

    setSimulationBreakdownDetail(state, payload) {
      state.simulationbreakdowndetail = payload
    },

  },
  actions: {
    setToken(context, payload) {
      context.commit("setToken", payload);
    },
    logout(context) {
      context.commit("logout");
    },
    setUserProfile(context, payload) {
      context.commit("setUserProfile", payload)
    },

    getSimulationList(context) {
      console.log(context.state.token)
      http
        .get('/simulations/simulation', {
          headers: {
            Authorization: "JWT " + context.state.token
          },
        })
        .then(({ data }) => {
          context.commit("setSimulationList", data);
        });
    },

    getSimulationDetail(context, oid) {
      http
        .get(`/simulations/${oid}`, {
          headers: {
            Authorization: "JWT " + context.state.token
          },
        })
        .then(({ data }) => {
          context.commit("setSimulationDetail", data);
        });
    },
    deleteSimulationDetail() {
      http
        .delete('/simulations/oid', {
          headers: {
            Authorization: "JWT " + context.state.token
          },
        })
        .then();
    },

    getSimulationBreakdownList(context) {
      http
        .get('/simulations/simulationbreakdown', {
          headers: {
            Authorization: "JWT " + context.state.token
          },
        })
        .then(({ data }) => {
          context.commit("setSimulationBreakdownList", data);
        });
    },

    getSimulationBreakdownDetail(context) {
      http
        .get('/simulations/oid', {
          headers: {
            Authorization: "JWT " + context.state.token
          },
        })
        .then(({ data }) => {
          context.commit("setSimulationBreakdownDetail", data);
        });
    },
  },
  modules: {},
});