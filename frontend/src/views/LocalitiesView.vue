<script>
import FooterCentered from '@/components/FooterCentered.vue';
import NavbarDefault from '@/components/Navbars/NavbarDefault.vue';
import LocalitiesList from '@/components/LocalitiesList.vue';
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
    LocalitiesList,
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
            <h3 class="text-white">Saiba onde atuamos</h3>
            <p class="text-white">Estamos constantemente expandindo nossa rede para atender a mais áreas e comunidades.
            </p>
          </div>
        </div>
      </div>
    </div>
    <!-- enrolação -->
  </section>
  <section>
    <LocalitiesList />
  </section>
  <FooterCentered />
  <div class="fixed-plugin">
    <WppButton />
  </div>
</template>