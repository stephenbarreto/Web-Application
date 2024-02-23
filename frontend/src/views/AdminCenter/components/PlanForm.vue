<script>
// componentes
import MaterialInput from '@/components/MaterialInput.vue';

import api from '@/services/api';

export default {
  name: 'LocalityForm',
  data() {
    return {
      formData: {
        benefits: []
      },
      benefits: [],
    }
  },
  props: {
    initialData: {
      type: Object,
      name: String,
      value: Number,
      default: () => ({ name: '', value: 0 })
    }
  },
  methods: {
    updateFormData({ name, value }) {
      this.formData[name] = value;
    },
    getFormData() {
      return this.formData;
    },
    getBenefits() {
      api.get('planos/beneficios/').then(response => {
        this.benefits = response.data;
      }).catch(e => console.error(e));
    }
  },
  components: {
    MaterialInput
  },
  created() {
    this.getBenefits()
  },
}
</script>

<template>
  <form action="">
    <MaterialInput id="name" class="input-group-outline my-3" :label="{ text: 'Nome', class: 'form-label' }" type="text"
      @input-change="updateFormData" name="name" :value="initialData.name" />
    <MaterialInput id="value" class="input-group-outline my-3" :label="{ text: 'Valor', class: 'form-label' }"
      type="number" @input-change="updateFormData" name="value" :value="initialData.value" />
    <div class="input-group input-group-static">
      <label for="planBenefits">Benefícios do Plano:</label>
      <select multiple id="planBenefits" v-model="formData.benefits" class="form-control">
        <option v-for="benefit in benefits" :key="benefit.id" :value="benefit.id">
          {{ benefit.name }}
        </option>
      </select>
    </div>
  </form>
</template>