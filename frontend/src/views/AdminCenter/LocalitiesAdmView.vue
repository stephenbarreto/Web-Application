<script>
// componentes
import NavBar from '@/components/Navbars/NavBar.vue'
import SidebarNav from './components/SidebarNav.vue'
import LocalityForm from './components/LocalityForm.vue'
import MaterialButton from '@/components/MaterialButton.vue'

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
      localities: [],
    }
  },
  methods: {
    getLocalities() {
      api.get('localidades/').then(response => {
        this.localities = response.data;
      }).catch(e => console.error('Erro ao obter as localidades: ', e))
    },
    getModal(initialData = {}) {
      // Criar um elemento div
      const div = document.createElement('div');
      // Montar o componente vue na div
      const form = createApp(LocalityForm, { initialData: initialData }).mount(div);

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
    createLocality() {
      this.getModal().then(result => {
        if (result.isConfirmed) {
          api.post('localidades/criar', result.value).then(() => {
            this.getLocalities();
            Swal.fire('Criada!', 'Localidade criada com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao criar a localidade: ', e)
          });
        }
      })
    },
    editLocality(id, locality) {
      const initialData = { city: locality.city, state: locality.state }

      this.getModal(initialData).then(result => {
        if (result.isConfirmed) {
          api.put(`localidades/editar/${id}`, result.value).then(() => {
            this.getLocalities();
            Swal.fire('Editada!', 'Localidade editada com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao editar a localidade: ', e)
          });
        }
      })
    },
    deleteLocality(id) {
      Swal.fire({
        title: 'Excluir localidade',
        text: 'Esta ação é irreversível. Tem certeza de que deseja excluir a localidade?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        // cancelButtonColor: '',
        confirmButtonText: 'Sim, excluir!',
        cancelButtonText: 'Cancelar',
      }).then((result) => {
        if (result.isConfirmed) {
          api.delete(`localidades/deletar/${id}`).then(() => {
            this.getLocalities()
            Swal.fire('Excluído!', 'Localidade deletada com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao deletar a localidade: ', e)
          });
        }
      });
    }
  },
  mounted() {
    this.getLocalities();
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
            <div class="d-flex">
              <button class="btn btn-success btn-md ms-4 mt-n3 border-radius-xl" @click="createLocality">
                <i class="fa fa-plus ms-0 me-2"></i>Nova localidade
              </button>
            </div>
            <div class="card-body">
              <div class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th>Cidade</th>
                      <th>Estado</th>
                      <th></th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(locality, index) in localities" :key="index">
                      <td>{{ locality.city }}</td>
                      <td>{{ locality.state }}</td>
                      <td class="d-flex">
                        <MaterialButton @click="editLocality(locality.id, locality)" color="warning" margin="mb-0 mx-1"
                          size="sm" icon="pen">
                          <span class="d-none d-md-block">editar</span>
                        </MaterialButton>
                        <MaterialButton @click="deleteLocality(locality.id)" color="danger" margin="mb-0 mx-1" size="sm"
                          icon="trash">
                          <span class="d-none d-md-block">deletar</span>
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
