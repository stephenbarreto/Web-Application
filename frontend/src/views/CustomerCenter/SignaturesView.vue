<script>
// componentes
import NavBar from '@/components/Navbars/NavBar.vue'
import SidebarNav from './components/SidebarNav.vue'
import MaterialButton from '@/components/MaterialButton.vue'
import ShowFile from './components/ShowFile.vue'

import api from '@/services/api'
import Swal from 'sweetalert2'
import { createApp } from 'vue'

export default {
  components: {
    NavBar,
    SidebarNav,
    MaterialButton
  },
  data() {
    return {
      signatures: [],
    }
  },
  methods: {
    getSignatures() {
      api.get('cliente/assinaturas').then(response => {
        this.signatures = response.data;
      }).catch(e => console.error('Erro ao obter as assinaturas: ', e))
    },
    showContract(contract) {
      // Criar um elemento div
      const div = document.createElement('div');
      // Montar o componente vue na div
      const form = createApp(ShowFile, { file: contract }).mount(div);

      // Cria e exibe o modal sweet alert
      return Swal.fire({
        title: 'Novo Cliente',
        html: form.$el,
        focusConfirm: false,
        showCancelButton: true,
        preConfirm: () => {
          // Retorna os dados do form do componente Vue
          return form.getFormData();
        },
      })
    },
  },
  mounted() {
    this.getSignatures();
  }
}
</script>

<template>
  <SidebarNav />
  <main class="main-content position-relative max-height-vh-100 h-100 overflow-x-hidden">
    <NavBar />
    <div class="container-fluid mt-5">
      <div class="row justify-content-center">
        <div class="col-md-11">
          <div class="card">
            <div class="card-body">
              <div class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th>Plano</th>
                      <th>Valor</th>
                      <th>status</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(signature, index) in signatures" :key="index">
                      <td>{{ signature.plan.name }}</td>
                      <td>R${{ signature.plan.value }}</td>
                      <td>{{ signature.is_active ? ativo : inativo }}</td>
                      <td class="d-flex">
                        {{ signature }}
                        <MaterialButton @click="showContract(signature.contract)" color="warning" margin="mb-0 mx-1"
                          size="sm" icon="eye">
                          <span class="d-none d-md-block">Ver contrato</span>
                        </MaterialButton>
                      </td>
                    </tr>
                    <tr v-if="signatures.length === 0">
                      <td colspan="5">Não há assinaturas</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
