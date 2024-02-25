<script>
import Background from '@/assets/img/veloxnet/background.png'
import Background1 from '@/assets/img/veloxnet/carrossel.png'
import Background2 from '@/assets/img/veloxnet/carrossel2.png'
import Background3 from '@/assets/img/veloxnet/carrossel3.png'

export default {
  props: {
    name: {
      type: String,
      default: 'default'
    },
    images: {
      type: Array,
      path: Object,
      default: () => [
        { path: Background },
        { path: Background1 }, 
        { path: Background2 }, 
        { path: Background3 } 
      ]
    }
  }
}
</script>

<template>
  <div :id="`carousel-${name}-pricing`" class="carousel slide carousel-team" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item" v-for="(image, index) in images" :key="index" :class="{ active: index === 0 }">
        <img :src="image.path" :alt="`image_${index}`" width="100%">
      </div>
    </div>
    <a class="carousel-control-prev text-dark text-lg" role="button" :href="`#carousel-${name}-pricing`"
      data-bs-slide="prev">
      <div class="bg-light rounded-circle d-flex justify-content-center align-items-center"
        style="width: 3.5rem; height: 3.5rem;">
        <i class="fas fa-chevron-left" aria-hidden="true"></i>
        <span class="sr-only">Previous</span>
      </div>
    </a>
    <a class="carousel-control-next text-dark text-lg" role="button" :href="`#carousel-${name}-pricing`"
      data-bs-slide="next">
      <div class="bg-light rounded-circle d-flex justify-content-center align-items-center"
        style="width: 3.5rem; height: 3.5rem;">
        <i class="fas fa-chevron-right" aria-hidden="true"></i>
        <span class="sr-only">Next</span>
      </div>
    </a>
  </div>
</template>
