<template>
  <div
    :class="containerClass"
    role="alert"
    aria-live="assertive"
    aria-atomic="true"
  >
    <div class="p-toast-message-fixed-blue p-toast-message-content">

      <span><ProgressSpinner/></span>
      <div class="p-toast-message-text-blue">
        <span class="p-toast-summary">{{ message.summary }}</span>
        <div class="p-toast-detail" v-html="message.detail"></div>
      </div>
    </div>
  </div>
</template>

<script>
import ToastMessage from "primevue/toast/ToastMessage.vue";
import ProgressSpinner from 'primevue/progressspinner';
export default {
  extends: ToastMessage,
  components:{
      "ProgressSpinner": ProgressSpinner
  }
};
</script>
<style>
.p-toast-message-fixed-blue{
      color: #007bff!important;
    height: 7em!important;
    display: flex!important;
    flex-direction: column!important;
    align-items: center!important;
    justify-content: center!important;
    height: fit-content!important;
}
.p-toast-message-text-blue{
    color: #007bff!important;
    display: flex!important;
    flex-direction: column!important;
    align-items: center!important;
    justify-content: center!important;
}

</style>