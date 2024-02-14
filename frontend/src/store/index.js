import { createStore } from "vuex";
import router from "@/router";
import api from "@/services/api";

export default createStore({
  state: {
    user: null,
    token: "",
    title: "VeloxNet",
    isAuthenticated: false,
    hideConfigButton: false,
    isPinned: true,
    color: "success",
    isNavFixed: false,
    isAbsolute: false,
    showNavs: true,
    showSidenav: true,
    showNavbar: true,
    showFooter: true,
    showMain: true,
    isDarkMode: false,
    navbarFixed:
      "position-sticky blur shadow-blur left-auto top-1 z-index-sticky px-0 mx-4",
    absolute: "position-absolute px-4 mx-0 w-100 z-index-2",
  },
  mutations: {
    initializeAuth(state) {
      // Checa se existe um token
      if (localStorage.getItem("token")) {
        state.token = localStorage.getItem("token");
        state.isAuthenticated = true;
      } else {
        state.token = "";
        state.isAuthenticated = false;
      }
    },
    setToken(state, token) {
      state.token = token;
      localStorage.setItem("token", token);
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = "";
      localStorage.removeItem("token");
      state.isAuthenticated = false;
    },
    toggleConfigurator(state) {
      state.showConfig = !state.showConfig;
    },
    navbarMinimize(state) {
      const sidenav_show = document.querySelector(".g-sidenav-show");

      if (sidenav_show.classList.contains("g-sidenav-pinned")) {
        sidenav_show.classList.remove("g-sidenav-pinned");
        state.isPinned = true;
      } else {
        sidenav_show.classList.add("g-sidenav-pinned");
        state.isPinned = false;
      }
    },
    navbarFixed(state) {
      if (state.isNavFixed === false) {
        state.isNavFixed = true;
      } else {
        state.isNavFixed = false;
      }
    },
    toggleEveryDisplay(state) {
      state.showNavbar = !state.showNavbar;
      state.showSidenav = !state.showSidenav;
      state.showFooter = !state.showFooter;
    },
    toggleHideConfig(state) {
      state.hideConfigButton = !state.hideConfigButton;
    },
    color(state, payload) {
      state.color = payload;
    },
    setUser(state, user) {
      state.user = user;
    },
    removeUser(state) {
      state.user = null;
    },
    setTitle(state, title) {
      state.title = title;
    }
  },
  actions: {
    setColor({ commit }, payload) {
      commit("color", payload);
    },
    logout({ commit }) {
      api.post('usuarios/auth/token/logout').then(() => {
        commit('removeToken');
        commit('removeUser');
        router.push('/')
      }).catch(e => console.error(e));
    },
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
    token: (state) => state.token,
    user: (state) => state.user,
  },
});
