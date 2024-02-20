<script>
// componentes
import NavBar from '@/components/Navbars/NavBar.vue'
import SidebarNav from './components/SidebarNav.vue'
import MaterialButton from '@/components/MaterialButton.vue'
import setMaterialInput from "@/assets/js/material-input";
import TicketForm from './components/TicketForm.vue';

import api from '@/services/api'
import Swal from 'sweetalert2'
import { createApp } from 'vue'

export default {
  components: {
    NavBar,
    SidebarNav,
    MaterialButton,
  },
  data() {
    return {
      signatures: [],
      search: '',
    }
  },
  methods: {
    setMaterialInput,
    getSignatures() {
      api.get('assinaturas/', {
        params: {
          username: this.search
        }
      }).then(response => {
        this.signatures = response.data;
      }).catch(e => console.error('Erro ao obter os assinaturas: ', e))
    },
    deleteSignature(id) {
      Swal.fire({
        title: 'Destaivar assinatura',
        text: 'Tem certeza de que deseja desativar a assinatura cliente?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        // cancelButtonColor: '',
        confirmButtonText: 'Sim, desativar!',
        cancelButtonText: 'Cancelar',
      }).then((result) => {
        if (result.isConfirmed) {
          api.delete(`assinaturas/deletar/${id}`).then(() => {
            this.getSignatures()
            Swal.fire('Desativado!', 'Assinatura desativado com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao desativar o assinatura: ', e)
          });
        }
      });
    },
    reactivateSignature(id) {
      Swal.fire({
        title: 'Reativar assinatura',
        text: 'Tem certeza de que deseja reativar a assinatura do cliente?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Sim, reativar!',
        cancelButtonText: 'Cancelar',
      }).then((result) => {
        if (result.isConfirmed) {
          api.put(`assinaturas/editar/${id}`, { 'is_active': true }).then(() => {
            this.getSignatures()
            Swal.fire('Reativado!', 'Assinatura reativada com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao reativar o assinatura: ', e)
          });
        }
      });
    },
    getTicketModal(signature) {
      // Criar um elemento div
      const div = document.createElement('div');
      // Montar o componente vue na div
      const form = createApp(TicketForm, { signature: signature }).mount(div);

      // Cria e exibe o modal sweet alert
      return Swal.fire({
        title: 'Novo Boleto',
        html: form.$el,
        focusConfirm: false,
        showCancelButton: true,
        preConfirm: () => {
          // Retorna os dados do form do componente Vue
          return form.getFormData();
        },
        onAfterClose: () => {
          // Destroi o componente após o fechamento do alerta
          form.$destroy();
        },
      })
    },
    createTicket(signature) {
      this.getTicketModal(signature).then(result => {
        if (result.isConfirmed) {
          api.post('boletos/criar', result.value, {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          }).then(() => {
            this.getSignatures();
            Swal.fire('Criado!', 'Boleto criado com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao criar o boleto: ', e)
          });
        }
      })
    },
  },
  mounted() {
    this.getSignatures();
    setMaterialInput();
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
          <div class="card card-body mb-5">
            <div class="input-group input-group-outline">
              <label class="form-label" for="search">Nome do usuário</label>
              <input type="text" name="search" id="search" class="form-control" v-model="search">
              <button @click="getSignatures" class="btn btn-primary m-0">pesquisar</button>
            </div>
          </div>
          <div class="card">
            <div class="card-body">
              <div class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th>Nome do cliente</th>
                      <th>Plano</th>
                      <th>Valor</th>
                      <th>Ativo</th>
                      <th></th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="signature in signatures" :key="signature.id">
                      <td>{{ signature.user.username }}</td>
                      <td>{{ signature.plan.name }}</td>
                      <td>R${{ signature.plan.value }}</td>
                      <td>{{ signature.is_active ? 'sim' : 'não' }}</td>
                      <td class="d-flex">
                        <MaterialButton v-if="signature.is_active" @click="deleteSignature(signature.id)" color="danger"
                          margin="mb-0 mx-1" size="sm" icon="user-times">
                          <span class="d-none d-md-block">Desativar</span>
                        </MaterialButton>
                        <MaterialButton v-else @click="reactivateSignature(signature.id)" color="success"
                          margin="mb-0 mx-1" size="sm" icon="user-check">
                          <span class="d-none d-md-block">Reativar</span>
                        </MaterialButton>
                        <MaterialButton @click="createTicket(signature)" color="success" margin="mb-0 mx-1" size="sm"
                          icon="plus">
                          <span class="d-none d-md-block">Nova Boleto</span>
                        </MaterialButton>
                      </td>
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
