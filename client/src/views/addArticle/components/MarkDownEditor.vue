<template>
    <div class="md">
        <vue-simplemde
            v-model="content"
            ref="markdownEditor"
            preview-class="markdown-body"
            :highlight="true"
            :configs="configs"
        />
        <!-- <div class="button" @click="handleClickSubmit">提交1</div> -->
    </div>
</template>

<script>
// ! 在main.js中已经定义了，所以不用再次写，因此注释
// import VueSimplemde from 'vue-simplemde'
// import hljs from 'highlight.js';
// window.hljs = hljs;

export default {
    name: "MarkDownEditor",
    // components: {
    //   VueSimplemde
    // }
    // props: {
    //     isSubmit: {
    //         type: Boolean,
    //         default: false,
    //     },
    // },
    data() {
        return {
            // mdIsSubmit: this.isSubmit,
            content: "",
            configs: {
                // promptURLs: true,
                spellChecker: false,
                toolbar: [
                    "clean-block",
                    "|",
                    "bold",
                    "italic",
                    "strikethrough",
                    "|",
                    "heading-smaller",
                    "heading-bigger",
                    "quote",
                    "code",
                    "horizontal-rule",
                    "|",
                    "unordered-list",
                    "ordered-list",
                    "table",
                    "|",
                    "link",
                    "image",
                    "|",
                    "preview",
                    "side-by-side",
                    "fullscreen",
                    "|",
                    "guide",
                ],
            },
        }
    },

    // 监听父组件传值
    // computed: {
    //     mdIsSubmit(){
    //         console.log("点击了提交3", this.isSubmit);
    //         this.$emit("add", this.content)
    //         return this.isSubmit
    //     }
    // },
    computed: {
        simplemde() {
            console.log(this.$refs.markdownEditor.simplemde)
            return this.$refs.markdownEditor.simplemde
        },
    },
    watch: {
        content(){
            this.$emit("add", this.content)
        },
        // isSubmit() {
        //     // handle() {
        //     //     console.log("点击了提交", this.isSubmit)
        //     //     return this.isSubmit
        //     // },
        //     // immediate: true
        //     // if(this.content === ''){
        //     //     alert('请写入文章')
        //     //     this.content = '请写入文章'
        //     //     console.log(1);
        //     // } else
        //     if (this.isSubmit) {
        //         // console.log(newV, oldV)
        //         console.log(2)
        //         console.log("点击了提交", this.isSubmit)
        //         // this.$emit("add", this.content)
                
        //     }
        // },
    },
    // methods: {
    //     handleClickSubmit() {
    //         this.$emit("add", this.content)
    //     },
    // },
}
</script>

<style lang="stylus">
/* @import '~simplemde/dist/simplemde.min.css';
@import '~simplemde/dist/simplemde.min.css';
@import '~highlight.js/styles/atom-one-dark.css';
@import '~github-markdown-css'; */
.md
    max-width 76rem
    margin 0 auto
    font-size 1.4rem
    background #fff
    border-radius 2rem
    .editor-toolbar
        border none
    .CodeMirror
        height 60vh
 
</style>
