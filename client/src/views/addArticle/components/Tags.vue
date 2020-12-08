<template>
    <div class="tag">
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
    </div>
</template>

<script>
import axios from "axios"

export default {
    name: "Tags",
    data() {
        return {
            allTags: [],
            isShow: false,
            tags: [],
        }
    },
    beforeMount() {
        this.getTag()
    },
    watch: {
        isShow: function(newVal){
            if(newVal === false){
                // console.log("newVal === true");
                // console.log(this.tags);
                this.$emit("receiveTags",this.tags)
            }
        }
    },
    mounted() {
        document.addEventListener("click", (e) => {
            // console.log("e",e.target);
            // console.log("!this.$el.contains(e.target)",!this.$el.contains(e.target))
            if (!this.$el.contains(e.target)) {
                this.isShow = false
                // this.$emit("receiveTags",this.tags)
            }
        })
    },
    methods: {
        getTag() {
            axios.get("https://api.tian999.top/api/get-tag/").then((res) => {
                // console.log(res.data)
                this.allTags = res.data
            })
        },
        handleClickTag() {
            this.isShow = !this.isShow
        },
        handleClickLi(tagID) {
            if (this.isInTags(tagID)) {
                // console.log("do nothing")
                let index = this.tags.findIndex((item) => {
                    if (item == tagID) return true
                })
                // console.log(index);
                this.tags.splice(index, 1)
            } else {
                // console.log("do push")
                this.tags.push(tagID)
                // console.log(this.tags);
            }
            // console.log("tag", this.tag)
            // console.log(this.isInTags(tagID))
            // console.log(tagID);
            // console.log(this.$refs[tagID]);
            // this.$refs.[tagID].style.color = 'red'
        },

        // 判断是否点击了tag（点击便会加入tag数组）
        isInTags(tagID) {
            // return this.tags.indexOf(tagID) === -1 ? false : true
            let res = this.tags.some((item) => {
                // console.log("tagID", tagID)
                // console.log("item", item)
                if (item === tagID) {
                    // console.log("success")
                    return true
                } else {
                    return false
                }
            })
            return res
        },
    },
}
</script>

<style lang="stylus" scoped>
.tag
    position relative
    display inline-block
    .tag-btn
        background #eee
        height 4rem
        line-height 4rem
        width 4rem
        text-align center
        border-radius 2rem
        font-size 1.4rem
        margin-left 2rem
        cursor pointer
    .all-tag
        background #aaa
        border-radius 2rem
        z-index 10
        position absolute
        top 5.8rem
        right -5.5rem
        display grid
        grid-template-columns repeat(2, 8rem)
        grid-template-areas "two one" "two three" "two four"
        text-align center
        for row in 1 2 3 4
            ul:nth-child({row})
                if row == 1
                    grid-area one
                if row == 2
                    grid-area two
                if row == 3
                    grid-area three
                if row == 4
                    grid-area four
        ul
            // width 25%
            font-size 1.8rem
            padding-inline-start 0
            // background red
            li
                font-size 1.2rem
                line-height 1.5
                cursor pointer
            li:first-child
                padding-top 1rem
            .active
                color red
</style>
