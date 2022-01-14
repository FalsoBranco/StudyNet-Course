<script setup>
import router from '../../router'
import AuthService from '../../services/AuthService'
import { useUserStore } from '../../stores/user'
import Hero from '../../layout/Hero.vue'
import Section from '../../layout/Section.vue'
import axios from '../../plugins/axios'

const store = useUserStore()

const userToken = store.userToken

const logout = async (token) => {
  AuthService.logout(token)
    .then((response) => {
      // response.data
    })
    .catch((error) => console.log(error.message))
  localStorage.removeItem('token')
  store.removeToken()
  router.push('/')
}
</script>

<template>
  <div class="account">
    <Hero> Welcome to StudyNet </Hero>
    <Section>
      <button @click="logout(userToken)" class="btn is-danger">Log out</button>
    </Section>
  </div>
</template>
