<script>
// componentes
import MaterialInput from '@/components/MaterialInput.vue';
import NavbarDefault from '@/components/Navbars/NavbarDefault.vue';
import FooterCentered from '@/components/FooterCentered.vue'
import WppButton from '@/components/WppButton.vue';
import api from '@/services/api';

export default {
  name: 'LoginView',
  data() {
    return {
      formData: {},
    }
  },
  components: {
    MaterialInput,
    NavbarDefault,
    FooterCentered,
    WppButton,
  },
  methods: {
    updateFormData({ name, value }) {
      this.formData[name] = value
    },
    login() {
      api.defaults.headers.common["Authorization"] = "";

      api.post('usuarios/auth/token/login', this.formData).then(response => {
        const token = response.data.auth_token;

        this.$store.commit("setToken", token);

        api.defaults.headers.common['Authorization'] = `Token ${token}`;

        localStorage.setItem("token", token);

        // Redireciona o usuário para a página inicial
        this.$router.push('/')
      }).catch(e => {
        console.error('Erro no login: ', e.response.data);
      })
    },
  },
}
</script>

<template>
  <!-- barra de navegação -->
  <NavbarDefault :sticky="true" />
  <section>
    <div class="page-header min-vh-75">
      <div class="container">
        <div class="row">
          <div class="col-xl-4 col-lg-5 col-md-7 mx-auto">
            <div class="card z-index-0 mt-7">
              <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
                <div class="bg-gradient-primary shadow-primary border-radius-lg py-3 pe-1 text-center py-4">
                  <h4 class="font-weight-bolder text-white mt-1 mb-0">Acessar Conta</h4>
                  <p class="mb-1 text-sm text-white">Informe seus dados de login</p>
                </div>
              </div>
              <div class="card-body pb-0">
                <p>{{ message }}</p>
                <form @submit.prevent="login">
                  <MaterialInput id="email" class="input-group-outline my-3"
                    :label="{ text: 'Email', class: 'form-label' }" type="email" @input-change="updateFormData"
                    name="email" />
                  <MaterialInput id="email" class="input-group-outline my-3"
                    :label="{ text: 'Senha', class: 'form-label' }" type="password" @input-change="updateFormData"
                    name="password" />
                  <div class="text-center">
                    <input type="submit" class="btn bg-gradient-primary w-100 mt-4 mb-2" value="Acessar">
                  </div>
                </form>
              </div>
              <div class="card-footer text-center pt-0 px-sm-4 px-1">
                <p class="mb-0 mt-3 text-sm mx-auto">
                  Ainda não é cliente?
                  <RouterLink to="/planos">Confira nossos planos</RouterLink>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- rodapé -->
  <FooterCentered />
  <div class="fixed-plugin">
    <WppButton />
  </div>
</template>
