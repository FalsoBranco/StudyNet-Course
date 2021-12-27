import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

import router from './router'
import axios from 'axios'

import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

const app = createApp(App)

app.config.productionTip = true

axios.defaults.baseURL = 'http://localhost:8000'

app.use(createPinia())
app.use(router, axios, Buefy)
app.mount('#app')
