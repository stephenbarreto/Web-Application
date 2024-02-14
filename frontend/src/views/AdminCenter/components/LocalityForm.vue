<script>
import MaterialInput from '@/components/MaterialInput.vue';

export default {
  name: 'LocalityForm',
  data() {
    return {
      formData: {},
    }
  },
  props: {
    initialData: {
      type: Object,
      city: String,
      state: String,
      default: () => ({ city: '', state: '' })
    }
  },
  methods: {
    updateFormData({ name, value }) {
      this.formData[name] = value;
    },
    getFormData() {
      return this.formData;
    }
  },
  components: {
    MaterialInput
  },
  mounted() {
    
  }
}
</script>

<template>
  <form action="">
    <MaterialInput id="city" class="input-group-outline my-3" :label="{ text: 'Cidade', class: 'form-label' }" type="text"
      @input-change="updateFormData" name="city" :value="initialData.city" />
    <MaterialInput id="state" class="input-group-outline my-3" :label="{ text: 'Estado', class: 'form-label' }"
      type="text" @input-change="updateFormData" name="state" :value="initialData.state" />
  </form>
</template>