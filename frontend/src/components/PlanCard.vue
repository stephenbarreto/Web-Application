<script>
export default {
  props: {
    name: {
      type: String,
      default: ''
    },
    value: {
      type: Number,
      default: 0
    },
    benefits: {
      type: Object,
      name: String,
      description: String,
      default: () => { }
    },
    bgColor: {
      type: String,
      default: 'bg-light'
    },
    link: {
      type: String,
      default: 'https://wa.me/5538998292029?text=Ol%C3%A1%21+Vim+pelo+site+da+VeloxNet+e+gostaria+de+saber+mais+sobre+os+planos+de+assinatura+dispon%C3%ADveis.+'
    }
  },
  name: 'PlanCard',
}
</script>

<template>
  <div class="col-lg-4 mb-4">
    <div class="card shadow-lg h-100" :class="bgColor">
      <span class="badge rounded-pill bg-primary mt-n2 mx-auto">{{ name }}</span>
      <div class="card-header bg-transparent text-center pt-4 pb-3">
        <h1 class="font-weight-bold mt-2">
          <small class="text-lg me-1">R$</small>{{ value }}<small class="text-lg">/mo</small>
        </h1>
      </div>
      <div class="card-body text-lg-start text-center pt-0">
        <div v-for="(benefit, index) in benefits" :key="index"
          class="d-flex justify-content-lg-start justify-content-center p-2 cursor-pointer">
          <i class="material-icons my-auto">done</i>
          <span class="ps-3" :title="benefit.description">{{ benefit.name }}</span>
        </div>
      </div>
      <div class="card-footer">
        <a :href="link" class="btn btn-icon bg-gradient-primary d-lg-block mb-0">
          Assinar
          <i class="fas fa-arrow-right ms-1" aria-hidden="true"></i>
        </a>
      </div>
    </div>
  </div>
</template>
