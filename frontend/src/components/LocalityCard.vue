<script>
export default {
  name: 'LocalityCard',
  props: {
    city: {
      type: String,
      default: ''
    },
    state: {
      type: String,
      default: ''
    },
  },
}
</script>

<template>
  <div class="col-md-4 p-2">
    <div class="card p-3 text-start h-100">
      <h5 class="mt-3 font-weight-bolder">
        <i class="material-icons text-gradient text-primary text-3xl">share_location</i>
        {{ city }}
      </h5>
      <p class="text-sm font-weight-bold">{{ state }}</p>
    </div>
  </div>
</template>
