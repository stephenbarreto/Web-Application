<script>
// componentes
import NavBar from '@/components/Navbars/NavBar.vue'
import SidebarNav from './components/SidebarNav.vue'
import TicketForm from './components/TicketForm.vue'
import MaterialButton from '@/components/MaterialButton.vue'
import ShowFile from '@/components/ShowFile.vue'
import MaterialInput from '@/components/MaterialInput.vue'

import api from '@/services/api'
import Swal from 'sweetalert2'
import { createApp } from 'vue'
import formatDate from '@/assets/js/utils'

export default {
  components: {
    NavBar,
    SidebarNav,
    MaterialButton,
    MaterialInput,
  },
  data() {
    return {
      tickets: [],
      query: {
        username: '',
        expireDate: '',
        createdDate: '',
      },
    }
  },
  methods: {
    formatDate,
    getLocalities() {
      api.get('boletos/').then(response => {
        this.tickets = response.data;
      }).catch(e => console.error('Erro ao obter as boletos: ', e))
    },
    getModal(initialData = {}) {
      // Criar um elemento div
      const div = document.createElement('div');
      // Montar o componente vue na div
      const form = createApp(TicketForm, { initialData: initialData }).mount(div);

      // Cria e exibe o modal sweet alert
      return Swal.fire({
        title: 'Preencha o formulário',
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
    editTicket(id, ticket) {
      const initialData = { city: ticket.city, state: ticket.state }

      this.getModal(initialData).then(result => {
        if (result.isConfirmed) {
          api.put(`boletos/editar/${id}`, result.value).then(() => {
            this.getLocalities();
            Swal.fire('Editada!', 'Boleto editada com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao editar o boleto: ', e)
          });
        }
      })
    },
    deleteTicket(id) {
      Swal.fire({
        title: 'Excluir localidade',
        text: 'Esta ação é irreversível. Tem certeza de que deseja excluir o boleto?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        // cancelButtonColor: '',
        confirmButtonText: 'Sim, excluir!',
        cancelButtonText: 'Cancelar',
      }).then((result) => {
        if (result.isConfirmed) {
          api.delete(`boletos/deletar/${id}`).then(() => {
            this.getLocalities()
            Swal.fire('Excluído!', 'Boleto deletada com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao deletar o boleto: ', e)
          });
        }
      });
    },
    showTicket(ticket) {
      // Criar um elemento div
      const div = document.createElement('div');
      // Montar o componente vue na div
      const form = createApp(ShowFile, { file: ticket }).mount(div);

      // Cria e exibe o modal sweet alert
      return Swal.fire({
        title: 'Boleto',
        html: form.$el,
        showCloseButton: true,
        showConfirmButton: false,
        customClass: {
          popup: 'w-100 w-md-70 w-lg-60 w-xl-50',
        },
        preConfirm: () => {
          // Retorna os dados do form do componente Vue
          return form.getFormData();
        },
      })
    },
    updateQuery({ name, value }) {
      this.query[name] = value
    },
  },
  mounted() {
    this.getLocalities();
  },
  computed: {
    filteredTickets() {
      let filteredTickets = this.tickets;

      if (this.query.username) {
        let query = this.query.username.toLowerCase()

        filteredTickets = filteredTickets.filter(ticket => {
          return ticket.signature.user.username.toLowerCase().includes(query)
        });
      }

      if (this.query.createdDate) {
        filteredTickets = filteredTickets.filter(ticket => {
          return ticket.created_date === this.query.createdDate;
        });
      }

      if (this.query.expireDate) {
        filteredTickets = filteredTickets.filter(ticket => {
          return ticket.expire_date === this.query.expireDate;
        });
      }

      return filteredTickets;
    }
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
          <div class="card mb-4">
            <div class="card-body">
              <div class="row">
                <div class="col-md-4">
                  <MaterialInput id="username" variant="outline" :label="{ text: 'Filtrar por nome do cliente' }"
                    type="text" name="username" @input-change="updateQuery" placeholder="Nome do cliente" />
                </div>
                <div class="col-md-4">
                  <MaterialInput id="createdDate" variant="outline" :label="{ text: 'Filtrar por data de emissão' }"
                    type="date" name="createdDate" @input-change="updateQuery" placeholder="Nome do cliente" />
                </div>
                <div class="col-md-4">
                  <MaterialInput id="expireDate" variant="outline" :label="{ text: 'Filtrar por data de vencimento' }"
                    type="date" name="expireDate" @input-change="updateQuery" placeholder="Nome do cliente" />
                </div>
              </div>
            </div>
          </div>
          <div class="card">
            <div class="card-body">
              <div class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th>Cliente</th>
                      <th class="text-center">Data de emissão</th>
                      <th class="text-center">Data de vencimento</th>
                      <th></th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(ticket, index) in filteredTickets" :key="index">
                      <td>{{ ticket.signature.user.username }}</td>
                      <td class="text-center">{{ formatDate(ticket.created_date) }}</td>
                      <td class="text-center">{{ formatDate(ticket.expire_date) }}</td>
                      <td class="d-flex text-center">
                        <MaterialButton @click="editTicket(ticket.id, ticket)" color="warning" margin="mb-0 mx-1"
                          size="sm" icon="pen">
                          <span class="d-none d-md-block">editar</span>
                        </MaterialButton>
                        <MaterialButton @click="deleteTicket(ticket.id)" color="danger" margin="mb-0 mx-1" size="sm"
                          icon="trash">
                          <span class="d-none d-md-block">deletar</span>
                        </MaterialButton>
                        <MaterialButton @click="showTicket(ticket.document)" color="info" margin="mb-0 mx-1" size="sm"
                          icon="eye">
                          <span class="d-none d-md-block">Ver boleto</span>
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

<style scoped>
input {
  width: 100%;
}
</style>