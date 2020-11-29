<template>
    <div class="header">
        <div class="link">
            <div class="main">主页</div>
            <div class="article">全部</div>
            <div class="rain">十雨</div>
            <div class="about">关于十雨</div>
            <div class="login">
                <router-link to="/login">登陆</router-link>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src

export default {
    name: "HomeInfo",
}
</script>

<style lang="stylus" scoped>

.header
    border 1px solid black
    width 100%
    height 5rem
    font-size 1.3rem
    display flex
    justify-content center
    align-items center
    .link
        display flex
        width 70%
        justify-content space-between

</style>
