<template>
    <div class="header">
        <div class="link">
            <div class="main">主页</div>
            <div class="article">全部</div>
            <div class="rain">十雨</div>
            <div class="about">关于十雨</div>
            <div class="login" v-if="!authUserLogin" @click="triggerPage('/login')">登陆</div>
            <div class="logout" v-else @click="triggerPage('logout')">登出</div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src

export default {
    name: "HomeInfo",
    computed: {
        // 验证用户是否登陆，登陆在homeHeader里显示“登出”
        authUserLogin(){
            console.log('authUserLogin',this.$store.getters.isUserLogin);
            return this.$store.getters.isUserLogin ? true : false
        }
    },
    methods: {
        triggerPage(path){
            // this.LoginOrLogout = !this.authUserLogin
            // console.log(this.LoginOrLogout);
            if (path === "logout") {
                this.$store.dispatch("logout")
                // this.$store.commit('clearUserInfo')
                // this.$message.success("登出成功")
            } else {
                this.$router.push(path)
            }
        },
    },
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
