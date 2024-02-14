<script>
import SidenavCollapse from "./SidenavCollapse.vue";

export default {
  name: "SidenavList",
  props: {
    cardBg: String,
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
      isActive: "active"
    };
  },
  components: {
    SidenavCollapse
  }
};
</script>

<template>
  <div class="w-auto h-auto collapse navbar-collapse max-height-vh-100 h-100" id="sidenav-collapse-main">
    <ul class="navbar-nav">
      <li class="nav-item" v-for="(link, index) in links" :key="index">
        <sidenav-collapse url="#" :aria-controls="''" :collapse="false" :collapseRef="link.href" :navText="link.name">
          <template v-slot:icon>
            <i class="material-icons-round opacity-10 fs-5">{{ link.icon }}</i>
          </template>
        </sidenav-collapse>
      </li>
    </ul>
  </div>
</template>
