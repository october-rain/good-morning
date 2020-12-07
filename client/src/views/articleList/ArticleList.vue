<template>
    <div class="body">
        <exhibit></exhibit>
        <ul class="list">
            <router-link
                class="itemrouter"
                tag="li"
                :to="'/article/' + item.id"
                v-for="item in articleList"
                :key="item.id"
            >
                <list-item :article="item"></list-item>
            </router-link>
        </ul>
    </div>
</template>

<script>
import ListItem from "./components/ListItem"
import Exhibit from './components/Exhibit'
// import axios from "axios"
// import Qs from "qs"

export default {
    name: "List",
    data() {
        return {
            articleList: [],
        }
    },
    components: {
        ListItem,
        Exhibit,
    },
    beforeMount() {
        this.$store.dispatch("getArticleList").then((res) => {
            if (res) {
                // console.log(res);
                this.articleList = this.$store.state.articleList
                // console.log("this.articleList", this.articleList);
            }
        })
    },
    // methods: {
    //     handleClickToArticle(item) {
    //         console.log("id",item.id);
    //         this.$store.dispatch('getArticle',item.id)
    //     },
    // },
}
</script>

<style lang="stylus" scoped>
.list
    padding-top 3rem
    padding-left 0
    max-width 80rem
    margin 0 auto
    .itemrouter
        margin-top 3rem
</style>
