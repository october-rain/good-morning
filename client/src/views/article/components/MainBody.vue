<template>
    <div class="article-body">
        <!-- 边角信息 -->
        <div
            id="scene"
            class="cover"
            :style="{ backgroundImage: 'url(' + article.cover + ')' }"
        >
            <div class="mask"></div>
            <div class="title">{{ article.title }}</div>
        </div>
        <div class="wrapper">
            <div class="article markdown-body">
                <div class="info">
                    <div class="desc">文章描述：{{ article.desc }}</div>
                    <div class="author">作者：{{ article.author }}</div>
                    <div class="time">时间：{{ article.time }}</div>
                </div>
                <div class="content" v-html="content" v-highlight></div>
            </div>
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
            id: this.$route.params.id,
            article: {},
        }
    },
    created() {
        this.getArticleInfo()
    },
    methods: {
        getArticleInfo() {
            axios({
                url: "https://api.tian999.top/api/get-article/",
                params: {
                    id: this.$route.params.id,
                },
            }).then((res) => {
                this.article = res.data
                this.content = res.data.content
                this.markdownRender()
                // console.log("this.content", this.content)
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
            // console.log("this.content", this.content)
            this.content = marked(this.content)
            // console.log(this.content);
        },
    },
}
</script>

<style lang="stylus" scoped>
// .info
//     z-index 100
.article-body
    position relative
    .cover
        position relative
        display flex
        align-items center
        height 40vh
        overflow hidden
        padding 0
        border 0
        overflow hidden
        background-position center center
        background-size cover
        transform translate3d(0px, 0px, 0px)
        // margin-top -15vh
        z-index -1
        .mask
            position absolute
            width 100%
            height 100%
            background #0007
            z-index -1
        .title
            margin 0 auto
            font-size 5rem
            color #eee
            z-index 2
    .wrapper
        background-image url(../../../assets/pictures/pexels-tom-verdoot-1530216.jpg)
        background-attachment fixed
        background-size cover
        background-repeat no-repeat
        padding 5rem 0
        .article
            padding 3rem 0
            margin-top 2rem
            background #fff
            max-width 65vw
            margin 0 auto
            z-index 10
            // background red
            // border .1rem solid #000
            border-radius 2rem
            font-size 1.6rem
            box-shadow:
                0 -12.5px 10px rgba(0, 0, 0, 0.06),
                0 -6.7px 5.3px rgba(0, 0, 0, 0.048),
                0 -2.8px 2.2px rgba(0, 0, 0, 0.034),
                0 2.8px 2.2px rgba(0, 0, 0, 0.034),
                0 6.7px 5.3px rgba(0, 0, 0, 0.048),
                0 12.5px 10px rgba(0, 0, 0, 0.06),
                0 22.3px 17.9px rgba(0, 0, 0, 0.072),
                0 41.8px 33.4px rgba(0, 0, 0, 0.086),
                0 100px 80px rgba(0, 0, 0, 0.12)
            .info
                // max-width 80vw
                margin 0 auto
                font-size 2rem
                display grid
                grid-template-columns 1fr 1fr
                grid-template-areas:"desc ." "author time"
                grid-gap 3rem 20px
                justify-items center
                align-items end
                .desc
                    grid-area desc
                .author
                    grid-area author
                .time
                    grid-area time
                    font-size 1.2rem
            .content
                max-width 65rem
                margin 0 5rem
</style>
