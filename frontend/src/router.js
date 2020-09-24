import Vue from 'vue'
import Router from 'vue-router'
import Chart from '@/views/dashboard/component/Chart'
Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      component: () => import("@/views/dashboard/Index"),
      children: [
        // Main
        {
          name: 'Main',
          path: '',
          component: () => import('@/views/dashboard/Main'),
        },
        // Dashboard
        {
          name: 'Strategy',
          path: 'Strategy',
          component: () => import('@/views/dashboard/Strategy'),
        },
        // Pages
        {
          name: "User Profile",
          path: "pages/user",
          component: () => import("@/views/dashboard/pages/UserProfile")
        },
        {
          name: "Notifications",
          path: "components/notifications",
          component: () => import("@/views/dashboard/component/Notifications")
        },
        {
          name: "Community",
          path: "Community",
          component: () => import("@/views/dashboard/component/Community")
        },
        {
          name: "BackTest",
          path: "BackTest",
          component: () => import("@/views/dashboard/component/BackTest")
        },
        // Tables
        {
          name: "Simulation",
          path: "Simulation",
          component: () => import("@/views/dashboard/tables/Simulation")
        },
        {
          name: "Stock Data",
          path: "components/stocks",
          component: () => import("@/views/Stock")
        },
        // Maps
        {
          name: "Chart",
          path: 'chart/:code',
          component: Chart,
        }
        // Upgrade
      ]
    }
  ]
});