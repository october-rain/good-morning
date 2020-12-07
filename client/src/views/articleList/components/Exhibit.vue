<template>
    <div class="exhibit">
        <div id="scene" class="wrapper-img" v-parallax="0.4">
            <!-- <div data-depth="0.4" class="layer"> -->
            <img
                class="inner-img"
                src="../../../assets/pictures/rain-2563986_1920.jpg"
                :width="imgWidth"
                :height="imgHeight"
            />
            <!-- </div> -->
        </div>

        <div class="solgan">
            <h1 v-parallax="-0.2">THIS IS OCTOBER RAIN</h1>
            <h1 v-parallax="0.3">THIS IS OCTOBER RAIN</h1>
        </div>
        <div class="mask"></div>
        <!-- <div class="info">
            <div class="time">
                {{ date.month }} {{ date.day }}, {{ date.year }}
            </div>
            <div class="title">
                欢迎光临！！
                <transition name="el-fade-in-linear">
                    <span v-show="!hiddenText" class="tipsText"
                        >请向下滚动</span
                    >
                </transition>
            </div>
            <div class="content">
                一个人知道自己为什么而活，就可以忍受任何一种生活。
            </div>
        </div> -->
        <div class="header">
            <div class="triangle" @click="triggerPage('/')"></div>
        </div>
    </div>
</template>

<script>
// import Parallax from "parallax-js"

export default {
    name: "Exhibit",
    data() {
        return {
            imgWidth: null,
            imgHeight: null,
            // hiddenText: false,
            // date: {},
        }
    },
    created() {
        let wWidth = document.documentElement.clientWidth
        let wHeight = document.documentElement.clientHeight
        this.imgWidth = wWidth + 150
        this.imgHeight = wHeight + 150
        // this.imgWidth = wWidth
        // this.imgHeight = wHeight
        if (wWidth <= 600) {
            this.imgWidth = 1920 / 1.3
            this.imgHeight = 960
        }
        // this.getYearMonthDay()
    },
    // mounted() {
        // this.hiddenTextEmit()
        // const scene = document.getElementById("scene")
        // const parallaxInstance = new Parallax(scene, {
        //     relativeInput: true,
        //     clipRelativeInput: true,
        // })
    // },
    methods: {
        // getYearMonthDay() {
        //     const date = new Date()
        //     this.date.year = date.getFullYear()
        //     this.date.month = date.getMonth() + 1
        //     this.date.day = date.getDate()
        //     // const result = `${year}-${month}-${day} ${123}`
        //     console.log(this.date)
        // },
        // hiddenTextEmit() {
        //     setTimeout(() => {
        //         this.hiddenText = true
        //     }, 3000)
        // },
        triggerPage(path){
            this.$router.push(path)
        }
    },
}
</script>

<style lang="stylus" scoped>
.exhibit
    width 100vw
    height 100vh
    overflow hidden
    position relative
    z-index 10
    .wrapper-img
        position relative
        overflow hidden
        // width 100%
        height 100%
        .inner-img
            position absolute
            max-width none
            display block
            margin-bottom 2rem
            top -3rem
            left 50%
            transform translateX(-50%)
    .solgan
        font-size 3.5rem
        position absolute
        top 0
        bottom 0
        left 0
        right 0
        height 100vh
        width 100vw
        h1
            position absolute
            margin 0
            top 0
            bottom 0
            left 0
            right 0
            line-height 100vh
            text-align center
            user-select none
        h1:first-child
            clip-path: polygon(0 0,100% 0,100% 30%,-65% 100%,0 100%);
        h1:last-child
            clip-path: polygon(100% 0,100% 100%,-65% 100%,100% 30%)

    .mask
        position absolute
        top 0
        left 0
        height 100%
        width 100%
        background-color: #00000086;
        clip-path: polygon(0 0,35% 0,70% 100%,0 100%);
        pointer-events: none;
    .header
        position absolute
        top 4rem
        left 3rem
        .triangle
            width: 0;
            height: 0;
            border: 1.4rem solid transparent;
            border-right: 2rem solid #aaa;
            border-radius .4rem
            cursor pointer
        .triangle:hover
            border: 1.4rem solid transparent;
            border-right: 2rem solid #fff;
            border-radius .4rem
</style>
