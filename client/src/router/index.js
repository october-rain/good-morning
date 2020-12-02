import Vue from "vue"
import VueRouter from "vue-router"
import Home from "@/views/home/Home.vue"
import Login from "@/views/login/Login.vue"

Vue.use(VueRouter)

const routes = [
    {
        path: "/",
        name: "home",
        component: Home,
    },
    {
        path: "/login",
        name: "login",
        component: Login,
        //component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue')
    },
]

const router = new VueRouter({
    routes,
})

export default router
