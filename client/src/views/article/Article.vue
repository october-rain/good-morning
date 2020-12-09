<template>
    <div class="article">
        <!-- header -->
        <main-body class="mainbody"></main-body>
        <!-- footer -->
    </div>
</template>

<script>
import MainBody from "./components/MainBody"

export default {
    name: "Article",
    components: {
        MainBody
    }
}
</script>

<style lang="stylus" scoped>
// .mainbody
//     max-width 60rem
//     margin 0 auto

</style>
