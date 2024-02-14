<script>
import MaterialInput from '@/components/MaterialInput.vue';
import api from '@/services/api';

export default {
  name: 'SignatureForm',
  data() {
    return {
      formData: {
        plan: 0,
        contract: '',
      },
      plans: []
    }
  },
  props: {
    user: Object,
  },
  methods: {
    getFormData() {
      return this.formData;
    },
    getPlans() {
      api.get('planos/').then(response => {
        this.plans = response.data;
      }).catch(e => console.error(e));
    },
    setFile(e) {
      this.formData.contract = e.target.files[0];
    },
    computed: {
      fileName() {
        return this.formData.file ? this.formData.file.name : 'Nenhum arquivo selecionado';
      },
    },
  },
  components: {
    MaterialInput
  },
  mounted() {
    this.getPlans();
    this.formData['user'] = this.user.id;
  }
}
</script>

<template>
  <form action="">
    <MaterialInput id="username" class="input-group-outline my-3" :label="{ text: 'Usuário', class: 'form-label' }"
      type="text" name="username" :value="user.username" isDisabled="true" />
    <div class="input-group input-group-static">
      <label for="planBenefits">Plano:</label>
      <select id="plan" v-model="formData.plan" class="form-control">
        <option v-for="plan in plans" :key="plan.id" :value="plan.id">
          {{ plan.name }}
        </option>
      </select>
    </div>
    <div class="mt-3">
      <label for="contract">Selecione um contrato:</label>
      <input type="file" id="contract" ref="ContractInput" class="form-control" @change="setFile" />
    </div>
  </form>
</template>