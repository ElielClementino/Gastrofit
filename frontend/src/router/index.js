import { createRouter, createWebHistory } from 'vue-router'
import ingredientsRoutes from "./ingredients.routes.js"
import homeRoutes from './home.routes'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    ...homeRoutes,
    ...ingredientsRoutes,
  ]
})

export default router
