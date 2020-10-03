<template>
  <v-app>
    <dashboard-core-app-bar />
    <dashboard-core-drawer />
    <dashboard-core-view />
  </v-app>
</template>

<script>
import BeforeLogin from "@/views/dashboard/BeforeLogin.vue";

export default {
  name: "DashboardIndex",

  components: {
    DashboardCoreAppBar: () => import("./components/core/AppBar"),
    DashboardCoreDrawer: () => import("./components/core/Drawer"),
    DashboardCoreView: () => import("./components/core/View"),
  },

  data: () => ({
    expandOnHover: false,
  }),
};
</script>
