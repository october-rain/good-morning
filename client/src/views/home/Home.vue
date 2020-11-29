<template>
    <div class="home">
        <home-bg>
            <home-header slot="info"></home-header>
            <home-foot slot="foot"></home-foot>
        </home-bg>
    </div>
</template>

<script>
import HomeHeader from "./components/HomeHeader"
import HomeBg from "./components/HomeBg"
import HomeFoot from "./components/HomeFoot"

export default {
    name: "",
    components: {
        HomeHeader,
        HomeBg,
        HomeFoot,
    },
}
</script>

<style lang="stylus" scoped></style>
