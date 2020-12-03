<template>
    <div class="body">
        <!-- header -->
        <ul class="list">
            <router-link
                class="itemrouter"
                tag="li"
                to="/article"
                v-for="item in articleList"
                :key="item.id"
                @click="handleClickToArticle(item)"
            >
                <list-item :article="item"></list-item>
            </router-link>
        </ul>
    </div>
</template>

<script>
import ListItem from "./components/ListItem"
// import axios from "axios"
// import Qs from "qs"

export default {
    name: "List",
    data() {
        return {
            articleList: [
                {
                    id: 1,
                    title: "我的第一篇文章",
                    desc: "文章描述",
                    cover:
                        "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1144136955,2127408886&fm=26&gp=0.jpg",
                    time: "2020-12-03",
                    author: "tian",
                },
                {
                    id: 2,
                    title: "我的第二篇文章",
                    desc: "文章描述",
                    cover:
                        "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1144136955,2127408886&fm=26&gp=0.jpg",
                    time: "2020-12-03",
                    author: "tian",
                },
                {
                    id: 3,
                    title: "我的第三篇文章",
                    desc: "文章描述",
                    cover:
                        "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1144136955,2127408886&fm=26&gp=0.jpg",
                    time: "2020-12-03",
                    author: "tian",
                },
            ],
            content: "",
        }
    },
    components: {
        ListItem,
    },
    beforeMount() {
        this.$store.dispatch("getArticleList").then((res) => {
            if (res) {
                this.articleList = this.$store.state.articleList
            }
        })
    },
    methods: {
        handleClickToArticle(item) {
            this.$store.dispatch('getArticle',item.id)
        },
    },
}
</script>

<style lang="stylus" scoped>
.list
    padding-top 3rem
    max-width 80rem
    margin 0 auto
    .itemrouter
        margin-top 3rem
</style>
