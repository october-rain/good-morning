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
        path: "/me",
        name: "Me",
        component: () => import("../views/me/Me.vue"),
    },
    {
        path: "/login",
        name: "Login",
        component: Login,
        //component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue')
    },
    {
        path: "/profile",
        name: "Profile",
        component: () => import("../views/profile/Profile.vue"),
    },
    {
        path: "/addarticle",
        name: "AddArticle",
        // which is lazy-loaded when the route is visited.
        component: () =>
            import(
                /* webpackChunkName: "about" */ "../views/addArticle/AddArticle.vue"
            ),
    },
    {
        path: "/articlelist",
        name: "ArticleList",
        // which is lazy-loaded when the route is visited.
        component: () =>
            import(
                /* webpackChunkName: "about" */ "../views/articleList/ArticleList.vue"
            ),
    },
    {
        path: "/article/:id",
        name: "Article",
        // which is lazy-loaded when the route is visited.
        component: () =>
            import(
                /* webpackChunkName: "about" */ "../views/article/Article.vue"
            ),
    },
]

const router = new VueRouter({
    routes,
})

export default router
