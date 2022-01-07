<script setup>
import axios from 'axios'
import router from '../../router'
import AuthServices from '../../services/auth.services'
import { useUserStore } from '../../stores/user'

const store = useUserStore()

const userToken = store.userToken
const logout = async (token) => {
  AuthServices.logout(token)
    // await axios
    // .post(
    //   'api/v1/token/logout',
    //   {},
    //   {
    //     headers: {
    //       Authorization: `token ${token}`,
    //     },
    //   }
    // )
    .then((response) => {
      response.data
    })
    .catch((error) => console.log(error.message))
  axios.defaults.headers.common['Authorization'] = ''
  localStorage.removeItem('token')
  useUserStore().removeToken()
  router.push('/')
}
</script>

<template>
  <div class="home">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Welcome to StudyNet</h1>
      </div>
    </div>
    <section class="section">
      <button @click="logout(userToken)" class="btn is-danger">Log out</button>
    </section>
  </div>
</template>
