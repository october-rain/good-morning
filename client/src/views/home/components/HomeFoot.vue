<template>
    <div class="foot">
        <div class="content">
            <div class="wechat" title="微信公众号">
                OctoberRain
            </div>
            <div class="github" title="点个star吧！">github</div>
            <div class="weibo" title="微博">weibo</div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src

export default {
    name: "HomeFoot",
}
</script>

<style lang="stylus" scoped>

.foot
    width 100%
    height 5rem
    background-color #17181b40
    position absolute
    bottom 0
    display flex
    justify-content center
    align-items center
    color white
    .content
        width 70%
        display flex
        justify-content space-between
</style>
