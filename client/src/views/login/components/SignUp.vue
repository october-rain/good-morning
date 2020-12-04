<template>
    <div class="sign-up">
        <form class="form">
            <div class="input account">
                <input
                    type="text"
                    class="field"
                    v-model="userInfo.username"
                    autocomplete="on"
                />
                <label class="label">账号：</label>
            </div>
            <div class="input password">
                <input
                    type="password"
                    class="field"
                    v-model="userInfo.password"
                    autocomplete="on"
                />
                <label class="label">密码：</label>
            </div>
            <div class="input password">
                <input
                    type="password"
                    class="field"
                    v-model="userInfo.password2"
                    autocomplete="on"
                    @keyup.enter="handleClickRegister"
                />
                <label class="label">再次输入：</label>
            </div>
            <div class="button">
                <div
                    type="submit"
                    class="btn signin-btn"
                    @click="handleClickRegister"
                >
                    注册
                </div>
                <!-- <div class="btn signup-btn">注册</div> -->
            </div>
            <div class="switch">已经注册？点击<span class="register" @click="handleClickLogin">登陆</span></div>
        </form>
    </div>
</template>

<script>

export default {
    name: "SignUp",
    props: {
        hasUser: Boolean
    },
    mounted(){
        console.log(this.userInfo)
    },
    data() {
        return {
            userInfo: {
                username: "",
                password: "",
                password2:"",
            },
            hasThisUser: this.hasUser
        }
    },
    methods: {
        handleClickRegister() {
            if(this.userInfo.username == "" || this.userInfo.password == '' || this.userInfo.password2 == ''){
                alert('输入内容不能为空！')
                return
            }
            if(this.userInfo.password2 != this.userInfo.password){
                alert('两次输入密码不一致！')
                return
            }
            if(this.userInfo.password.length < 8){
                alert('密码不能小于8位数')
                return
            }
            this.$store.dispatch('signUp', this.userInfo)
            this.$router.push({path: '/'})
        },
        handleClickLogin(){
            this.hasThisUser = !this.hasThisUser
            this.$emit('switch')
        }
    },
}
</script>

<style lang="stylus" scoped>

.sign-up
    position absolute
    top 50%
    left 50%
    margin-top -20rem
    margin-left -25rem
    height 40rem
    width 50rem
    background-color #958A8A40
    border-radius 1rem
    .form
        width 100%
        height 100%
        display flex
        flex-direction column
        align-items center
        border-radius 1rem
        user-select none 
        margin-top 1rem
        .input
            position relative
            .field
                width 32rem
                background-color transparent
                border none
                border-bottom .1rem solid #0004
                margin 2rem 0
                padding 1rem 1.5rem 1.5rem 0
                font-size 1.6rem
                color #4b4b4b
                text-indent 6rem
                &:focus
                    text-indent 10px
                &:focus~label
                    transform translateY(-3.5rem)
                    font-size 1.4rem
            .label
                position absolute
                left 0
                font-size 2rem
                color #4b4b4b
                pointer-events none
                text-transform uppercase
                transition: all 0.3s;
                bottom: 3.4rem;
        .button
            margin-top 2.5rem
            width 25%
            height 3rem
            border .1rem solid #000
            border-radius .8rem
            line-height 3rem
            font-size 1.6rem
            .signin-btn
                color #000
                cursor pointer
                letter-spacing 1rem
                padding-left .5rem
        .switch
            font-size 1.6rem
            margin-top 3rem
            letter-spacing .12rem
            .register
                color red
</style>
