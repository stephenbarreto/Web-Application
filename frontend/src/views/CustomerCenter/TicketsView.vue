<script>
// componentes
import NavBar from '@/components/Navbars/NavBar.vue'
import SidebarNav from './components/SidebarNav.vue'
import MaterialButton from '@/components/MaterialButton.vue'
import ShowFile from '@/components/ShowFile.vue'

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
      tickets: [],
    }
  },
  methods: {
    getTickets() {
      api.get('cliente/boletos').then(response => {
        this.tickets = response.data;
      }).catch(e => console.error('Erro ao obter os boletos: ', e))
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
    getStatusName(status) {
      let statusName = ''

      switch (status) {
        case 0:
          statusName = 'Aguardando pagamento'
          break;
        case 1:
          statusName = 'Pago'
          break;
        case 2:
          statusName = 'Expirado'
          break;
      }
      return statusName;
    },
    formatDate(dateString) {
      // Verifica se a string de data está no formato 'YYYY-MM-DD'
      if (!/^\d{4}-\d{2}-\d{2}$/.test(dateString)) {
        console.error("Formato de data inválido. Use o formato 'YYYY-MM-DD'.");
        return null;
      }

      // Divide a string da data em partes (ano, mês, dia)
      const parts = dateString.split('-');
      const year = parseInt(parts[0]);
      const month = parseInt(parts[1]);
      const day = parseInt(parts[2]);

      // Cria um objeto Date com a data
      const dateObject = new Date(year, month - 1, day);

      // Formata a data para o padrão brasileiro ('DD/MM/YYYY')
      const formattedDate = dateObject.toLocaleDateString('pt-BR');

      return formattedDate;
    }
  },
  mounted() {
    this.getTickets();
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
                      <th class="text-center">Data de emissão</th>
                      <th class="text-center">Data de vencimento</th>
                      <th class="text-center">Status</th>
                      <th></th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(ticket, index) in tickets" :key="index">
                      <td>{{ ticket.signature.plan.name }}</td>
                      <td class="text-center">{{ formatDate(ticket.created_date) }}</td>
                      <td class="text-center">{{ formatDate(ticket.expire_date) }}</td>
                      <td class="text-center">{{ getStatusName(ticket.status) }}</td>
                      <td class="d-flex text-center">
                        <MaterialButton @click="showTicket(ticket.document)" color="warning" margin="mb-0 mx-1" size="sm"
                          icon="eye">
                          <span class="d-none d-md-block">Ver boleto</span>
                        </MaterialButton>
                      </td>
                    </tr>
                    <tr v-if="tickets.length === 0">
                      <td colspan="5">Não há boletos</td>
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
