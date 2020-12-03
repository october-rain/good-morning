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
                @click.native="handleClickToArticle(item)"
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
            articleList: [],
            content: "",
        }
    },
    components: {
        ListItem,
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
    methods: {
        handleClickToArticle(item) {
            console.log("id",item.id);
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
