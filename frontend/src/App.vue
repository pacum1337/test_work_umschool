<template>
  <div class="container">
    <nav-and-logout></nav-and-logout>
    <router-view></router-view>
  </div>
</template>

<script>
import NavAndLogout from "@/components/NavAndLogout";
export default {
  components: {
    NavAndLogout
  }
}
</script>

<style>

</style>
