<template>
  <div class="home">
    <Panel/>
    <img alt="Vue logo" style="height: 25em;" src="../assets/logo.png">
    <HelloWorld msg="Bienvenido a SOTA WebApp"/>
  </div>
</template>

<script>
  // @ is an alias to /src
  import HelloWorld from '../components/HelloWorld.vue'

  export default {
    name: 'Home',
    components: {
      HelloWorld
    }
  }
</script>
