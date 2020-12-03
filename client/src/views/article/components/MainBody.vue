<template>
    <div class="body">
        <!-- 边角信息 -->
        <div class="content markdown-body">
            <div v-html="content" v-highlight></div>
        </div>
    </div>
</template>

<script>
import marked from "marked"
// import "highlight.js/styles/monokai-sublime.css"
import "highlight.js/styles/solarized-dark.css"

export default {
    name: "MainBody",
    data() {
        return {
            content: "### 标题",
            article: this.$store.state.article,
        }
    },
    mounted() {
        this.markdownRender()
    },
    methods: {
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
            
            this.article = this.$store.state.article
            console.log("this.article",this.article)
            this.content = marked(this.article.content)
            // console.log(this.content);
        },
    },
}
</script>

<style lang="stylus" scoped></style>