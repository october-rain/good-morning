<template>
    <div class="add-article">
        <div class="content">
            <input
                class="title"
                type="text"
                placeholder="标题"
                v-model="articleInfo.title"
            />
            <input
                class="desc"
                type="text"
                placeholder="描述"
                v-model="articleInfo.describe"
            />
            <!-- 这里如果不写组件的话，直接写在当前组件里，点击外侧关闭框的操作是无效的，所以网上有些人才会专门写一个组件出来啊。。。牛逼了 -->
            <tags @receiveTags="receiveTags"/>
            <!-- <div class="tag">
                <div class="tag-btn" @click="handleClickTag">
                    Tag
                </div>
                <div class="all-tag" v-show="isShow">
                    <ul v-for="bigtag in allTags" :key="bigtag.sortID">
                        {{
                            bigtag.sortname
                        }}
                        <li
                            v-for="smalltag in bigtag.tag_data"
                            :key="smalltag.tagID"
                            @click="handleClickLi(smalltag.tagID)"
                            :ref="'li' + smalltag.tagID"
                            :class="{ active: isInTags(smalltag.tagID) }"
                        >
                            {{ smalltag.tagname }}
                        </li>
                    </ul>
                </div>
            </div> -->
            <mark-down-editor @add="addContent"></mark-down-editor>
            <div class="button" @click="Submit">
                <svg class="svg">
                    <rect class="rectangle" />
                </svg>
                <div class="btn">Submit</div>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import MarkDownEditor from "./components/MarkDownEditor"
import Tags from "./components/Tags"
import axios from "axios"
import Qs from "qs"

export default {
    name: "AddArticle",
    data() {
        return {
            submitAble: true, // 是否能够发送，发送不能过快
            articleInfo: {
                title: "",
                describe: "",
                content: "",
                cover: "",
                token: "",
                tag: [],
            },
            // allTags: [],
            // isShow: false,
            // tags: [],
        }
    },
    components: {
        MarkDownEditor,
        Tags
    },
    // beforeMount() {
    //     this.getTag()
    // },
    // mounted() {
    //     document.addEventListener("click", (e) => {
    //         // console.log("e",e.target);
    //         // console.log("!this.$el.contains(e.target)",!this.$el.contains(e.target))
    //         if (!this.$el.contains(e.target)) this.isShow = false
    //     })
    // },
    methods: {
        addContent(content) {
            // console.log(content)
            this.articleInfo.content = content
            // console.log(this.articleInfo);
            this.articleInfo.token = localStorage.getItem("token")
        },
        Submit() {
            if (this.submitAble) {
                this.submitAble = false
                setTimeout(() => {
                    this.submitAble = true
                }, 2000)
                if (!this.articleInfo.title || !this.articleInfo.describe) {
                    alert("请输入标题和描述")
                } else if (!this.articleInfo.content) {
                    alert("请输入文章")
                } else {
                    axios({
                        url: "https://api.tian999.top/api/add-article/",
                        method: "POST",
                        data: Qs.stringify(this.articleInfo),
                    })
                        .then((res) => {
                            console.log("add-article 请求成功")
                            if (res.data === "repeat") {
                                alert("文章标题重复")
                            } else if (res.data === "ok") {
                                alert("文章添加成功")
                                window.location.reload()
                            }
                        })
                        .catch((err) => {
                            console.error(err)
                        })
                }
            } else {
                alert("等等在点击哦")
            }
        },
        // getTag() {
        //     axios.get("https://api.tian999.top/api/get-tag/").then((res) => {
        //         // console.log(res.data)
        //         this.allTags = res.data
        //     })
        // },
        // handleClickTag() {
        //     this.isShow = !this.isShow
        // },
        // handleClickLi(tagID) {
        //     if (this.isInTags(tagID)) {
        //         // console.log("do nothing")
        //         let index = this.tags.findIndex((item) => {
        //             if (item == tagID) return true
        //         })
        //         // console.log(index);
        //         this.tags.splice(index, 1)
        //     } else {
        //         this.tags.push(tagID)
        //     }
        //     // console.log("tag", this.tag)
        //     // console.log(this.isInTags(tagID))
        //     // console.log(tagID);
        //     // console.log(this.$refs[tagID]);
        //     // this.$refs.[tagID].style.color = 'red'
        // },

        // // 判断是否点击了tag（点击便会加入tag数组）
        // isInTags(tagID) {
        //     // return this.tags.indexOf(tagID) === -1 ? false : true
        //     let res = this.tags.some((item) => {
        //         // console.log("tagID", tagID)
        //         // console.log("item", item)
        //         if (item === tagID) {
        //             // console.log("success")
        //             return true
        //         } else {
        //             return false
        //         }
        //     })
        //     return res
        // },
        receiveTags(tags){
            this.articleInfo.tag = tags
        }
    },
}
</script>

<style lang="stylus" scoped>
.add-article
    height 100vh
    padding-top 10rem
    background #2e2e2e
    .content
        margin 0 auto
        max-width 76rem
        input
            font-size 1.4rem
            outline none
            width 16rem
            height 4rem
            margin 0 4rem 2rem 0
            border none
            border-radius 1rem
            text-indent 1rem
            background #eee
        .desc
            width 46rem
        .button
            margin 5rem auto 0
            position relative
            width 24rem
            height 6rem
            text-align center
            cursor pointer
            .svg
                width 24rem
                height 6rem
                .rectangle
                    width 24rem
                    height 6rem
                    stroke-width .8rem
                    stroke #ff6348
                    fill transparent
                    // /* Core part of the animation */
                    stroke-dasharray 100 500
                    stroke-dashoffset -372
            .btn
                text-transform uppercase
                color white
                font-size 2.4rem
                letter-spacing .5rem
                position: relative
                top: -4.6rem
        .button:hover .rectangle
            animation 0.5s extend linear forwards


@keyframes extend
    to
        stroke-dasharray 600
        stroke-dashoffset 0
        stroke-width 2

// .all-tag
//     grid-template-areas:
//         "two one"
//         "two three"
//         "two four";
</style>
