<template>
  <aside id="sidenav-main"
    class="sidenav navbar navbar-vertical navbar-expand-xs border-0 border-radius-xl my-3 ms-3 fixed-start bg-light shadow-xl">
    <div class="sidenav-header">
      <i class="top-0 p-3 cursor-pointer fas fa-times text-secondary opacity-5 position-absolute end-0 d-none d-xl-none"
        aria-hidden="true" id="iconSidenav"></i>
      <a class="m-0 navbar-brand" href="/">
        <img :src="logo" alt="Logo" class="navbar-brand-img">
      </a>
    </div>
    <hr class="horizontal dark mt-0 mb-2" />
    <SidenavList :links="links"/>
  </aside>
</template>

<script>
import SidenavList from "./SidenavList.vue";
import { mapState } from "vuex";
import logo from "@/assets/img/veloxnet/veloxnet-logo-horizontal.png"

export default {
  name: "SideNav",
  components: {
    SidenavList,
  },
  props: {
    links: {
      type: Array,
      name: String,
      href: String,
      icon: String,
      default: () => [],
    },
  },
  data() {
    return {
      logo,
    };
  },
  computed: {
    ...mapState(["isRTL", "sidebarType", "isDarkMode"]),
  },
};
</script>
