<script>
export default {
  name: 'MaterialButton',
  methods: {
    getVariant(variant, color) {
      let colorValue;

      // Setting the button variant and color
      if (variant === "gradient") {
        colorValue = `bg-gradient-${color}`;
      } else if (variant === "outline") {
        colorValue = `btn-outline-${color}`;
      } else {
        colorValue = `btn-${color}`;
      }

      return colorValue;
    }
  },
  props: {
    variant: {
      type: String,
      validator(variant) {
        return ["contained", "gradient", "outline"].includes(variant);
      },
      default: "contained",
    },
    color: {
      validator(color) {
        return [
          "primary",
          "secondary",
          "info",
          "success",
          "warning",
          "danger",
          "error",
          "light",
          "white",
          "dark",
          "none",
        ].includes(color);
      },
      default: "",
    },
    size: {
      validator(size) {
        return ["sm", "md", "lg"].includes(size);
      },
      default: "md",
    },
    fullWidth: {
      type: Boolean,
      default: false,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    margin: {
      type: String,
      default: 'm-0'
    },
    icon: {
      type: String,
      default: ''
    }
  }
};
</script>

<template>
  <button class="btn d-flex align-items-center"
    :class="[`btn-${size}`, { 'w-100': fullWidth, 'disabled': disabled }, getVariant(variant, color), margin]">
    <i v-if="icon" class="fa me-md-2 me-0 fs-6" :class="`fa-${icon}`"></i>
    <slot />
  </button>
</template>
