import { createRouter, createWebHistory } from 'vue-router'
import DeviceBinding from '../views/DeviceBinding.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'device-binding',
      component: DeviceBinding
    }
  ]
})

export default router
