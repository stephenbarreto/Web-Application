<script>
// componentes
import NavbarDefault from '@/components/Navbars/NavbarDefault.vue';
import FooterCentered from '@/components/FooterCentered.vue'
import WppButton from '@/components/WppButton.vue';

import CardBG from '@/assets/img/veloxnet/capa2.png';

export default {
  name: 'AboutView',
  data() {
    return {
      CardBG,
    }
  },
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
    <section class="position-relative">
      <div class="page-header min-vh-50"
        :style="`background-image: url(${CardBG}); transform: translate3d(0px, 0px, 0px);`" loading="lazy">
        <span class="mask bg-gradient-dark"></span>
        <div class="container">
          <div class="row justify-content-center">
            <div class="col-lg-6 text-center mx-auto">
              <h2 class="text-white mb-3">Quem Somos - VeloxNet</h2>
              <p class="lead text-white mb-6">Bem-vindo à VeloxNet, Sua Jornada para uma Conexão Acessível e Conveniente</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section>
      <div class="card card-body shadow-xl mx-3 mx-md-4 mt-n6 mb-4">
        <section class="py-md-7 py-5">
          <div class="container">
            <div class="row align-items-center">
              <div class="col-lg-8 col-10 mx-auto">
                <div class="mb-md-5">
                  <p class="text-dark">
                    Somos dedicados a oferecer uma conexão que não só transforma vidas, mas também se encaixa no 
                    seu bolso. Na VeloxNet, valorizamos sua comodidade, proporcionando todos os equipamentos 
                    necessários de forma gratuita.
                  </p>
                  <p class="text-dark">
                    Acreditamos que todos devem ter acesso a uma internet de qualidade, independentemente de sua situação 
                    financeira. Por isso, buscamos constantemente maneiras de oferecer serviços acessíveis, sem 
                    comprometer a qualidade.
                  </p>
                  <p class="text-dark">
                    <b>Na VeloxNet, oferecemos:</b> 
                  </p>
                  <p class="text-dark">
                    <b>Preços Acessíveis:</b> Entendemos a importância de uma internet acessível. Nossos planos são 
                    cuidadosamente projetados para se adequar ao seu orçamento, garantindo que você tenha acesso a uma 
                    conexão de qualidade sem pesar no bolso.
                  </p>
                  <p class="text-dark">
                    <b>Equipamentos Gratuitos:</b> ão se preocupe com custos adicionais. Todos os equipamentos necessários 
                    para desfrutar da nossa conexão de alta velocidade são fornecidos gratuitamente. Desde roteadores até cabos,
                     estamos aqui para garantir sua comodidade desde o primeiro dia.
                  </p>
                  <p class="text-dark">
                    <b>Atendimento Excepcional:</b> Além de preços acessíveis e equipamentos gratuitos, nossa equipe de suporte 
                    técnico está sempre pronta para ajudar. Estamos disponíveis 24/7 para garantir que você receba a assistência 
                    necessária sempre que precisar.
                  </p>
                  <h2>
                    O Que Nos Diferencia?
                  </h2>
                  <p class="text-dark">
                    <b>Velocidade Inigualável:</b> Nossa promessa é proporcionar uma conexão rápida e estável,
                    permitindo que
                    você navegue, transmita e trabalhe sem limitações. A VeloxNet é sinônimo de velocidade inigualável.
                  </p>
                  <p class="text-dark">
                    <b>Atendimento Personalizado:</b> Acreditamos no poder do atendimento humano. Nossa equipe de
                    suporte
                    técnico está
                    disponível 24/7 para garantir que você tenha assistência sempre que precisar.
                  </p>
                  <p class="text-dark">
                    <b>Cobertura Total:</b> Quer esteja em casa, no trabalho ou em trânsito, nossa cobertura abrangente
                    garante
                    que
                    você esteja sempre conectado, sem interrupções.
                  </p>

                  <b>Junte-se à VeloxNet e experimente uma internet de qualidade que não compromete seu bolso. 
                     Estamos aqui para tornar a sua jornada online fácil, acessível e conveniente.</b>
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
