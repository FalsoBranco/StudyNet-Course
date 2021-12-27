<script>
import Navbar from '@/components/Navbar.vue'
import axios from 'axios'
import { storeToRefs } from 'pinia'
import Footer from './components/Footer.vue'
import { useUserStore } from './stores/user'
export default {
  // TODO Inicialize store before create
  name: 'app',
  components: { Navbar, Footer },
  setup() {
    const store = useUserStore()
    store.initializeStore()
    // const { token } = storeToRefs(store)
    const token = store.userToken

    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token' + token.value
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
}
</script>

<template>
  <Navbar />
  <router-view />
  <Footer />
</template>

<style lang="scss"></style>
