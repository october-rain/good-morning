<template>
    <header class="header">
        <div class="logo">十雨札记</div>
        <nav class="nav">
            <span class="main" @click="triggerPage('/articlelist')">主页</span>
            <span class="article" @click="triggerPage('/category')">分类</span>
            <span class="rain" @click="triggerPage('/octoberrain')">十雨</span>
        </nav>
        <div :class="infoClass">
            <span
                class="login"
                v-if="!authUserLogin"
                @click="triggerPage('/login')"
                >登陆</span
            >
            <span class="me" v-else @click="triggerPage('profile')"
                ><img class="headimg" :src="headImg" alt="头像"></span
            >
        </div>
    </header>
</template>

<script>
// @ is an alias to /src

export default {
    name: "HomeInfo",
    // data() {
    //     return {
    //         headImg: this.$store.getters.getUserInfo.profile.headimg
    //     }
    // },
    // mounted() {
    //     console.log(this.$store.getters.getUserInfo.profile);
    // },
    computed: {
        // 验证用户是否登陆，登陆在homeHeader里显示“登出”
        authUserLogin() {
            // console.log('authUserLogin',this.$store.getters.isUserLogin);
            return this.$store.getters.isUserLogin ? true : false
        },
        infoClass(){
            return this.$store.getters.isUserLogin ? "after-login" : "info"
        },
        headImg(){
            // console.log(this.$store.getters.getUserInfo);
            return this.$store.getters.getUserInfo.headimg
        }
    },
    methods: {
        triggerPage(path) {
            this.$router.push(path)
        },
    },
}
</script>

<style lang="stylus" scoped>
.header
    width 100vw
    height 6rem
    display grid
    padding 0 5rem
    grid-template-columns 3fr 10fr 1fr
    align-items center
    position relative
    z-index 10
    background-color #00000040
    .logo
        font-size 2rem
        font-weight 600
        color: #e7e9ec
    .nav
        padding-top .2rem
        justify-self end
        span
            font-size 1.6rem
            color #e7e9ec
            margin 3rem
            cursor pointer
    .info
        padding-top .2rem
        justify-self end
        span
            color #e7e9ec
            font-size 1.6rem
            display inline-block
            width 100%
            height 100%
            line-height 3rem
            text-align center
            cursor pointer
    .after-login
        width 3rem
        height 3rem
        border-radius 50%
        justify-self end
        overflow hidden
        cursor pointer
        .headimg
            width 100%

</style>
