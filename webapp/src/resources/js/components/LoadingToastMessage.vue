<template>
  <div
    :class="containerClass"
    role="alert"
    aria-live="assertive"
    aria-atomic="true"
  >
    <div class="p-toast-message-content">
      <span><ProgressSpinner/></span>
      <div class="p-toast-message-text">
        <span class="p-toast-summary">{{ message.summary }}</span>
        <div class="p-toast-detail" v-html="message.detail"></div>
      </div>
      <button
        class="p-toast-icon-close p-link"
        @click="onCloseClick"
        v-if="message.closable !== false"
        type="button"
        style="color: #007bff!important;"
        v-ripple
      >
        <span class="p-toast-icon-close-icon pi pi-times"></span>
      </button>
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
