import { createRouter, createWebHistory } from 'vue-router'
//import { createRouter, createWebHashHistory } from 'vue-router' // 手动改为hash模式
import HomeView from '../views/HomeView.vue'
import Table from '@/views/Table.vue'
import Table2 from '@/views/Table2.vue'
import Table3 from '@/views/Table3.vue'
import Table4 from '@/views/Table4.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  // history: createWebHashHistory(), //手动改为hash模式
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/table',
      name: 'table',
      component: Table
    },
    {
      path: '/table2',
      name: 'table2',
      component: Table2
    },
    {
      path: '/table3',
      name: 'table3',
      component: Table3
    },
    {
      path: '/table4',
      name: 'table4',
      component: Table4
    }
  ]
})

export default router
