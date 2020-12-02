<template>
    <div class="addArticle">
        <input type="text" placeholder="标题" v-model="articleInfo.title" />
        <input type="text" placeholder="描述" v-model="articleInfo.desc" />
        <mark-down-editor @add="addContent"></mark-down-editor>
        <div class="button" @click="Submit">提交</div>
    </div>
</template>

<script>
// @ is an alias to /src
import MarkDownEditor from "./components/MarkDownEditor"
import axios from "axios"
import Qs from "qs"

export default {
    name: "AddArticle",
    data() {
        return {
            submitAble: true, // 是否能够发送，发送不能过快
            articleInfo: {
                title: "",
                desc: "",
                content: "",
            },
        }
    },
    components: {
        MarkDownEditor,
    },
    methods: {
        addContent(content) {
            // console.log(content)
            this.articleInfo.content = content
            // console.log(this.articleInfo);
        },
        Submit() {
            if (this.submitAble) {
                this.submitAble = false
                setTimeout(() => {
                    this.submitAble = true
                }, 2000)
                if (!this.articleInfo.title || !this.articleInfo.desc) {
                    alert("请输入标题和描述")
                } else if (!this.articleInfo.content) {
                    alert("请输入文章")
                } else {
                    axios({
                        url: "http://127.0.0.1:9000/api/add-article/",
                        method: "POST",
                        data: Qs.stringify(this.articleInfo),
                    })
                        .then((res) => {
                            console.log("add-article 请求成功");
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
    },
}
</script>

<style lang="stylus" scoped></style>
