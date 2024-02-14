import axios from "axios";
import store from "@/store";

const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1/',
});

// Interceptador para configurar cabeçalho de autorização.
// A cada query realizada à api, caso o usuário esteja logado, envia um token de
// autorização gerado no momento do login.
api.interceptors.response.use(
  response => response,
  error => {
    if (error.response && error.response.status === 401) {
      // Token de acesso inválido, limpar o token armazenado no localStorage
      store.commit("removeToken");
    }
    return Promise.reject(error);
  },
);

api.interceptors.request.use(
  config => {
    const token = localStorage.getItem('token');

    if (token) {
      config.headers.Authorization = `Token ${token}`;
    }

    return config;
  }
);

export default api;
