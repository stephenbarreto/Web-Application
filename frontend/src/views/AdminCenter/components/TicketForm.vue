<script>
// componentes
import MaterialInput from '@/components/MaterialInput.vue';

export default {
  name: 'TicketForm',
  data() {
    return {
      formData: {
        expire_date: '',
        document: '',
      },
    }
  },
  props: {
    signature: Object,
  },
  methods: {
    getFormData() {
      return this.formData;
    },
    setFile(e) {
      this.formData.document = e.target.files[0];
    },
    formatDate({ value }) {
      // Converte a data para o formato 'YYYY-MM-DD'
      const date = new Date(value);
      const formattedDate = date.toISOString().split('T')[0];
      this.formData['expire_date'] = formattedDate;
    }
  },
  computed: {
    fileName() {
      return this.formData.file ? this.formData.file.name : 'Nenhum arquivo selecionado';
    },
  },
  components: {
    MaterialInput
  },
  mounted() {
    this.formData['signature'] = this.signature.id;
  }
}
</script>

<template>
  <form action="">
    <MaterialInput id="expire_date" class="input-group-outline my-3" name="expire_date"
      :label="{ text: 'Data de validade', class: 'form-label' }" type="date" @input-change="formatDate" />
    <div class="mt-3">
      <label for="document">Selecione um boleto:</label>
      <input type="file" id="document" ref="ContractInput" class="form-control" @change="setFile" />
    </div>
  </form>
</template>