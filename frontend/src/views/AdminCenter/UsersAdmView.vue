<script>
// componentes
import NavBar from '@/components/Navbars/NavBar.vue'
import SidebarNav from './components/SidebarNav.vue'
import UserForm from './components/UserForm.vue'
import MaterialButton from '@/components/MaterialButton.vue'
import setMaterialInput from "@/assets/js/material-input";
import SignatureForm from './components/SignatureForm.vue';

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
      users: [],
      search: '',
    }
  },
  methods: {
    setMaterialInput,
    getUsers() {
      api.get('usuarios/', {
        params: {
          username: this.search
        }
      }).then(response => {
        this.users = response.data;
      }).catch(e => console.error('Erro ao obter os usuários: ', e))
    },
    getModal(initialData = {}) {
      // Criar um elemento div
      const div = document.createElement('div');
      // Montar o componente vue na div
      const form = createApp(UserForm, { initialData: initialData }).mount(div);

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
        // onAfterClose: () => {
        //   // Destroi o componente após o fechamento do alerta
        //   form.$destroy();
        // },
      })
    },
    getSignatureModal(user) {
      // Criar um elemento div
      const div = document.createElement('div');
      // Montar o componente vue na div
      const form = createApp(SignatureForm, { user: user }).mount(div);

      // Cria e exibe o modal sweet alert
      return Swal.fire({
        title: 'Nova Assinatura',
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
    createUser() {
      this.getModal().then(result => {
        if (result.isConfirmed) {
          api.post('usuarios/registrar', result.value).then(() => {
            this.getUsers();
            Swal.fire('Criado!', 'Cliente criado com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao criar o cliente: ', e)
          });
        }
      })
    },
    createSignature(user) {
      this.getSignatureModal(user).then(result => {
        if (result.isConfirmed) {
          api.post('assinaturas/criar', result.value, {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          }).then(() => {
            this.getUsers();
            Swal.fire('Criada!', 'Assinatura criada com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao criar a assinatura: ', e)
          });
        }
      })
    },
    editUser(id, user) {
      const initialData = { name: user.username, email: user.email }

      this.getModal(initialData).then(result => {
        if (result.isConfirmed) {
          api.put(`usuarios/editar/${id}`, result.value).then(() => {
            this.getUsers();
            Swal.fire('Editado!', 'Cliente editado com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao editar o cliente: ', e)
          });
        }
      })
    },
    deleteUser(id) {
      Swal.fire({
        title: 'Destaivar cliente',
        text: 'Tem certeza de que deseja desativar o cliente?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        // cancelButtonColor: '',
        confirmButtonText: 'Sim, desativar!',
        cancelButtonText: 'Cancelar',
      }).then((result) => {
        if (result.isConfirmed) {
          api.delete(`usuarios/deletar/${id}`).then(() => {
            this.getUsers()
            Swal.fire('Desativado!', 'Cliente desativado com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao desativar o cliente: ', e)
          });
        }
      });
    },
    reactivateUser(id) {
      Swal.fire({
        title: 'Reativar cliente',
        text: 'Tem certeza de que deseja reativar o cliente?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Sim, reativar!',
        cancelButtonText: 'Cancelar',
      }).then((result) => {
        if (result.isConfirmed) {
          api.put(`usuarios/editar/${id}`, { 'is_active': true }).then(() => {
            this.getUsers()
            Swal.fire('Reativado!', 'Cliente reativado com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao reativar o cliente: ', e)
          });
        }
      });
    }
  },
  mounted() {
    this.getUsers();
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
              <button @click="getUsers" class="btn btn-primary m-0">pesquisar</button>
            </div>
          </div>
          <div class="card">
            <div class="d-flex">
              <button class="btn btn-success btn-md ms-4 mt-n3 border-radius-xl" @click="createUser">
                <i class="fa fa-plus ms-0 me-2"></i>Novo Cliente
              </button>
            </div>
            <div class="card-body">
              <div class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th>Nome</th>
                      <th>E-mail</th>
                      <th>Ativo</th>
                      <th></th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="user in users" :key="user.id">
                      <td>{{ user.username }}</td>
                      <td>{{ user.email }}</td>
                      <td>{{ user.is_active ? 'sim' : 'não' }}</td>
                      <td class="d-flex">
                        <MaterialButton @click="editUser(user.id, user)" color="warning" margin="mb-0 mx-1" size="sm"
                          icon="pen">
                          <span class="d-none d-md-block">editar</span>
                        </MaterialButton>
                        <MaterialButton v-if="user.is_active" @click="deleteUser(user.id)" color="danger"
                          margin="mb-0 mx-1" size="sm" icon="user-times">
                          <span class="d-none d-md-block">Desativar</span>
                        </MaterialButton>
                        <MaterialButton v-else @click="reactivateUser(user.id)" color="success" margin="mb-0 mx-1"
                          size="sm" icon="user-check">
                          <span class="d-none d-md-block">Reativar</span>
                        </MaterialButton>
                        <MaterialButton @click="createSignature(user)" color="success" margin="mb-0 mx-1" size="sm"
                          icon="plus">
                          <span class="d-none d-md-block">Nova assinatura</span>
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
