<script>
import FooterCentered from '@/components/FooterCentered.vue';
import NavbarDefault from '@/components/Navbars/NavbarDefault.vue';
import PlansList from '@/components/PlansList.vue';
import WppButton from '@/components/WppButton.vue';

import CardBG from '@/assets/img/veloxnet/capa2.png';

export default {
  data() {
    return {
      CardBG,
    }
  },
  components: {
    FooterCentered,
    NavbarDefault,
    PlansList,
    WppButton
  }
}
</script>

<template>
  <NavbarDefault />
  <section>
    <div class="bg-gradient-dark position-relative m-3 border-radius-xl shadow-lg overflow-hidden"
      :style="`background-image: url(${CardBG}); background-size: cover;`" loading="lazy">
      <span class="mask bg-gradient-dark opacity-6"></span>
      <div class="container pb-lg-9 pb-7 pt-7 position-relative z-index-1">
        <div class="row">
          <div class="col-md-8 mx-auto text-center">
            <h3 class="text-white">Confira nossos preços</h3>
            <p class="text-white">Oferecemos uma variedade de planos de internet com diferentes velocidades para atender
              às suas necessidades. Nossos consultores especializados podem ajudá-lo a escolher o plano que melhor se
              adapta ao seu estilo de vida e exigências de uso da internet.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
  <section>
    <PlansList />
  </section>
  <FooterCentered />
  <div class="fixed-plugin">
    <WppButton />
  </div>
</template>