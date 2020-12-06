<template>
    <div class="home">
        <home-bg>
            <home-header slot="header"></home-header>
            <home-info slot="info"></home-info>
            <home-foot slot="foot"></home-foot>
        </home-bg>
    </div>
</template>

<script>
import HomeHeader from "./components/HomeHeader"
import HomeInfo from "./components/HomeInfo"
import HomeBg from "./components/HomeBg"
import HomeFoot from "./components/HomeFoot"

export default {
    name: "",
    components: {
        HomeHeader,
        HomeBg,
        HomeFoot,
        HomeInfo
    },
}
</script>

<style lang="stylus" scoped></style>
