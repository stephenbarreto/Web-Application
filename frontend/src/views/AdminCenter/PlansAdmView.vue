<script>
// componentes
import NavBar from '@/components/Navbars/NavBar.vue'
import SidebarNav from './components/SidebarNav.vue'
import PlanForm from './components/PlanForm.vue'
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
      plans: [],
    }
  },
  methods: {
    getPlans() {
      api.get('planos/').then(response => {
        this.plans = response.data;
      }).catch(e => console.error('Erro ao obter os planos: ', e))
    },
    getModal(initialData = {}) {
      // Criar um elemento div
      const div = document.createElement('div');
      // Montar o componente vue na div
      const form = createApp(PlanForm, { initialData: initialData }).mount(div);

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
    createPlan() {
      this.getModal().then(result => {
        if (result.isConfirmed) {
          api.post('planos/criar', result.value).then(() => {
            this.getPlans();
            Swal.fire('Criado!', 'Plano criado com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao criar o plano: ', e)
          });
        }
      })
    },
    editPlan(id, plan) {
      const initialData = { name: plan.name, value: plan.value }

      this.getModal(initialData).then(result => {
        if (result.isConfirmed) {
          api.put(`planos/editar/${id}`, result.value).then(() => {
            this.getPlans();
            Swal.fire('Editado!', 'Plano editado com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao editar o plano: ', e)
          });
        }
      })
    },
    deletePlan(id) {
      Swal.fire({
        title: 'Excluir plano',
        text: 'Esta ação é irreversível. Tem certeza de que deseja excluir o plano?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        // cancelButtonColor: '',
        confirmButtonText: 'Sim, excluir!',
        cancelButtonText: 'Cancelar',
      }).then((result) => {
        if (result.isConfirmed) {
          api.delete(`planos/deletar/${id}`).then(() => {
            this.getPlans()
            Swal.fire('Excluído!', 'Plano deletado com sucesso.', 'success');
          }).catch(e => {
            console.error('Erro ao deletar o plano: ', e)
          });
        }
      });
    }
  },
  mounted() {
    this.getPlans();
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
              <button class="btn btn-success btn-md ms-4 mt-n3 border-radius-xl" @click="createPlan">
                <i class="fa fa-plus ms-0 me-2"></i>Novo plano
              </button>
            </div>
            <div class="card-body">
              <div class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th>Nome</th>
                      <th>Valor</th>
                      <th></th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(plan, index) in plans" :key="index">
                      <td>{{ plan.name }}</td>
                      <td>R${{ plan.value }}</td>
                      <td class="d-flex">
                        <MaterialButton @click="editPlan(plan.id, plan)" color="warning" margin="mb-0 mx-1" size="sm"
                          icon="pen">
                          <span class="d-none d-md-block">editar</span>
                        </MaterialButton>
                        <MaterialButton @click="deletePlan(plan.id)" color="danger" margin="mb-0 mx-1" size="sm"
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
