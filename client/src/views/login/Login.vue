<template>
    <div class="start" :class="[switchBg]">
        <div class="switch">
            <span class="one" @click="handleClickSpring">春</span>
            <span class="two" @click="handleClickAutumn">秋</span>
        </div>
        <sign-in @switch="handelSwitch" v-show="hasUser" />
        <sign-up @switch="handelSwitch" v-show="!hasUser" />
    </div>
</template>

<script>
import SignIn from "./components/SignIn"
import SignUp from "./components/SignUp"

export default {
    name: "Login",
    components: {
        SignIn,
        SignUp,
    },
    data() {
        return {
            hasUser: true,
            switchBg: 'spring'
        }
    },
    methods: {
        handelSwitch() {
            this.hasUser = !this.hasUser
        },
        handleClickSpring(){
            this.switchBg = 'spring'
        },
        handleClickAutumn(){
            this.switchBg = 'autumn'
        }
    },
}
</script>

<style lang="stylus" scoped>

.start
    width 100%
    height 100vh
    position relative
    max-width unset
    background-size cover
    background-repeat no-repeat
    background-position center
    .switch
        position absolute
        width 20%
        height 4rem
        line-height 4rem
        background #63636610
        top 5rem
        right 5rem
        cursor pointer
        font-size 1.6rem
        .one
            display inline-block
            margin-right 30%
            padding 0 .6rem
        .two
            display inline-block
            padding 0 .6rem
.spring
    background-image url(../../assets/pictures/pexels-jaymantri-4827.jpg)
.autumn
    background-image url(../../assets/pictures/pexels-efdal-yildiz-917494.jpg)


</style>
