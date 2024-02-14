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
        { href: '/adm/planos', name: 'Planos', icon: 'shopping_bag' },
        { href: '/adm/planos/beneficios', name: 'Benefícios dos Planos', icon: 'loyalty' },
        { href: '/adm/localidades', name: 'Localidades', icon: 'share_location' },
        { href: '/adm/usuarios', name: 'Clientes', icon: 'group' },
        { href: '/adm/assinaturas', name: 'Assinaturas', icon: 'receipt_long' },
        { href: '/adm/mensagens', name: 'Mensagens', icon: 'message' }
      ],
    }
  }
}
</script>

<template>
  <SideNav :links="links" />
</template>
