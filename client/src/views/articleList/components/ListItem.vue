<template>
    <div class="list-item">
        <div class="cover"><img :src="articleInfo.cover" /></div>
        <div class="article">
            <div class="content">
                <div class="title">{{ articleInfo.title }}</div>
                <div class="desc">{{ articleInfo.desc }}</div>
            </div>

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
    height 28rem
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
        position relative
        display flex
        flex-direction column
        justify-content space-between
        align-items flex-start
        padding 2rem
        height 100%
        .content
            .title
                font-size 1.8rem
                margin 1rem 0 2rem 0
            .desc
                font-size 1.4rem
                // text-indent 1.6rem
        .info
            align-self flex-end
</style>
