import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
    meta: { title: 'Home' }
  },
  {
    path: '/video-preview',
    name: 'VideoPreview',
    component: () => import('../views/video-preview.vue'),
    meta: { title: 'Video Preview' }
  },
  {
    path: '/main',
    name: 'Main',
    component: () => import('../views/main.vue'),
    meta: { title: 'Main' }
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0, behavior: 'smooth' }
    }
  }
})

export default router
