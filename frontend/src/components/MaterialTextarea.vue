<script>
import setMaterialInput from "@/assets/js/material-input.js";

export default {
  name: "MaterialTextarea",
  props: {
    variant: {
      type: String,
      default: "outline",
    },
    id: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      default: "",
    },
    value: {
      type: [String, Number],
      default: "",
    },
    placeholder: {
      type: String,
      default: "Your text here...",
    },
    isRequired: Boolean,
    isDisabled: {
      type: Boolean,
      default: false,
    },
    rows: {
      type: Number,
      default: 5,
    },
    success: {
      type: Boolean,
      default: false,
    },
    error: {
      type: Boolean,
      default: false,
    },
    label: {
      type: [String, Object],
      text: String,
      class: String,
      default: () => ({
        class: "",
      }),
    },
  },
  data() {
    return {
      inputValue: '',
    };
  },
  created() {
    this.inputValue = this.value;
  },
  mounted() {
    setMaterialInput();

    if (this.value) {
      this.emitChange();
    }
  },
  methods: {
    getStatus: (error, success) => {
      let isValidValue;

      if (success) {
        isValidValue = "is-valid";
      } else if (error) {
        isValidValue = "is-invalid";
      } else {
        isValidValue = null;
      }

      return isValidValue;
    },
    emitChange() {
      this.$emit('input-change', { name: this.name, value: this.inputValue });
    },
  },
};
</script>

<template>
  <div class="input-group"
    :class="[`input-group-${variant} ${getStatus(error, success)}`, inputValue ? 'is-filled' : '']">
    <label v-if="label" :class="[variant === 'static' ? '' : 'form-label', label.class]">
      {{ typeof label == "string" ? label : label.text }}
    </label>
    <textarea :name="name" :id="id" class="form-control" :rows="rows" v-model="inputValue" :placeholder="placeholder"
      :isRequired="isRequired" :disabled="isDisabled" @input="emitChange"></textarea>
  </div>
</template>
