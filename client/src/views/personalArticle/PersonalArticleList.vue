<template>
    <div class="personal-body">
        <!-- <exhibit></exhibit> -->
        <ul class="list">
            <router-link
                class="itemrouter"
                tag="li"
                :to="'/article/' + item.id"
                v-for="item in articleList"
                :key="item.id"
            >
                <list-item class="item" :article="item"></list-item>
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
        }
    },
    components: {
        ListItem,
    },
    beforeMount() {
        this.$store.dispatch("getPersonalArticleList").then((res) => {
            if (res) {
                console.log(res);
                this.articleList = this.$store.state.articleList
                console.log("this.articleList", this.articleList);
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

<style lang="stylus">
.personal-body
    // background-color #444
    .list
        background-color #fff
        padding-top 3rem
        padding-left 0
        max-width 80rem
        margin 0 auto 8rem
        .itemrouter
            margin-top 8rem
            box-shadow: 8px 8px 2px 1px rgba(0, 0, 255, .2);
        .itemrouter:nth-child(2n)
            .cover
                float right
</style>
