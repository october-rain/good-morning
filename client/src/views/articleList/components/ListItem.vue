<template>
    <div class="list-item">
        <div class="cover"><img :src="articleInfo.cover" /></div>
        <div class="article">
            <div class="title">{{ articleInfo.title }}</div>
            <div class="desc">{{ articleInfo.desc }}</div>
            <div class="info">
                <div class="time">{{ articleInfo.time }}</div>
                <div class="author">{{ articleInfo.author }}</div>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src

export default {
    name: "ListItem",
    props: {
        article: Object,
    },
    data() {
        return {
            articleInfo: this.article,
        }
    },
}
</script>

<style lang="stylus" scoped>
.list-item
    position relative
    width 100%
    background-color #2e2e2e
    overflow auto
    cursor pointer
    color #eee
    .cover
        height 28rem
        // min-height 28rem 具体还得后期再调
        max-width 49rem
        overflow: hidden
        float left
        img
            // height 16rem
            height 100%
            vertical-align middle  // 解决基线问题（底部多出2像素）
            // margin-top -50%
    .article
        float left
        padding 2rem
        .title
            font-size 1.6rem
            font-weight bold
            margin 1rem 0 2rem 0
        .desc
            font-size 1.4rem
        .info
            // position absolute
            // top 12rem
            // right 4rem
            padding-top 14rem
            padding-left 18rem
            font-size 1.2rem
            text-align end
            .time 
                font-size 1rem
                margin-bottom .4rem

</style>
