<template>
    <div class="img-upload">
        <div class="upload-btn" @click="handleClickUpload">Img</div>
        <input type="file" name="file" accept="image/*" ref="upload" class="upload-input" @change="handleCLickInput($event)"/>
    </div>
</template>

<script>
// @ is an alias to /src

export default {
    name: "ImgUpload",
    data() {
        return {
            file: []
        }
    },
    methods: {
        handleClickUpload(){
            this.$refs.upload.click()
        },
        handleCLickInput(e){
            this.file = e.target.files
            // console.log(this.file);
            this.$emit("receiveImg",e.target.files)
        }
    },
}
</script>

<style lang="stylus" scoped>
.img-upload
    position relative
    display inline-block
    .upload-btn 
        background #eee
        height 4rem
        line-height 4rem
        width 4rem
        text-align center
        border-radius 2rem
        font-size 1.4rem
        margin-left 2rem
        cursor pointer
    input 
        display none

</style>
