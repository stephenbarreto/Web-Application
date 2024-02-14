<script>
// componentes
import NavBar from '@/components/Navbars/NavBar.vue'
import SidebarNav from './components/SidebarNav.vue'
import MaterialButton from '@/components/MaterialButton.vue'

import api from '@/services/api'

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
    showTicket() {
      alert('O boleto apareceria em um modal');
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
                      <th>Data de emissão</th>
                      <th>Data de vencimento</th>
                      <th>Status</th>
                      <th></th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(ticket, index) in tickets" :key="index">
                      <td>{{ ticket.plan.name }}</td>
                      <td>{{ ticket.created_date }}</td>
                      <td>{{ ticket.expire_date }}</td>
                      <td>{{ ticket.status }}</td>
                      <td class="d-flex">
                        <MaterialButton @click="showTicket" color="warning" margin="mb-0 mx-1" size="sm" icon="eye">
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
