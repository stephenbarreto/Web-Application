<script>
import setMaterialInput from "@/assets/js/material-input";

export default {
  props: {
    variant: {
      type: String,
      default: "outline",
    },
    name: {
      type: String,
      default: "",
    },
    id: {
      type: String,
      default: "",
    },
    type: {
      type: String,
      default: "text",
    },
    label: {
      type: [String, Object],
      text: String,
      class: String,
      default: () => ({
        class: "",
      }),
    },
    value: {
      type: [String, Number],
      default: "",
    },
    placeholder: {
      type: String,
      default: "",
    },
    size: {
      type: String,
      default: "md",
    },
    error: {
      type: Boolean,
      default: false,
    },
    success: {
      type: Boolean,
      default: false,
    },
    isRequired: {
      type: Boolean,
      default: false,
    },
    isDisabled: {
      type: Boolean,
      default: false,
    },
    inputClass: {
      type: String,
      default: "",
    },
    icon: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      inputValue: '',
    };
  },
  methods: {
    getClasses(size, success, error) {
      let sizeValue, isValidValue;

      sizeValue = size && `form-control-${size}`;

      if (error) {
        isValidValue = "is-invalid";
      } else if (success) {
        isValidValue = "is-valid";
      } else {
        isValidValue = "";
      }

      return `${sizeValue} ${isValidValue}`;
    },
    emitChange() {
      this.$emit('input-change', { name: this.name, value: this.inputValue });
    },
  },
  created() {
    this.inputValue = this.value;
  },
  mounted() {
    setMaterialInput();

    if (this.value) {
      this.emitChange();
    }
  }
}
</script>

<template>
  <div class="input-group" :class="[(inputValue || type === 'date') ? 'is-filled' : '', `input-group-${variant}`]">
    <label v-if="label" :class="[variant === 'static' ? '' : 'form-label', label.class]">
      {{ typeof label == "string" ? label : label.text }}
    </label>
    <span v-if="icon" class="input-group-text"><i class="fas" :class="`fa-${icon}`" aria-hidden="true"></i></span>
    <input :name="name" :id="id" :type="type" class="form-control" :class="[getClasses(size, success, error), inputClass]"
      v-model="inputValue" :placeholder="placeholder" :isRequired="isRequired" :disabled="isDisabled"
      @input="emitChange" />
  </div>
</template>
