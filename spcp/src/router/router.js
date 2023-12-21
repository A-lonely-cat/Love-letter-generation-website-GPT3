import { createRouter, createWebHashHistory } from 'vue-router'
import Qingshu from '../components/showmainn.vue'
import Index from '../components/index.vue'

const routes = [
    {
        name: "index",
        path: '/',
        component: Index
    },
    {
        name: "qingshu",
        path: "/qingshu",
        component: Qingshu
    }
]


const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router