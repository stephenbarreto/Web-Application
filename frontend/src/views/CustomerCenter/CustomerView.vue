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
      signatures: [],
    }
  },
  methods: {
    getSignatures() {
      api.get('cliente/assinaturas').then(response => {
        this.signatures = response.data;
      }).catch(e => console.error('Erro ao obter as assinaturas: ', e))
    },
    showSignature() {
      alert('O contrato apareceria em um modal');
    }
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
          <div class="card col-md-4">
            <div class="card-header p-3 pt-2">
              <div
                class="icon icon-lg icon-shape bg-gradient-primary shadow-primary shadow text-center border-radius-xl mt-n4 position-absolute">
                <i class="material-icons opacity-10">assignment</i>
              </div>
              <div class="text-end pt-1">
                <p class="text-sm mb-0 text-capitalize">Minhas assinaturas</p>
                <h4 class="mb-0">{{ signatures.length }}</h4>
              </div>
            </div>
            <hr class="dark horizontal my-0">
            <div class="card-footer p-3">
              <router-link :to="{ name: 'signatures' }" class="btn btn-sm btn-primary m-0 float-end">
                detalhes
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
