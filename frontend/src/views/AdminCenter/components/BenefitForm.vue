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
      name: String,
      description: String,
      default: () => ({ name: '', description: '' })
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
    <MaterialInput id="name" class="input-group-outline my-3" :label="{ text: 'Nome', class: 'form-label' }" type="text"
      @input-change="updateFormData" name="name" :value="initialData.name" />
    <MaterialInput id="description" class="input-group-outline my-3" :label="{ text: 'Descrição', class: 'form-label' }"
      type="text" @input-change="updateFormData" name="description" :value="initialData.description" />
  </form>
</template>