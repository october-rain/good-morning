<template>
    <div class="list-item">
        <div class="cover"><img :src="articleInfo.cover" /></div>
        <div class="article">
            <div class="title">{{articleInfo.title}}</div>
            <div class="desc">{{articleInfo.desc}}</div>
        </div>
        <div class="info">
            <div class="time">{{articleInfo.time}}</div> 
            <div class="author">{{articleInfo.author}}</div>    
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
            articleInfo: this.article
        }
    },
}
</script>

<style lang="stylus" scoped>
.list-item
    position relative
    width 100%
    background #666
    overflow auto
    .cover
        height 16rem
        overflow: hidden
        float left
        img
            // height 16rem
            width 28rem
            vertical-align middle  // 解决基线问题（底部多出2像素）
            margin-top -50%
    .article
        float left
        padding 2rem
    .info
        position absolute
        top 12rem
        right 4rem
</style>
