<script>
export default {
  props: {
    file: File,
  }
}
</script>

<template>
  <div>
    <iframe :src="file" frameborder="0" class="w-100 min-vh-75"></iframe>
  </div>
</template>