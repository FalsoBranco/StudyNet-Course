import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

import 'buefy/dist/buefy.css'

const app = createApp(App)

app.config.productionTip = true

app.use(createPinia())
app.use(router)
app.mount('#app')
