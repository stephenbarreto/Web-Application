<script>
import SideNav from '@/components/Sidenav/SideNav.vue';

export default {
  name: 'SidebarNav',
  components: {
    SideNav
  },
  data() {
    return {
      links: [
        { href: '/assinante', name: 'Geral', icon: 'dashboard' },
        { href: '/assinante/assinaturas', name: 'Minhas assinaturas', icon: 'assignment' },
        { href: '/assinante/boletos', name: 'Meus boletos', icon: 'receipt_long' },
      ],
    }
  }
}
</script>

<template>
  <SideNav :links="links" />
</template>
