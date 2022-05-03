<template>
<div style="height:100%">
  <div class="main-container" style="text-align: center">
    <p><em class="pi pi-exclamation-triangle" style="font-size: 10rem; color:#ffc107;"></em></p>
    <h3>Error 404: Not Found.</h3> <br/> <span style="font-size:2rem;"> <strong>Oops...</strong> ¡La página que buscas no existe!</span>
  </div>
</div>
</template>
<script>
export default {
  name: "NotFoundPage"
}
</script>

<style scoped>
.main-container{
    display:flex;
    flex-direction: column;
    justify-content: center;
    height:100vh;
}
</style>