<script setup>
import Navbar from '@/components/Navbar.vue'
import axios from './plugins/axios'
import Footer from './components/Footer.vue'
import { useUserStore } from './stores/user'

const store = useUserStore()
store.initializeStore()
</script>

<template>
  <Navbar />
  <router-view />
  <Footer />
</template>

<style lang="scss"></style>
