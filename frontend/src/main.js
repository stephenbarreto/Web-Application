import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import materialDashboard from './themes/material-dashboard'

createApp(App).use(store).use(router).use(materialDashboard).mount('#app')
