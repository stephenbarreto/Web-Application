<template>
  <nav
    class="navbar navbar-main navbar-expand-lg position-sticky mt-4 top-1 px-0 mx-4 shadow-xl border-radius-xl z-index-sticky bg-light"
    v-bind="$attrs" id="navbarBlur" data-scroll="true" :class="isAbsolute ? 'mt-4' : 'mt-0'" :key="isAuthenticated">
    <div class="px-3 py-1 container-fluid">
      <BreadCrumbs :currentPage="title" />
      <div class="mt-2 collapse navbar-collapse mt-sm-0 me-md-0 me-sm-4 me-sm-4" id="navbar">
        <ul class="navbar-nav justify-content-end ms-md-auto">
          <li class="nav-item dropdown d-flex align-items-center">
            <span v-if="user" class="me-2">{{ user.username }}</span>
            <a href="#" id="dropdownMenuButton" data-bs-toggle="dropdown"
              class="px-0 nav-link font-weight-bold d-flex align-items-center" aria-expanded="false">
              <i class="material-icons me-sm-1">account_circle</i>
            </a>
            <ul class="px-2 py-3 dropdown-menu dropdown-menu-end me-n3 shadow-dark shadow-lg"
              aria-labelledby="dropdownMenuButton" data-bs-popper="none">
              <li>
                <button @click="logout()" class="dropdown-item border-radius-md" v-if="isAuthenticated">
                  <i class="fa fa-sign-out-alt me-2"></i><span>Sair</span>
                </button>
              </li>
            </ul>
          </li>
          <li class="nav-item d-xl-none ps-3 d-flex align-items-center">
            <a href="#" @click="toggleSidebar" class="p-0 nav-link text-body lh-1" id="iconNavbarSidenav">
              <div class="sidenav-toggler-inner">
                <i class="sidenav-toggler-line"></i>
                <i class="sidenav-toggler-line"></i>
                <i class="sidenav-toggler-line"></i>
              </div>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import BreadCrumbs from "../BreadCrumbs.vue";
import { mapMutations, mapState, mapGetters } from "vuex";
import Swal from "sweetalert2";

export default {
  name: "NavBar",
  data() {
    return {
      showMenu: false,
    };
  },
  props: ["minNav"],
  created() {
    this.minNav;
  },
  methods: {
    ...mapMutations(["navbarMinimize", "toggleConfigurator"]),

    toggleSidebar() {
      this.navbarMinimize();
    },
    logout() {
      Swal.fire({
        title: 'Sair',
        text: 'Tem certeza de que deseja se deslogar ?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        // cancelButtonColor: '',
        confirmButtonText: 'Sim, quero sair!',
        cancelButtonText: 'Cancelar',
      }).then((result) => {
        if (result.isConfirmed) {
          this.store.dispatch('logout');
        }
      });
    }
  },
  components: {
    BreadCrumbs,
  },
  computed: {
    ...mapGetters({
      isAuthenticated: "isAuthenticated",
    }),
    ...mapState(["isAbsolute", "user", "title"]),
  },
};
</script>
