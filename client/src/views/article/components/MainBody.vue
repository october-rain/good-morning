<template>
    <div class="body">
        <!-- 边角信息 -->
        <div class="info">
            <div class="title">{{article.title}}</div>
            <div class="desc">{{article.desc}}</div>
            <div class="author">{{article.author}}</div>
            <div class="time">{{article.time}}</div>
            <div class="cover"><img :src="article.cover" alt=""></div>
        </div>
        <div class="content markdown-body">
            <div v-html="content" v-highlight></div>
        </div>
    </div>
</template>

<script>
import axios from "axios"
import marked from "marked"
// import "highlight.js/styles/monokai-sublime.css"
import "highlight.js/styles/solarized-dark.css"

export default {
    name: "MainBody",
    data() {
        return {
            content: "### 标题",
            articleList: this.$store.state.articleList,
            id: this.$route.params.id,
            article: {}
        }
    },
    mounted() {
        this.getArticleInfo()
    },
    methods: {
        getArticleInfo() {
            this.article = this.articleList.find((obj) => obj.id == this.id)
            console.log(this.article);
            axios({
                url: "http://127.0.0.1:9000/api/get-article/",
                params: {
                    id: this.$route.params.id,
                },
            }).then((res) => {
                this.content = res.data.content
                this.markdownRender()
                console.log("this.content", this.content)
                console.log("获取 article 成功", res)
            })
        },
        markdownRender() {
            marked.setOptions({
                renderer: new marked.Renderer(),
                pedantic: false,
                gfm: true,
                tables: true,
                breaks: false,
                sanitize: false,
                smartLists: true,
                smartypants: false,
                xhtml: false,
            })
            console.log("this.content", this.content)
            this.content = marked(this.content)
            // console.log(this.content);
        },
    },
}
</script>

<style lang="stylus" scoped></style>
