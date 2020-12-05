<template>
    <div class="profile">
        <profile-header></profile-header>
        <profile-body></profile-body>
    </div>
</template>

<script>
import ProfileHeader from "./components/ProfileHeader"
import ProfileBody from "./components/ProfileBody"

export default {
    name: "Profile",
    components: {
        ProfileHeader,
        ProfileBody
    }
}
</script>

<style lang="stylus" scoped></style>
