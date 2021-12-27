<script setup>
import axios from 'axios'
import { ref } from 'vue'
import router from '../router'

const username = ref('')
const email = ref('')
const password = ref('')
const password2 = ref('')
const errors = ref([])

const submitForm = () => {
  if (username.value === '') {
    errors.value.push('The username is missing')
  }
  if (email.value === '') {
    errors.value.push('The email is missing')
  }
  if (password.value === '') {
    errors.value.push('The password is missing')
  }
  if (password.value !== password2.value) {
    errors.value.push('The password ate not matching')
  }
  if (!errors.value.length) {
    const formData = {
      username: username.value,
      password: password.value,
      email: email.value,
    }
    axios
      .post('/api/v1/users/', formData)
      .then((response) => {
        router.push('/log-in')
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
        <h1 class="title">Sign up</h1>
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
                <input v-model="username" id="username" name="username" type="text" class="input" />
              </div>
            </div>
            <div class="field">
              <label for="email">Email</label>
              <div class="control">
                <input v-model="email" id="email" name="email" type="text" class="input" />
              </div>
            </div>
            <div class="field">
              <label for="password">Password</label>
              <div class="control">
                <input
                  v-model="password"
                  id="password"
                  name="password"
                  type="password"
                  class="input"
                />
              </div>
            </div>
            <div class="field">
              <label for="password2">Repeat Password</label>
              <div class="control">
                <input
                  v-model="password2"
                  id="password2"
                  name="password2"
                  type="password"
                  class="input"
                />
              </div>
            </div>
            <div class="field">
              <div class="control">
                <button class="button is-dark">Sing up</button>
              </div>
            </div>
          </form>

          <p>Or <router-link to="/log-in">click here</router-link> to log in!</p>
        </div>
      </div>
    </div>
  </section>
</template>
