<template>
  <nav aria-label="breadcrumb">
    <ol class="px-0 pt-1 pb-0 mb-0 bg-transparent breadcrumb me-sm-6">
      <li class="text-sm breadcrumb-item" :class="color">
        <a :class="color" class="opacity-8" href="#">{{ basePage }}</a>
      </li>
      <li class="text-sm breadcrumb-item active" :class="color" aria-current="page">
        {{ currentPage }}
      </li>
    </ol>
    <h6 class="mb-0 font-weight-bolder">{{ currentPage }}</h6>
  </nav>
</template>

<script>
export default {
  name: "BreadCrumbs",
  props: {
    currentPage: {
      type: String,
      required: "",
    },
    basePage: {
      type: String,
      default: "Páginas"
    },
    color: {
      type: String,
      default: "text-dark"
    }
  },
};
</script>
