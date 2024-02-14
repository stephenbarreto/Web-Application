<script>
// componentes
import NavbarDefault from '@/components/Navbars/NavbarDefault.vue';
import FooterCentered from '@/components/FooterCentered.vue'
import WppButton from '@/components/WppButton.vue';

import CardBG from '@/assets/img/veloxnet/capa2.png';

import api from '@/services/api';
import Swal from 'sweetalert2';

export default {
  name: 'ContactView',
  data() {
    return {
      CardBG,
      email: '',
      description: '',
      name: ''
    }
  },
  components: {
    NavbarDefault,
    FooterCentered,
    WppButton,
  },
  methods: {
    sendMessage() {
      const data = {
        name: this.name,
        email: this.email,
        description: this.description
      }

      api.post('mensagens/criar', data).then(() => {
        Swal.fire('Enviada!', 'Sua mensagem foi enviada com sucesso.', 'success');
      }).catch(() => {
        Swal.fire(
          'Erro!',
          `
            Sua mensagem não pôde ser enviad. Por favor, tente mais tarde. Se o 
            problema persistir, tente entrar em contato conosco por outro canal 
            de suporte.
          `,
          'error'
        );
      });
    }
  }
}
</script>

<template>
  <!-- barra de navegação -->
  <NavbarDefault :sticky="true" />
  <main>
    <section class="position-relative">
      <div class="page-header min-vh-50"
        :style="`background-image: url(${CardBG}); transform: translate3d(0px, 0px, 0px);`" loading="lazy">
        <span class="mask bg-gradient-dark"></span>
        <div class="container">
          <div class="row justify-content-center">
            <div class="col-lg-6 text-center mx-auto">
              <h2 class="text-white mb-3">Como podemos lhe ajudar?</h2>
              <p class="lead text-white mb-6">Nós sempre queremos ouvir de você! Informe-nos se houver algo em que
                possamos ajudá-lo.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section>
      <div class="card card-body shadow-xl mx-3 mx-md-4 mt-n6 mb-4">
        <div class="container">
          <div class="row mt-sm-0 mt-5">
            <div class="col-lg-3 col-md-4 position-relative ms-lg-auto">
              <div class="p-3 text-center border-right-after">
                <i class="material-icons text-gradient text-primary text-5xl mb-3">email</i>
                <h6 class="mb-0">Email</h6>
                <p class="text-dark font-weight-normal">hello@email.com</p>
              </div>
            </div>
            <div class="col-lg-3 col-md-4 position-relative">
              <div class="p-3 text-center border-right-after">
                <div class="d-flex mb-3 justify-content-center w-100">
                  <i class="material-icons text-gradient text-primary text-5xl">call</i>
                  <i class="fa fa-whatsapp text-gradient text-primary text-5xl ms-3"></i>
                </div>
                <h6 class="mb-0">Telefone e Whatsapp</h6>
                <p class="text-dark font-weight-normal">(38) 9 9999-9999</p>
              </div>
            </div>
            <div class="col-lg-3 col-md-4 me-lg-auto">
              <div class="p-3 text-center">
                <i class="material-icons text-gradient text-primary text-5xl mb-3">contacts</i>
                <h6 class="mb-0">Contato</h6>
                <p class="text-dark font-weight-normal">Stephen Barreto</p>
              </div>
            </div>
          </div>
        </div>
        <section class="py-md-7 py-5">
          <div class="container">
            <div class="row align-items-center">
              <div class="col-lg-8 col-10 mx-auto text-center">
                <div class="mb-md-5">
                  <h3>Contate-nos</h3>
                  <p class="text-dark">
                    Para mais dúvidas, envie um e-mail para hello@email.com ou entre em contato através do nosso
                    formulário de contato.
                  </p>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-lg-8 mx-auto">
                <div class="card card-plain">
                  <form id="contactForm" autocomplete="off" @submit.prevent="sendMessage">
                    <div class="card-body">
                      <div class="row">
                        <div class="col-md-6">
                          <div class="input-group input-group-static mb-4">
                            <label>Seu nome completo</label>
                            <input type="text" class="form-control" placeholder="Nome completo" v-model="name">
                            <span class="input-group-text"><i class="material-icons">person</i></span>
                          </div>
                        </div>
                        <div class="col-md-6 ps-md-2">
                          <div class="input-group input-group-static mb-4">
                            <label>Seu e-mail</label>
                            <input type="email" class="form-control" placeholder="E-mail" v-model="email">
                            <span class="input-group-text"><i class="material-icons">email</i></span>
                          </div>
                        </div>
                      </div>
                      <div class="form-group mb-4 mt-md-0 mt-4">
                        <div class="input-group input-group-static mb-4">
                          <label>Como podemos lhe ajudar?</label>
                          <textarea name="message" class="form-control" id="message" rows="6"
                            placeholder="Descreva seu problema e como podemos lhe ajudar"
                            v-model="description"></textarea>
                        </div>
                      </div>
                      <div class="row">
                        <div class="col-md-12 text-center">
                          <button type="submit" class="btn bg-gradient-primary mt-4">Enviar mensagem</button>
                        </div>
                      </div>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </section>
      </div>
    </section>
  </main>
  <!-- rodapé -->
  <FooterCentered />
  <div class="fixed-plugin">
    <WppButton />
  </div>
</template>
