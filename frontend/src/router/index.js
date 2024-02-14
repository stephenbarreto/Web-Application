import { createRouter, createWebHistory } from 'vue-router'

import HomeView from "@/views/HomeView.vue";
import LoginView from "@/views/LoginView.vue";
import ContactView from "@/views/ContactView.vue"
import FAQView from "@/views/FAQView.vue"
import AboutView from "@/views/AboutView.vue"
import PlansView from "@/views/PlansView.vue"
import CustomerView from "@/views/CustomerCenter/CustomerView.vue"
import BenefitsAdmView from "@/views/AdminCenter/BenefitsAdmView.vue"
import LocalitiesAdmView from "@/views/AdminCenter/LocalitiesAdmView.vue"
import PlansAdmView from "@/views/AdminCenter/PlansAdmView.vue"
import UsersAdmView from "@/views/AdminCenter/UsersAdmView.vue"
import SignaturesAdmView from "@/views/AdminCenter/SignaturesAdmView.vue"
import MessagesAdmView from "@/views/AdminCenter/MessagesAdmView.vue"
import LocalitiesView from "@/views/LocalitiesView.vue"
import SignaturesView from "@/views/CustomerCenter/SignaturesView.vue"
import TicketsView from "@/views/CustomerCenter/TicketsView.vue"
import NotFound from "@/views/NotFound.vue"

import api from '@/services/api';
import store from '@/store';

const publicRoutes = [
  { path: '/:catchAll(.*)', component: NotFound, meta: { title: '404' } },
  {
    path: "/",
    name: "home",
    component: HomeView,
    meta: { title: 'VeloxNet' }
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
    meta: { guest: true, title: 'Login' }
  },
  {
    path: "/contato-suporte",
    name: "contact",
    component: ContactView,
    meta: { title: 'Contato e Suporte' }
  },
  {
    path: "/faq",
    name: "faq",
    component: FAQView,
    meta: { title: 'Perguntas Frequentes' }
  },
  {
    path: "/sobre",
    name: "about",
    component: AboutView,
    meta: { title: 'Sobre nos' }
  },
  {
    path: "/planos",
    name: "plans",
    component: PlansView,
    meta: { title: 'Planos' }
  },
  {
    path: "/localidades",
    name: "localities",
    component: LocalitiesView,
    meta: { title: 'Localidades' }
  },
]

const adminRoutes = [
  {
    path: "/adm/planos",
    name: "adm-plans",
    component: PlansAdmView,
    meta: { requiresAuth: true, requiresAdmin: true, title: 'Planos' }
  },
  {
    path: "/adm/planos/beneficios",
    name: "adm-benefits",
    component: BenefitsAdmView,
    meta: { requiresAuth: true, requiresAdmin: true, title: 'Beneficios dos Planos' }
  },
  {
    path: "/adm/localidades",
    name: "adm-localities",
    component: LocalitiesAdmView,
    meta: { requiresAuth: true, requiresAdmin: true, title: 'Localidades' }
  },
  {
    path: "/adm/usuarios",
    name: "adm-users",
    component: UsersAdmView,
    meta: { requiresAuth: true, requiresAdmin: true, title: 'Clientes' }
  },
  {
    path: "/adm/assinaturas",
    name: "adm-signatures",
    component: SignaturesAdmView,
    meta: { requiresAuth: true, requiresAdmin: true, title: 'Assinaturas' }
  },
  {
    path: "/adm/mensagens",
    name: "adm-messages",
    component: MessagesAdmView,
    meta: { requiresAuth: true, requiresAdmin: true, title: 'Mensagens' }
  },
]

const customerRoutes = [
  {
    path: "/assinante",
    name: "customer",
    component: CustomerView,
    meta: { requiresAuth: true, title: 'Geral' }
  },
  {
    path: "/assinante/assinaturas",
    name: "signatures",
    component: SignaturesView,
    meta: { requiresAuth: true, title: 'Minhas Assinaturas' }
  },
  {
    path: "/assinante/boletos",
    name: "tickets",
    component: TicketsView,
    meta: { requiresAuth: true, title: 'Meus Boletos' }
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes: [...publicRoutes, ...adminRoutes, ...customerRoutes]
})

router.beforeEach((to, from, next) => {
  store.commit("initializeAuth");

  const requiresAuth = to.matched.some(route => route.meta.requiresAuth)
  const requiresAdmin = to.matched.some(route => route.meta.requiresAdmin)
  const requiresGuest = to.matched.some(route => route.meta.guest)
  const isAuthenticated = store.state.isAuthenticated;

  // Define o título da página com base na meta-informação da rota
  const pageTitle = to.meta.title || 'VeloxNet';
  store.commit('setTitle', pageTitle);

  if (requiresGuest && isAuthenticated) {
    // Redirecionar para a página inicial se o usuário já estiver autenticado
    next({ path: '/' });
  } else if (!requiresAuth) {
    // Acessar a página caso o usuário não precise estar logado
    if (isAuthenticated) {
      api.get('usuarios/auth/users/me').then(response => {
        const user = response.data
        store.commit("setUser", user);

        if (requiresAdmin && !user.is_manager) {
          next({ path: '/' });
        } else {
          next();
        }
      }).catch(e => console.error(e))
    } else {
      next();
    }
  } else {
    if (isAuthenticated) {
      api.get('usuarios/auth/users/me').then(response => {
        const user = response.data
        store.commit("setUser", user);

        if (requiresAdmin && !user.is_manager) {
          next({ path: '/' });
        } else {
          next();
        }
      }).catch(e => console.error(e))
    } else {
      next({ path: '/login' });
    }
  }
});

export default router