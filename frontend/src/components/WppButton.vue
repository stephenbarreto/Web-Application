<script>
import FixedButton from './FixedButton.vue';

export default {
  props: {
    action: {
      type: String,
      default: 'https://wa.me/5538999999999?text=Ol%C3%A1%21+Vim+pelo+site+da+VeloxNet+e+gostaria+de+saber+mais+sobre+os+planos+de+assinatura+dispon%C3%ADveis.+'
    }
  },
  components: {
    FixedButton
  },
}
</script>

<template>
  <FixedButton :icon="'fa-whatsapp'" :color="'bg-success'" :action="action" />
</template>
