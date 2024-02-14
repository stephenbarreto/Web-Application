<script>
import api from '@/services/api';

// components
import LocalityCard from './LocalityCard.vue';

export default {
  name: 'LocalitiesList',
  props: {
    limit: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      localities: [],
      localitiesCount: 0
    }
  },
  components: {
    LocalityCard,
  },
  methods: {
    getPlans() {
      // Obter a lista de localidades
      api.get('localidades/')
        .then(response => {
          const localities = response.data

          this.localitiesCount = localities.length
          this.limit
            ? this.localities = localities.slice(0, this.limit)
            : this.localities = localities
        })
        .catch(e => console.error(e));
    },
  },
  created() {
    this.getPlans();
  },
}
</script>

<template>
  <div class="container mt-5">
    <div class="row mt-5">
      <LocalityCard v-for="locality in localities" :key="locality.id" :city="locality.city" :state="locality.state" />
    </div>
    <div v-if="limit && localitiesCount > limit" class="mt-4 text-center">
      <router-link :to="{ name: 'localities' }" class="btn btn-primary">Ver mais</router-link>
    </div>
  </div>
</template>