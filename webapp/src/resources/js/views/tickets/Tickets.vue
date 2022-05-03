
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
import CustomToast from "../../components/toasts/LoadingToast.vue";
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
      this.$toast.add({severity:"success", summary:"Please Wait...", detail: "<h3>Loading Content...</h3>"});
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
