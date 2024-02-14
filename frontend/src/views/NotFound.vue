<template>
  <div class="d-flex justify-content-center align-items-center min-vh-100">
    <div>
      <h1>404 - Página não encontrada</h1>
      <p class="text-dark fs-4">A página que você está procurando não existe.</p>
      <router-link :to="{ name: 'home' }" class="btn btn-lg btn-primary float-end">
        <i class="fa fa-chevron-left me-2"></i> Voltar para a página inicial
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFound',
}
</script>
