<script>
// componentes
import MaterialInput from '@/components/MaterialInput.vue';

export default {
  name: 'UserForm',
  data() {
    return {
      formData: {},
    }
  },
  props: {
    initialData: {
      type: Object,
      name: String,
      email: Number,
      default: () => ({ name: '', email: '' })
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
}
</script>

<template>
  <form action="">
    <MaterialInput id="username" class="input-group-outline my-3" :label="{ text: 'Nome', class: 'form-label' }"
      type="text" @input-change="updateFormData" name="username" :value="initialData.name" />
    <MaterialInput id="email" class="input-group-outline my-3" :label="{ text: 'Email', class: 'form-label' }"
      type="email" @input-change="updateFormData" name="email" :value="initialData.email" />
    <MaterialInput id="email" class="input-group-outline my-3" :label="{ text: 'Senha', class: 'form-label' }" type="text"
      @input-change="updateFormData" name="password" />
  </form>
</template>