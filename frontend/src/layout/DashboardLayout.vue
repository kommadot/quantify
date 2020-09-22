<template>
  <div class="wrapper" :class="{ 'nav-open': $sidebar.showSidebar }">
    <side-bar :background-color="sidebarBackground" short-title="Quantify" title="Quantify">
      <template slot="links">
        <sidebar-item
          :link="{
            name: '주식추천필터',
            icon: 'ni ni-bold-down text-primary',
            path: '/mainfilter'
          }"
        />

        <sidebar-item :link="{name: '저변동성전략', icon: 'ni ni-sound-wave text-red', path: '/lowvar'}" />
        <sidebar-item
          :link="{name: '모멘텀전략', icon: 'ni ni-money-coins text-yellow', path: '/momentum'}"
        />
        <sidebar-item :link="{name: '밸류전략', icon: 'ni ni-building text-blue', path: '/value'}" />
        <sidebar-item
          :link="{name: '퀄리티전략', icon: 'ni ni-chart-bar-32 text-green', path: '/quality'}"
        />
      </template>
    </side-bar>
    <div class="main-content" :data="sidebarBackground">
      <dashboard-navbar></dashboard-navbar>
      <div @click="toggleSidebar">
        <fade-transition :duration="200" origin="center top" mode="out-in">
          <!-- your content here -->
          <router-view></router-view>
        </fade-transition>
        <content-footer v-if="!$route.meta.hideFooter"></content-footer>
      </div>
    </div>
  </div>
</template>
<script>
import DashboardNavbar from "./DashboardNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import { FadeTransition } from "vue2-transitions";

export default {
  components: {
    DashboardNavbar,
    ContentFooter,
    FadeTransition,
  },
  data() {
    return {
      sidebarBackground: "vue", //vue|blue|orange|green|red|primary
    };
  },
  methods: {
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    },
  },
};
</script>
<style lang="scss">
</style>
