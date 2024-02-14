<script>
// componentes
import NavBar from '@/components/Navbars/NavBar.vue'
import SidebarNav from './components/SidebarNav.vue'
import BenefitForm from './components/BenefitForm.vue'
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
      benefits: [],
    }
  },
  methods: {
    getBenefits() {
      api.get('planos/beneficios/').then(response => {
        this.benefits = response.data;
      }).catch(e => console.error('Erro ao obter os benefícios: ', e))
    },
    getModal(initialData = {}) {
      // Criar um elemento div
      const div = document.createElement('div');
      // Montar o componente vue na div
      const form = createApp(BenefitForm, { initialData: initialData }).mount(div);

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
    createBenefit() {
      this.getModal().then(result => {
        if (result.isConfirmed) {
          api.post('planos/beneficios/criar', result.value).then(() => {
            this.getBenefits();
            Swal.fire('Criado!', 'Benefício criado com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao criar o benefício: ', e)
          });
        }
      })
    },
    editBenefit(id, benefit) {
      const initialData = { name: benefit.name, description: benefit.description }

      this.getModal(initialData).then(result => {
        if (result.isConfirmed) {
          api.put(`planos/beneficios/editar/${id}`, result.value).then(() => {
            this.getBenefits();
            Swal.fire('Editado!', 'Benefício editado com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao editar o benefício: ', e)
          });
        }
      })
    },
    deleteBenefit(id) {
      Swal.fire({
        title: 'Excluir benefício',
        text: 'Esta ação é irreversível. Tem certeza de que deseja excluir o benefício?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        // cancelButtonColor: '',
        confirmButtonText: 'Sim, excluir!',
        cancelButtonText: 'Cancelar',
      }).then((result) => {
        if (result.isConfirmed) {
          api.delete(`planos/beneficios/deletar/${id}`).then(() => {
            this.getBenefits()
            Swal.fire('Excluído!', 'Benefício deletado com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao deletar o benefício: ', e)
          });
        }
      });
    }
  },
  mounted() {
    this.getBenefits();
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
              <button class="btn btn-success btn-md ms-4 mt-n3 border-radius-xl" @click="createBenefit">
                <i class="fa fa-plus ms-0 me-2"></i>Novo benefício
              </button>
            </div>
            <div class="card-body">
              <div class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th>Nome</th>
                      <th>Descrição</th>
                      <th></th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(benefit, index) in benefits" :key="index">
                      <td>{{ benefit.name }}</td>
                      <td>{{ benefit.description }}</td>
                      <td class="d-flex">
                        <MaterialButton @click="editBenefit(benefit.id, benefit)" color="warning" margin="mb-0 mx-1"
                          size="sm" icon="pen">
                          <span class="d-none d-md-block">editar</span>
                        </MaterialButton>
                        <MaterialButton @click="deleteBenefit(benefit.id)" color="danger" margin="mb-0 mx-1" size="sm"
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
