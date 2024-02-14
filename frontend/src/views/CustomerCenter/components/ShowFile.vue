<script>
export default {
  props: {
    file: File,
  }
}
</script>

<template>
  <div>
    {{ file }}
    <iframe :src="file" frameborder="0"></iframe>
  </div>
</template>