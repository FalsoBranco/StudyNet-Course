<script setup>
import http from '../../plugins/axios'
import { ref, reactive } from 'vue'
import router from '../../router'
import AuthService from '../../services/AuthService'
import { useUserStore } from '../../stores/user'
import { validateLogin } from './helper'

const UserStore = useUserStore()
const user = reactive({
  username: '',
  password: '',
})
const errors = ref([])

const submitForm = () => {
  http.defaults.headers.common['Authorization'] = ''
  localStorage.removeItem('token')
  errors.value = []
  validateLogin(user)

  if (!errors.value.length) {
    const formData = {
      username: user.username,
      password: user.password,
    }
    AuthService.login(formData)
      .then((response) => {
        const token = response.data.auth_token
        UserStore.setToken(token)
        http.defaults.headers.common['Authentication'] = 'Token' + token
        localStorage.setItem('token', token)
        router.push({ name: 'Account' })
      })
      .catch((err) => {
        if (err.response) {
          for (let property in err.response.data) {
            errors.value.push(`${property}: ${err.response.data[property]}`)
          }
        } else if (err.message) {
          errors.value.push('Something went wrong. Please try again')
          console.log(JSON.stringify(err))
        }
      })
  }
}
</script>

<template>
  <div class="signup">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">Log in</h1>
      </div>
    </div>
  </div>
  <section class="section">
    <div class="container">
      <div class="columns">
        <div class="column is-4 is-offset-4">
          <div v-if="errors.length" class="notification is-danger">
            <p v-for="error in errors" :key="error">
              {{ error }}
            </p>
          </div>
          <form @submit.prevent="submitForm">
            <div class="field">
              <label for="username">Username</label>
              <div class="control">
                <input
                  v-model="user.username"
                  id="username"
                  name="username"
                  type="text"
                  class="input"
                />
              </div>
            </div>
            <div class="field">
              <label for="password">Password</label>
              <div class="control">
                <input
                  v-model="user.password"
                  id="password"
                  name="password"
                  type="password"
                  class="input"
                />
              </div>
            </div>

            <div class="field">
              <div class="control">
                <button class="button is-dark">Log in</button>
              </div>
            </div>
          </form>
          <p>Or <router-link to="/signup">click here</router-link> to sing up!</p>
        </div>
      </div>
    </div>
  </section>
</template>
