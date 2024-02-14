<script>
// componentes
import NavbarDefault from '@/components/Navbars/NavbarDefault.vue';
import FooterCentered from '@/components/FooterCentered.vue'
import WppButton from '@/components/WppButton.vue';

export default {
  name: 'FAQView',
  components: {
    NavbarDefault,
    FooterCentered,
    WppButton,
  },
}
</script>

<template>
  <!-- barra de navegação -->
  <NavbarDefault :sticky="true" />
  <main>
    <section>
      <!-- apresentação -->
    </section>
    <section class="mt-8">
      <div class="container">
        <div class="row justify-content-center text-center">
          <div class="col-md-4 p-3">
            <div class="card h-100 p-3">
              <div class="icon icon-md icon-shape bg-gradient-primary shadow-primary text-center border-radius-xl mt-n4">
                <i class="material-icons opacity-10">bolt</i>
              </div>
              <h5 class="mt-3">Conexão Rápida e Confiável</h5>
              <p class="text-dark">Desfrute de uma experiência de navegação ultrarrápida
                com a nossa conexão de alta velocidade. Transmita vídeos, jogue online e baixe arquivos em um piscar
                de olhos, sem interrupções.</p>
            </div>
          </div>
          <div class="col-md-4 p-3">
            <div class="card h-100 p-3">
              <div class="icon icon-md icon-shape bg-gradient-primary shadow-primary text-center border-radius-xl mt-n4">
                <i class="material-icons opacity-10">wifi</i>
              </div>
              <h5 class="mt-3">Cobertura Ampliada</h5>
              <p class="text-dark">Mantenha-se conectado em todos os cantos da sua casa ou empresa com nossa
                cobertura abrangente. Nossa infraestrutura robusta garante uma conexão estável em todos os ambientes,
                oferecendo a você liberdade para usar a internet onde quiser.</p>
            </div>
          </div>
          <div class="col-md-4 p-3">
            <div class="card h-100 p-3">
              <div class="icon icon-md icon-shape bg-gradient-primary shadow-primary text-center border-radius-xl mt-n4">
                <i class="material-icons opacity-10">support_agent</i>
              </div>
              <h5 class="mt-3">Suporte Técnico Excepcional</h5>
              <p class="text-dark">Estamos aqui para você sempre que for preciso. Nossa equipe de suporte técnico
                altamente qualificada está pronta para ajudar com qualquer problema que você possa encontrar.
                Garantimos uma experiência tranquila para que você possa aproveitar ao máximo sua VeloxNet.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="pt-7 pb-md-5 pb-lg-7">
      <div class="container">
        <div class="col-12 mx-auto">
          <div class="card shadow-lg">
            <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
              <div class="bg-gradient-primary shadow-primary border-radius-lg p-4">
                <h3 class="text-white mb-0">Perguntas frequentes</h3>
              </div>
            </div>
            <div class="card-body p-sm-5 pt-0">
              <h5 class="my-4">Básicas</h5>
              <div class="accordion" id="accordionFaq1">
                <div class="accordion-item mb-3">
                  <h6 class="accordion-header" id="headingOne">
                    <button class="accordion-button border-bottom font-weight-bold text-start" type="button"
                      data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true"
                      aria-controls="collapseOne">
                      Como posso verificar a disponibilidade da VeloxNet na minha região?
                      <i class="collapse-close fa fa-plus text-xs pt-1 position-absolute end-0" aria-hidden="true"></i>
                      <i class="collapse-open fa fa-minus text-xs pt-1 position-absolute end-0" aria-hidden="true"></i>
                    </button>
                  </h6>
                  <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne"
                    data-bs-parent="#accordionFaq1">
                    <div class="accordion-body text-sm text-dark">
                      Você pode verificar a disponibilidade dos nossos serviços em nossa página de
                      <router-link :to="{ name: 'localities' }" class="link-primary">localidades</router-link> de
                      cobertura. Estamos
                      constantemente expandindo nossa rede para atender a mais áreas e comunidades.
                    </div>
                  </div>
                </div>
              </div>
              <div class="accordion" id="accordionFaq2">
                <div class="accordion-item mb-3">
                  <h6 class="accordion-header" id="headingTwo">
                    <button class="accordion-button border-bottom font-weight-bold text-start" type="button"
                      data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="true"
                      aria-controls="collapseTwo">
                      Quais são as opções de velocidade de conexão oferecidas pela VeloxNet?
                      <i class="collapse-close fa fa-plus text-xs pt-1 position-absolute end-0" aria-hidden="true"></i>
                      <i class="collapse-open fa fa-minus text-xs pt-1 position-absolute end-0" aria-hidden="true"></i>
                    </button>
                  </h6>
                  <div id="collapseTwo" class="accordion-collapse collapse show" aria-labelledby="headingOne"
                    data-bs-parent="#accordionFaq2">
                    <div class="accordion-body text-sm text-dark">
                      Oferecemos uma variedade de planos de internet com diferentes velocidades para atender às suas
                      necessidades. Nossos consultores especializados podem ajudá-lo a escolher o plano que melhor se
                      adapta ao seu estilo de vida e exigências de uso da internet.
                    </div>
                  </div>
                </div>
              </div>
              <div class="accordion" id="accordionFaq3">
                <div class="accordion-item mb-3">
                  <h6 class="accordion-header" id="headingThree">
                    <button class="accordion-button border-bottom font-weight-bold text-start" type="button"
                      data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="true"
                      aria-controls="collapseThree">
                      Como posso entrar em contato com o suporte técnico da VeloxNet?
                      <i class="collapse-close fa fa-plus text-xs pt-1 position-absolute end-0" aria-hidden="true"></i>
                      <i class="collapse-open fa fa-minus text-xs pt-1 position-absolute end-0" aria-hidden="true"></i>
                    </button>
                  </h6>
                  <div id="collapseThree" class="accordion-collapse collapse show" aria-labelledby="headingOne"
                    data-bs-parent="#accordionFaq3">
                    <div class="accordion-body text-sm text-dark">
                      Nosso suporte técnico está disponível 24 horas por dia, 7 dias por semana. Você pode entrar em
                      contato conosco através do nosso número de telefone dedicado via ligação ou whatsapp.
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
  <!-- rodapé -->
  <FooterCentered />
  <div class="fixed-plugin">
    <WppButton />
  </div>
</template>
