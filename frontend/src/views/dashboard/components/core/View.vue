<template>
  <v-content>
    <router-view />

    <!-- <dashboard-core-footer style="position:absolute;bottom:10px;"/> -->
  </v-content>
</template>

<script>
  export default {
    name: 'DashboardCoreView',

    components: {
      DashboardCoreFooter: () => import('./Footer'),
    },
  }
</script>
