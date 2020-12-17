import Vue from "vue"
import Vuex from "vuex"
import Qs from "qs"
import axios from "axios"

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        userInfo: {},
        articleList: [],
    },
    getters: {
        isUserLogin(state) {
            return state.userInfo.token
        },
        getUserInfo(state) {
            return state.userInfo
        },
    },
    actions: {
        // {commit} 这是利用上下文的语法，使用commit函数方法
        signIn({ commit }, userInfo) {
            axios({
                url: "https://api.tian999.top/api/morn-login/",
                method: "post",
                data: Qs.stringify(userInfo),
            }).then((res) => {
                if (res.data == "nouser") {
                    alert("用户名不存在")
                    return
                }
                if (res.data == "pwderr") {
                    alert("密码错误")
                    return
                }
                commit("changeLoginUserInfo", res.data)
                // 缓存
                localStorage.setItem("token", res.data.token)
                // console.log("res",res);
                alert("登录成功！")
            })
        },
        signUp({ commit }, userInfo) {
            axios({
                url: "https://api.tian999.top/api/morn-register/",
                method: "post",
                data: Qs.stringify(userInfo),
            }).then((res) => {
                // console.log(res)
                if (res.data == "repeat") {
                    alert("用户名已存在！")
                    return
                }
                // 写跳转链接
                commit("changeLoginUserInfo", res.data)
                // 缓存
                localStorage.setItem("token", res.data.token)
                console.log("res.data.token", res.data.token)
                // console.log("res",res);
                alert("注册成功!")
            })
        },
        logout({ commit }) {
            commit("clearUserInfo")
        },
        tryAutoLogin({ commit }) {
            let token = localStorage.getItem("token")
            // console.log("token", token)
            if (token) {
                axios({
                    url: "https://api.tian999.top/api/morn-login/",
                    method: "get",
                    // data: Qs.stringify({token})
                    params: { token },
                }).then((res) => {
                    // console.log("自动登陆返回信息", res)
                    if (res.data == "error") {
                        // alert("用户登陆过期，请重新登陆")
                        console.log("用户登陆过期，请重新登陆")
                        return
                    }
                    // console.log("res",res)
                    commit("changeLoginUserInfo", res.data)
                })
            }
        },
        async getArticleList({ commit }) {
            let success = false
            await axios({
                url: "https://api.tian999.top/api/get-articlelist/",
                method: "GET",
                // data: Qs.stringify()
            }).then((res) => {
                let articleList = res.data.article_list
                commit("setArticleListInfo", articleList)
                if (res.data.num > 0) {
                    success = true
                    // console.log("success", success)
                }
                console.log("获取 article list 成功", res.data)
            })
            // console.log("success", success)
            return success
        },
        async getPersonalArticleList({ commit }) {
            let success = false
            let token = localStorage.getItem("token")
            // console.log("token", token)
            if (token) {
                await axios({
                    url: "https://api.tian999.top/api/get-userarticle/",
                    method: "POST",
                    // data: Qs.stringify(token),
                    data: Qs.stringify({ token }),
                    // params: {token: token}
                }).then((res) => {
                    let articleList = res.data
                    commit("setArticleListInfo", articleList)
                    if (res.data.length > 0) {
                        success = true
                        // console.log("success", success)
                    }
                    console.log("获取 personal article list 成功", res.data)
                })
            }
            // console.log("success", success)
            return success
        },
    },
    mutations: {
        changeLoginUserInfo(state, userInfo) {
            // state.userInfo.token = userInfo.token
            state.userInfo = userInfo
            // console.log("state.userInfo", state.userInfo);
        },
        clearUserInfo(state) {
            localStorage.setItem("token", "")
            state.userInfo = {}
        },
        setArticleListInfo(state, articleList) {
            state.articleList = articleList
            // console.log("state.articleList",state.articleList);
        },
    },
    modules: {},
})
