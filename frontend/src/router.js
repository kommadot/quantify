import Vue from 'vue'
import Router from 'vue-router'
import Chart from '@/views/dashboard/component/Chart'
import CommunityWrite from "@/views/dashboard/component/CommunityWrite"
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
          path: 'strategy',
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
          path: "community",
          component: () => import("@/views/dashboard/component/Community")
        },
        {
          name: "CommunityWrite",
          path: "communityWrite",
          component: CommunityWrite
        },
        {
          name: "CommunityDetail",
          path: "detail/:number",
          component: () => import("@/views/dashboard/component/CommunityDetail")
        },
        {
          name: "CommunityModify",
          path: "modify/:number",
          component: () => import("@/views/dashboard/component/CommunityModify")
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