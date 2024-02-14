<script>
// componentes
import PlansList from '@/components/PlansList.vue';
import LocalitiesList from '@/components/LocalitiesList.vue';
import NavbarDefault from '@/components/Navbars/NavbarDefault.vue';
import FooterCentered from '@/components/FooterCentered.vue'
import ImageCarousel from '@/components/ImageCarousel.vue';
import WppButton from '@/components/WppButton.vue';

// imagens
import CardBG from '@/assets/img/veloxnet/capa2.png';

export default {
  name: 'HomeView',
  data() {
    return {
      CardBG,
      sections: [
        { name: 'Planos', href: '#plans' },
        { name: 'Benefícios', href: '#benefits' },
        { name: 'Localidades', href: '#localities' }
      ]
    }
  },
  components: {
    PlansList,
    NavbarDefault,
    FooterCentered,
    ImageCarousel,
    WppButton,
    LocalitiesList,
  },
}
</script>

<template>
  <NavbarDefault :sticky="true" :sections="sections" />
  <main>
    <!-- apresentação -->
    <ImageCarousel />
    <!-- beneficios -->
    <section id="benefits">
      <div class="card shadow-lg mt-n5 mx-4 mb-4">
        <div class="card-body">
          <div class="container-fluid px-0">
            <div class="row">
              <div class="col-lg-4 col-sm-6 mb-sm-0 mb-4">
                <div class="info-horizontal bg-gradient-primary border-radius-xl p-4 d-block d-md-flex ">
                  <i class="material-icons text-3xl text-white">bolt</i>
                  <div class="description ps-0 ps-md-3">
                    <h5 class="text-white">Conexão Rápida e Confiável</h5>
                    <p class="text-white pe-0 pe-lg-5">Descrição: Desfrute de uma experiência de navegação ultrarrápida
                      com a nossa conexão de alta velocidade. Transmita vídeos, jogue online e baixe arquivos em um piscar
                      de olhos, sem interrupções.</p>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-sm-6 px-lg-1">
                <div class="info-horizontal border-radius-xl p-4 d-block d-md-flex ">
                  <i class="material-icons text-3xl text-gradient text-primary">wifi</i>
                  <div class="description ps-0 ps-md-3">
                    <h5>Cobertura Ampliada</h5>
                    <p class="text-dark">Mantenha-se conectado em todos os cantos da sua casa ou empresa com nossa
                      cobertura abrangente.
                      Nossa infraestrutura robusta garante uma conexão estável em todos os ambientes, oferecendo a você
                      liberdade para usar a internet onde quiser.</p>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 mt-lg-0 mt-4">
                <div class="info-horizontal border-radius-xl p-4 d-block d-md-flex ">
                  <i class="material-icons text-3xl text-gradient text-primary">support_agent</i>
                  <div class="description ps-0 ps-md-3">
                    <h5>Suporte Técnico Excepcional</h5>
                    <p class="text-dark">Estamos aqui para você sempre que for preciso. Nossa equipe de suporte técnico
                      altamente qualificada está pronta para ajudar com qualquer problema que você possa encontrar.
                      Garantimos uma experiência tranquila para que você possa aproveitar ao máximo sua VeloxNet.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- cidades disponíveis -->
    <section id="localities" class="mt-8">
      <div class="container">
        <div class="row">
          <div class="col-lg-8">
            <h3>Onde Atuamos</h3>
            <p class="font-weight-normal">
              Seja nosso cliente. Abaixo estão listadas as cidades onde a
              VeloxNet já está disponível e pronta para ir até você.
            </p>
          </div>
        </div>
        <LocalitiesList :limit="6" />
      </div>
    </section>
    <!-- planos -->
    <section id="plans" class="mt-8">
      <div class="bg-gradient-dark position-relative m-3 border-radius-xl shadow-lg overflow-hidden"
        :style="`background-image: url(${CardBG}); background-size: cover;`" loading="lazy">
        <span class="mask bg-gradient-dark opacity-6"></span>
        <div class="container pb-lg-9 pb-7 pt-7 position-relative z-index-1">
          <div class="row">
            <div class="col-md-8 mx-auto text-center">
              <h3 class="text-white">Confira nossos preços</h3>
              <p class="text-white">A VeloxNet já possui cobertura em sua cidade? Então confira abaixo o plano de
                assinatura
                ideal para suas necessidades.</p>
            </div>
          </div>
        </div>
      </div>
      <PlansList :limit="3" />
    </section>
    <!-- rodapé -->
  </main>
  <FooterCentered />
  <!-- botão flutuante -->
  <div class="fixed-plugin">
    <WppButton />
  </div>
</template>
