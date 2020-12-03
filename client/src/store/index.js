import Vue from "vue"
import Vuex from "vuex"
import Qs from "qs"
import axios from "axios"

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        userInfo: {
            // username: '',
            token: "",
        },
        articleList: [],
        article: {},
    },
    getters: {
        isUserLogin(state) {
            return state.userInfo.token
        },
    },
    actions: {
        // {commit} 这是利用上下文的语法，使用commit函数方法
        signIn({ commit }, userInfo) {
            axios({
                url: "http://127.0.0.1:9000/api/morn-login/",
                method: "post",
                data: Qs.stringify(userInfo),
            }).then((res) => {
                console.log(res.data)
                if (res.data == "nouser") {
                    alert("用户名不存在")
                    return
                }
                if (res.data == "pwderr") {
                    alert("密码错误")
                    return
                }
                // 写跳转链接
                userInfo.token = res.data
                console.log(userInfo)
                commit("changeLoginUserInfo", userInfo.token)
                // 缓存
                localStorage.setItem("token", res.data)
                alert("登录成功！")
            })
        },
        signUp({ commit }, userInfo) {
            axios({
                url: "http://127.0.0.1:9000/api/morn-register/",
                method: "post",
                data: Qs.stringify(userInfo),
            }).then((res) => {
                // console.log(res)
                if (res.data == "repeat") {
                    alert("用户名已存在！")
                    return
                }
                // 写跳转链接
                userInfo.token = res.data
                commit("changeLoginUserInfo", userInfo.token)
                // 缓存
                localStorage.setItem("token", res.data)
                alert("注册成功!")
            })
        },
        logout({ commit }) {
            commit("clearUserInfo")
        },
        tryAutoLogin({ commit }) {
            let token = localStorage.getItem("token")
            if (token) {
                axios({
                    url: "http://127.0.0.1:9000/api/morn-login/",
                    method: "get",
                    // data: Qs.stringify({token})
                    params: { token },
                }).then((res) => {
                    console.log("自动登陆返回信息", res)
                    if (res.data == "error") {
                        alert("用户登陆过期，请重新登陆")
                        return
                    }
                    commit("changeLoginUserInfo", token)
                })
            }
        },
        async getArticleList({ commit }) {
            let success = false
            await axios({
                url: "http://127.0.0.1:9000/api/get-articlelist/",
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
        getArticle({ commit }, articleId) {
            axios({
                url: "http://127.0.0.1:9000/api/get-article/",
                params: {
                    id: articleId,
                },
            }).then((res) => {
                let articleContent = res.data.content
                commit("setArticleInfo", {articleContent, articleId})
                console.log("获取 article 成功", res)
            })
        },
    },
    mutations: {
        changeLoginUserInfo(state, token) {
            state.userInfo.token = token
            // console.log(state.userInfo.token);
        },
        clearUserInfo(state) {
            state.userInfo = {
                username: "",
                token: "",
            }
        },
        setArticleListInfo(state, articleList) {
            state.articleList = articleList
            // console.log("state.articleList",state.articleList);
        },
        setArticleInfo(state, data) {
            state.article.content = data.articleContent
            // console.log(state.article.content)
            // console.log(state.articleList)
            // console.log(data.articleId)
            let found = state.articleList.find((obj) => obj.id == data.articleId)
            // console.log("found", found)
            state.article.title = found.title
            state.article.desc = found.desc
            state.article.cover = found.cover
            state.article.time = found.time
            state.article.author = found.author
            // console.log("state.article", state.article);
        },
    },
    modules: {},
})
