<template>
    <header class="header">
        <div class="logo" @click="triggerPage('/')">十雨札记</div>
        <nav class="nav">
            <span class="mood">心情</span>
            <span class="article" @click="triggerPage('personal-article')">文章</span>
            <span class="data">数据</span>
        </nav>
        <div class="profile">
            <div class="head" @click="show = !show">
                <img class="headimg" :src="getUserProfile.headimg" alt="头像" />
            </div>
            <div class="dropdown" v-show="show">
                <div class="edit">编辑</div>
                <div class="writing" @click="triggerPage('addarticle')">
                    写作
                </div>
                <div class="logout" @click="triggerPage('logout')">登出</div>
            </div>
        </div>
    </header>
</template>

<script>
// @ is an alias to /src

export default {
    name: "ProfileHeader",
    data() {
        return {
            show: false,
        }
    },
    computed: {
        getUserProfile() {
            // console.log(this.$store.getters.getUserInfo)
            return this.$store.getters.getUserInfo
        },
    },
    mounted() {
        // 点击下拉框之外的区域让下拉框消失
        document.addEventListener("click", (e) => {
            // console.log("e", e.target)
            // console.log("!this.$el.contains(e.target)",!this.$el.contains(e.target))
            if (!this.$el.contains(e.target)) this.show = false
        })
    },
    methods: {
        triggerPage(path) {
            if (path === "logout") {
                this.$store.dispatch("logout")
                this.$router.push("/")
            } else {
                console.log(123)
                this.$router.push(path)
            }
        },
    },
}
</script>

<style lang="stylus" scoped>

.header
    width 100vw
    height 6rem
    z-index 10
    display grid
    grid-template-columns 3fr 10fr 1fr
    align-items center // 垂直居中
    padding 0 5rem
    position relative
    background-color #00000040
    .logo
        font-size 2rem
        cursor pointer
        // color: #e7e9ec
    .nav
        justify-self end
        padding-top .2rem
        span
            cursor pointer
            font-size 1.6rem
            margin 3rem
            // color #e7e9ec
    .profile
        position relative
        justify-self end
        .head
            width 3rem
            height 3rem
            border-radius 50%
            overflow hidden
            cursor pointer
            .headimg
                width 100%
        .dropdown
            position absolute
            top 4.5rem
            right 0
            width 6rem
            height 11.5rem
            text-align center
            line-height 1.5
            font-size 1.6rem
            letter-spacing .3rem
            background #e7e9ec
            border-radius .5rem
            div
                margin 1rem
                padding-left .2rem
                cursor pointer
</style>
