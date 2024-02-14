<template>
  <router-view />
</template>

<script>
import api from '@/services/api';
import 'bootstrap/dist/js/bootstrap.bundle'
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  computed: {
    ...mapGetters({
      isAuthenticated: "isAuthenticated",
      user: "user"
    }),
    pageTitle() {
      return this.$store.state.title;
    }
  },
  data() {
    return {
      userInfo: {},
    }
  },
  methods: {
    getUserInfo() {
      // Obtem os dados do usuário
      api.get('usuarios/auth/users/me').then(response => {
        this.$store.commit("setUser", response.data);
      }).catch(e => console.error(e))
    },
  },
  watch: {
    pageTitle() {
      document.title = this.pageTitle;
    }
  }
}
</script>
