<template>
  <Teleport to="body">
    <div ref="container" :class="containerClass" v-bind="$attrs">
      <transition-group name="p-toast-message" tag="div" @enter="onEnter">
        <ErrorToastMessage
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
import ErrorToastMessage from "./ErrorToastMessage.vue";

export default {
  name: "ErrorToast", 
  extends: Toast,
  components: {
    ErrorToastMessage,
  },
};
</script>
<style scoped>

</style>