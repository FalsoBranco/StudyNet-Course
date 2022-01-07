<script setup>
import Navbar from '@/components/Navbar.vue'
import axios from './plugins/axios'
import Footer from './components/Footer.vue'
import { useUserStore } from './stores/user'

const store = useUserStore()
store.initializeStore()

const token = store.userToken
if (token) {
  axios.defaults.headers.common['Authorization'] = 'token' + token.value
} else {
  axios.defaults.headers.common['Authorization'] = ''
}
</script>

<template>
  <Navbar />
  <router-view />
  <Footer />
</template>

<style lang="scss"></style>
