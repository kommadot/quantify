import Vue from 'vue'
import Router from 'vue-router'
import DashboardLayout from '@/layout/DashboardLayout'
import AuthLayout from '@/layout/AuthLayout'
Vue.use(Router)

export default new Router({
  linkExactActiveClass: 'active',
  routes: [
    {
      path: '/',
      redirect: 'mainfilter',
      component: DashboardLayout,
      children: [
        {
          path: '/dashboard',
          name: 'dashboard',
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import(/* webpackChunkName: "demo" */ './views/Dashboard.vue')
        },
        {
          path: '/mainfilter',
          name: 'mainfilter',
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import(/* webpackChunkName: "demo" */ './views/Mainfilter.vue')
        },
        {
          path: '/lowvar',
          name: 'LowVariability',
          component: () => import(/* webpackChunkName: "demo" */ './views/LowVariability.vue')
        },
        {
          path: '/value',
          name: 'ValueStrategy',
          component: () => import(/* webpackChunkName: "demo" */ './views/Value.vue')
        },
        {
          path: '/momentum',
          name: 'Momentum',
          component: () => import(/* webpackChunkName: "demo" */ './views/Momentum.vue')
        },
        {
          path: '/quality',
          name: 'QualityStrategy',
          component: () => import(/* webpackChunkName: "demo" */ './views/Quality.vue')
        }
      ]
    },
    {
      path: '/',
      redirect: 'login',
      component: AuthLayout,
      children: [
        {
          path: '/login',
          name: 'login',
          component: () => import(/* webpackChunkName: "demo" */ './views/Login.vue')
        },
        {
          path: '/register',
          name: 'register',
          component: () => import(/* webpackChunkName: "demo" */ './views/Register.vue')
        }
      ]
    }
  ]
})
