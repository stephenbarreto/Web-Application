<script>
import api from '@/services/api';

// components
import PlanCard from './PlanCard.vue';

export default {
  name: 'PlansList',
  props: {
    limit: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      plans: [],
      plansCount: 0
    }
  },
  components: {
    PlanCard,
  },
  methods: {
    getPlans() {
      // Obter a lista de planos
      api.get('planos/')
        .then(response => {
          const plans = response.data

          this.plansCount = plans.length
          this.limit
            ? this.plans = plans.slice(0, this.limit)
            : this.plans = plans
        })
        .catch(e => console.error(e));
    },
  },
  created() {
    this.getPlans()
  },
}
</script>

<template>
  <div class="container mt-5">
    <div class="tab-content tab-space">
      <div class="tab-pane active" role="tabpanel" aria-labelledby="#tabs-iconpricing-tab-1">
        <div class="row">
          <PlanCard v-for="plan in plans" :key="plan.id" :name="plan.name" :value="plan.value"
            :benefits="plan.benefits" />
        </div>
      </div>
    </div>
    <div v-if="limit && plansCount > limit" class="mt-4 text-center">
      <router-link :to="{ name: 'plans' }" class="btn btn-primary">Ver mais</router-link>
    </div>
  </div>
</template>
