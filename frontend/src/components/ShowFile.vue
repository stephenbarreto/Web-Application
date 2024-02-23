<script>
export default {
  props: {
    file: String,
  },
  mounted() {
    const spinner = this.$refs.spinner;
    const iframe = this.$refs.iframe;

    spinner.classList.remove('d-none');
    iframe.classList.add('d-none');

    iframe.addEventListener('load', function () {
      spinner.classList.add('d-none');
      iframe.classList.remove('d-none');
    });
  },
}
</script>

<template>
  <div>
    <div class="spinner-container w-100 min-vh-75 d-flex justify-content-center align-items-center d-none" ref="spinner">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
    <iframe :src="file" frameborder="0" class="w-100 min-vh-75" id="fileIframe" ref="iframe">
    </iframe>
  </div>
</template>