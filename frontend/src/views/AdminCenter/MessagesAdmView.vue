<script>
// componentes
import NavBar from '@/components/Navbars/NavBar.vue'
import SidebarNav from './components/SidebarNav.vue'

import api from '@/services/api'

export default {
  components: {
    NavBar,
    SidebarNav,
  },
  data() {
    return {
      messages: [],
      showRead: false,
    }
  },
  methods: {
    getMessages() {
      api.get('mensagens/').then(response => {
        this.messages = response.data;
      }).catch(e => console.error('Erro ao obter as mensagens: ', e))
    },
    markAsReaded(messageId) {
      api.delete(`mensagens/deletar/${messageId}`).then(() => {
        this.getMessages();
      }).catch(e => console.error('Erro ao obter as mensagens: ', e))
    }
  },
  mounted() {
    this.getMessages();
  },
  computed: {
    filteredMessages() {
      if (this.showRead) {
        // Mostrar apenas os itens não lidos
        return this.messages.filter(message => !message.is_readed);
      } else {
        // Mostrar todos os itens
        return this.messages;
      }
    },
  },
}
</script>

<template>
  <SidebarNav />
  <main class="ma'in-content position-relative max-height-vh-100 h-100 overflow-x-hidden">
    <NavBar />
    <div class="container-fluid mt-5">
      <div class="row justify-content-center">
        <div class="col-md-11">
          <div class="card card-body mb-4">
            <label>
              <input type="checkbox" v-model="showRead" /> Mostrar apenas não lidas
            </label>
          </div>
          <div v-for="(message, index) in filteredMessages" :key="index" class="card card-body mb-4">
            <h5 class="text-dark font-weight-bold mb-0">
              {{ message.email }}
            </h5>
            <p class="mt-1 mb-0">{{ message.created_date }}</p>
            <p class="text-dark mt-3 mb-2 text-lg">{{ message.description }}</p>
            <div v-if="!message.is_readed">
              <button class="btn btn-sm btn-primary m-0 float-end" @click="markAsReaded(message.id)">
                Marcar comolida
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
