<script>
export default {
  props: {
    color: {
      type: String,
      default: 'bg-primary'
    },
    iconType: {
      type: String,
      default: 'fa'
    },
    icon: {
      type: String,
      default: 'fa-info'
    },
    iconColor: {
      type: String,
      default: 'text-light'
    },
    action: {
      type: String,
      default: '#'
    }
  }
}
</script>

<template>
  <a class="fixed-plugin-button position-fixed d-flex justify-content-center align-items-center shadow-danger"
    title="Filtrar currículos" style="width: 4rem; height: 4rem;" :class="[color, iconColor]" :href="action">
    <i class="fa-xl py-2" :class="[iconType, icon]" aria-hidden="true"></i>
  </a>
</template>
