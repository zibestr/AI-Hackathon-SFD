<template>
  <Header />
</template>

<script>
import Header from "./components/Header.vue";

export default {
  name: "App",
  components: {
    Header,
  },
};
</script>

<style lang="scss">
#app {
  font-family: Inter;
  text-align: center;
  background-color: #edfffe;
  width: 100vw;
  height: 100vh;
}
</style>
