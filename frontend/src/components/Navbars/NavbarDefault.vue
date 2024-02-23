<script>
// images
import ArrDark from "@/assets/img/down-arrow-dark.svg";
import DownArrWhite from "@/assets/img/down-arrow-white.svg";
import Logo from '@/assets/img/veloxnet/veloxnet-logo-horizontal.png'

export default {
  data() {
    return {
      Logo,
      action: null
    }
  },
  created() {
    const customer = {
      route: "/assinante",
      color: "bg-gradient-primary",
      label: "Central do assinante"
    }

    const admin = {
      route: "/adm/planos",
      color: "bg-gradient-primary",
      label: "Central do administrador"
    }
  
    this.action = this.$store.state.user?.is_manager ? admin : customer;
  },
  props: {
    transparent: {
      type: Boolean,
      default: false
    },
    light: {
      type: Boolean,
      default: true
    },
    dark: {
      type: Boolean,
      default: false
    },
    sticky: {
      type: Boolean,
      default: false
    },
    darkText: {
      type: Boolean,
      default: false
    },
    sections: {
      type: Array,
      name: String,
      href: String,
      default: () => []
    },
  },
  methods: {
    // set arrow  color
    getArrowColor() {
      if (this.transparent && this.textDark.value) {
        return ArrDark;
      } else if (this.transparent) {
        return DownArrWhite;
      } else {
        return ArrDark;
      }
    },
    // set text color
    getTextColor() {
      let color;

      if (this.transparent && this.textDark.value) {
        color = "text-dark";
      } else if (this.transparent) {
        color = "text-white";
      } else {
        color = "text-dark";
      }

      return color;
    }
  }
};
</script>

<template>
  <nav class="navbar navbar-expand-lg top-0" :class="{
    'z-index-3 w-100 shadow-none navbar-transparent position-absolute my-3':
      transparent,
    'z-index-3': sticky,
    'navbar-light bg-white p-0': light,
    ' navbar-dark bg-gradient-dark z-index-3 py-3': dark
  }">
    <div :class="transparent || light || dark
      ? 'container'
      : 'container-fluid px-0'
      ">
      <RouterLink class="navbar-brand d-none d-md-block" :class="[
        (transparent && textDark.value) || !transparent
          ? 'text-dark font-weight-bolder ms-sm-3'
          : 'text-white font-weight-bolder ms-sm-3'
      ]" to="/" rel="tooltip" title="Designed and Coded by Creative Tim" data-placement="bottom">
        <img :src="Logo" alt="VeloxNet" height="60">
      </RouterLink>
      <RouterLink class="navbar-brand d-block d-md-none" :class="transparent || dark
        ? 'text-white'
        : 'font-weight-bolder ms-sm-3'
        " to="/" rel="tooltip" title="Designed and Coded by Creative Tim" data-placement="bottom">
        <img :src="Logo" alt="VeloxNet" height="60">
      </RouterLink>
      <a class="btn btn-sm mb-0 ms-auto d-lg-none d-block" :href="action.route" :class="action.color">
        {{ action.label }}
      </a>
      <button class="navbar-toggler shadow-none ms-2" type="button" data-bs-toggle="collapse" data-bs-target="#navigation"
        aria-controls="navigation" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon mt-2">
          <span class="navbar-toggler-bar bar1"></span>
          <span class="navbar-toggler-bar bar2"></span>
          <span class="navbar-toggler-bar bar3"></span>
        </span>
      </button>
      <div class="collapse navbar-collapse w-100 pt-3 pb-2 py-lg-0" id="navigation">
        <ul class="navbar-nav navbar-nav-hover ms-auto">
          <li v-for="section in sections" :key="section.name" class="nav-item">
            <a :href="section.href" role="button" class="nav-link ps-2 cursor-pointer">
              {{ section.name }}
            </a>
          </li>
          <li class="nav-item dropdown dropdown-hover mx-2">
            <a role="button" class="nav-link ps-2 d-flex cursor-pointer align-items-center" :class="getTextColor()"
              id="dropdownMenuPages" data-bs-toggle="dropdown" aria-expanded="false">
              <i class="material-icons opacity-6 me-2 text-md" :class="getTextColor()">dashboard</i>
              Páginas
              <img :src="getArrowColor()" alt="down-arrow" class="arrow ms-2 d-lg-block d-none" />
              <img :src="getArrowColor()" alt="down-arrow" class="arrow ms-1 d-lg-none d-block ms-auto" />
            </a>
            <div class="dropdown-menu dropdown-menu-animation ms-n3 dropdown-md p-3 border-radius-xl mt-0 mt-lg-3"
              aria-labelledby="dropdownMenuPages">
              <div class="row d-none d-lg-block">
                <div class="col-12 px-4 py-2">
                  <div class="row">
                    <div class="position-relative">
                      <div class="dropdown-header text-dark font-weight-bolder d-flex align-items-center px-1">
                        Páginas Principais
                      </div>
                      <RouterLink to="/sobre" class="dropdown-item border-radius-md">
                        <span>Sobre Nós</span>
                      </RouterLink>
                      <RouterLink to="/contato-suporte" class="dropdown-item border-radius-md">
                        <span>Contato e Suporte</span>
                      </RouterLink>
                      <RouterLink to="/faq" class="dropdown-item border-radius-md">
                        <span>Perguntas Frequentes</span>
                      </RouterLink>
                      <RouterLink to="/planos" class="dropdown-item border-radius-md">
                        <span>Nossos Planos</span>
                      </RouterLink>
                      <RouterLink to="/localidades" class="dropdown-item border-radius-md">
                        <span>Onde Atuamos</span>
                      </RouterLink>
                    </div>
                  </div>
                </div>
              </div>
              <div class="d-lg-none">
                <div class="dropdown-header text-dark font-weight-bolder d-flex align-items-center px-0">
                  Páginas Principais
                </div>
                <RouterLink to="/sobre" class="dropdown-item border-radius-md">
                  <span>Sobre Nós</span>
                </RouterLink>
                <RouterLink to="/contato-suporte" class="dropdown-item border-radius-md">
                  <span>Contato e Suporte</span>
                </RouterLink>
                <RouterLink to="/faq" class="dropdown-item border-radius-md">
                  <span>Perguntas Frequentes</span>
                </RouterLink>
                <RouterLink to="/planos" class="dropdown-item border-radius-md">
                  <span>Nossos Planos</span>
                </RouterLink>
                <RouterLink to="/localidades" class="dropdown-item border-radius-md">
                  <span>Onde Atuamos</span>
                </RouterLink>
              </div>
            </div>
          </li>
        </ul>
        <ul class="navbar-nav d-lg-block d-none">
          <li class="nav-item">
            <a :href="action.route" class="btn btn-sm mb-0" :class="action.color">{{ action.label }}</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <!-- End Navbar -->
</template>
