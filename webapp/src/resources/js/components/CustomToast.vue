<template>
  <Teleport to="body">
    <div ref="container" id="#custom-toast" :class="containerClass" v-bind="$attrs">
      <transition-group name="p-toast-message" tag="div" @enter="onEnter">
        <LoadingToastMessage
          v-for="msg of messages"
          :key="msg.id"
          :message="msg"
          @close="remove($event)"
        />
      </transition-group>
    </div>
  </Teleport>
</template>
<script>
import Toast from "primevue/toast/Toast.vue";
import LoadingToastMessage from "./LoadingToastMessage.vue";

export default {
  extends: Toast,
  components: {
    LoadingToastMessage,
  },
};
</script>
<style scoped>
.p-toast .p-toast-message.p-toast-message-success {
    background: #e4f8f0;
    border: none;
    color: #007bff!important;
}
.p-toast{
    background: #ffffff!important;
     color: #007bff!important;
     border:none!important;
}
.p-toast .p-toast-message .p-toast-icon-close {
    color: #007bff!important;
    }
.p-toast-message,.p-toast-message-content, .p-toast-message-success{
    background: #ffffff!important;
     color: #007bff!important;
}
.p-toast .p-toast-message.p-toast-message-success .p-toast-message-icon, .p-toast .p-toast-message.p-toast-message-success .p-toast-icon-close{
    color: #007bff!important;
}
.p-toast-icon-close{
    color: #007bff!important;
}
.p-toast-message-text{
    color: #007bff!important;
}
</style>