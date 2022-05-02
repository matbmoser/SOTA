
<template>
  <div>
    <CustomToast />
    <CustomToast position="top-left" group="tl" />
    <CustomToast position="bottom-left" group="bl" />
    <CustomToast position="bottom-right" group="br" />

    <div class="card">
      <Button @click="test" label="test" />
    </div>
  </div>
</template>

<script>
import CustomToast from "./CustomToast.vue";
export default {
  components: {
    CustomToast,
  },
  data() {
    return {
      messages: [],
    };
  },
  methods: {
    test() {
      this.$toast.add({
        severity: "success",
        summary: "Test",
        detail: "<b>Test Bold</b>",
      });
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
