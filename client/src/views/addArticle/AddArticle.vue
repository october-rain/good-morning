<template>
    <div class="add-article">
        <div class="content">
            <input
                class="title"
                type="text"
                placeholder="标题"
                v-model="title"
            />
            <input class="desc" type="text" placeholder="描述" v-model="desc" />
            <img-upload @receiveImg="receiveImg" />
            <!-- 这里如果不写组件的话，直接写在当前组件里，点击外侧关闭框的操作是无效的，所以网上有些人才会专门写一个组件出来啊。。。牛逼了 -->
            <tags @receiveTags="receiveTags" />
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
import ImgUpload from "./components/ImgUpload"
import Tags from "./components/Tags"
import axios from "axios"
// import Qs from "qs"
export default {
    name: "AddArticle",
    data() {
        return {
            submitAble: true, // 是否能够发送，发送不能过快
            // articleInfo: {
            //     title: "",
            //     describe: "",
            //     content: "",
            //     cover: null,
            //     token: "",
            //     tag: [],
            // },
            title: "",
            desc: "",
            articleInfo: new FormData(),
            // allTags: [],
            // isShow: false,
            // tags: [],
        }
    },
    components: {
        MarkDownEditor,
        Tags,
        ImgUpload,
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
    // mounted() {
    //     console.log(this.articleInfo)
    // },
    methods: {
        addContent(content) {
            // console.log(content)
            // this.articleInfo.content = content
            if (this.articleInfo.get("content")) {
                this.articleInfo.set("content", content)
            } else {
                this.articleInfo.append("content", content)
            }
            // console.log(this.articleInfo);
            // this.articleInfo.token = localStorage.getItem("token")
        },
        Submit() {
            if (this.submitAble) {
                this.submitAble = false
                setTimeout(() => {
                    this.submitAble = true
                }, 2000)

                // formData添加数据
                this.articleInfo.append("token", localStorage.getItem("token"))
                this.articleInfo.append("title", this.title)
                this.articleInfo.append("desc", this.desc)
                // console.log(this.articleInfo)
                // console.log(this.articleInfo.get("title"))
                // console.log(this.articleInfo.get("desc"))
                // console.log(this.articleInfo.get("content"))
                // console.log(this.articleInfo.get("tag"))
                // console.log(this.articleInfo.get("cover"))
                // console.log(this.articleInfo.get("token"))

                if (
                    !this.articleInfo.get("title") ||
                    !this.articleInfo.get("desc")
                ) {
                    alert("请输入标题和描述")
                } else if (!this.articleInfo.get("content")) {
                    alert("请输入文章")
                } else {
                    // axios({
                    //     url: "https://api.tian999.top/api/add-article/",
                    //     method: "POST",
                    //     data: Qs.stringify(this.articleInfo, {
                    //         indices: false,
                    //     }),
                    // })
                    let config = {
                        headers: { "Content-Type": "multipart/form-data" },
                    }
                    axios
                        .post(
                            "https://api.tian999.top/api/add-article/",
                            this.articleInfo,
                            config
                        )
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
        receiveTags(tags) {
            // this.articleInfo.tag = JSON.stringify(tags)
            // console.log(typeof(this.articleInfo.tag));
            // console.log(tags)
            if (this.articleInfo.get("tag")) {
                this.articleInfo.set("tag", JSON.stringify(tags))
            } else {
                this.articleInfo.append("tag", JSON.stringify(tags))
            }
            // console.log(this.articleInfo.get("tag"))
        },
        receiveImg(imgs) {
            // console.log(typeof(imgs[0]));
            // console.log(imgs[0].name)
            // let imgSrc = this.getObjectURL(imgs[0])
            // console.log(imgSrc)

            // let formData = new FormData();

            if (this.articleInfo.get("cover")) {
                this.articleInfo.set("cover", imgs[0])
            } else {
                this.articleInfo.append("cover", imgs[0])
            }
            // console.log(formData.get("cover"));
            // this.articleInfo.cover = imgs
            // console.log(this.articleInfo);
            // console.log(typeof(this.articleInfo.cover));
            // console.log(
            //     this.articleInfo.get("cover"),
            //     this.articleInfo.get("content")
            // )
        },
        getObjectURL(file) {
            var url = null
            if (window.createObjectURL != undefined) {
                // basic
                url = window.createObjectURL(file)
            } else if (window.URL != undefined) {
                // mozilla(firefox)
                url = window.URL.createObjectURL(file)
            } else if (window.webkitURL != undefined) {
                // webkit or chrome
                url = window.webkitURL.createObjectURL(file)
            }
            return url
        },
    },
}
</script>

<style lang="stylus" scoped>
.add-article
    min-height 100vh
    height 100%
    padding-top 5vh
    padding-bottom 5vh
    background #2e2e2e
    .content
        height 100%
        margin 0 auto
        max-width 76rem
        input
            font-size 1.4rem
            outline none
            width 16rem
            height 4rem
            margin 0 2rem 2rem 0
            border none
            border-radius 1rem
            text-indent 1rem
            background #eee
        .desc
            width 42rem
            // width 30rem
        .button
            margin 4vh auto 0
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
