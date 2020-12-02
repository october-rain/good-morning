<template>
    <div class="bg">
        <slot name="info"></slot>
        <slot name="foot"></slot>
    </div>
</template>

<script>
// @ is an alias to /src

export default {
    name: "HomeBg",
}
</script>

<style lang="stylus" scoped>
.bg 
    position relative
    height 100vh
    background #333aaa

</style>
