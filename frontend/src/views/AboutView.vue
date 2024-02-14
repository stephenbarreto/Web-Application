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
              <p class="lead text-white mb-6">Bem-vindo à VeloxNet, sua Jornada para a Conexão Perfeita</p>
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
                    Na VeloxNet, acreditamos que a internet vai além da simples conectividade; ela é a ponte que une as
                    pessoas,
                    os lugares e as experiências. Fundada com o compromisso de oferecer uma conexão que transforma
                    vidas, a
                    VeloxNet se destaca como um provedor de internet dedicado a proporcionar uma experiência online
                    excepcional.
                  </p>
                  <p class="text-dark">
                    Somos mais do que um provedor de internet; somos facilitadores de conexões, impulsionados pela
                    paixão por
                    fornecer serviços de alta qualidade que moldam o modo como você vive, trabalha e se diverte. Na
                    VeloxNet,
                    estamos enraizados em valores fundamentais que orientam nossa missão:
                  </p>
                  <p class="text-dark">
                    <b>Inovação Constante:</b> Buscamos continuamente novas tecnologias e soluções para oferecer a você
                    o que há
                    de mais avançado em conectividade. Estamos na vanguarda da inovação para garantir que você aproveite
                    os
                    benefícios da era digital.
                  </p>
                  <p class="text-dark">
                    <b>Conexão Humana:</b> Acreditamos que a internet é uma ferramenta poderosa para unir as pessoas.
                    Nosso foco
                    vai
                    além dos bits e bytes; trabalhamos para criar uma experiência online que fortaleça relacionamentos,
                    conectando comunidades e famílias.
                  </p>
                  <p class="text-dark">
                    <b>Compromisso com a Excelência:</b> Nossa equipe é impulsionada pela busca constante da excelência.
                    Desde a
                    instalação inicial até o suporte técnico contínuo, estamos comprometidos em superar suas
                    expectativas e
                    oferecer um serviço de primeira classe.
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

                  <b>Junte-se à VeloxNet e Viva a Experiência de uma Conexão Sem Limites. Estamos Aqui Para Transformar
                    a
                    Maneira Como Você Conecta com o Mundo.</b>
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
