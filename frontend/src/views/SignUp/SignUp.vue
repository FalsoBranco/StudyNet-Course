<script>
import router from '../../router'

import { reactive, toRefs } from 'vue'
import AuthServices from '../../servies/auth.services'

export default {
  setup() {
    const state = reactive({
      username: '',
      email: '',
      password: '',
      password2: '',
      errors: [],
    })

    const submitForm = () => {
      state.errors = []
      if (state.username === '') state.errors.push('The username is missing')
      if (state.email === '') state.errors.push('The email is missing')
      if (state.password === '') state.errors.push('The password is missing')
      if (state.password !== state.password2) state.errors.push('The password are not matching')
      if (!state.errors.length) {
        const formData = {
          username: state.username,
          password: state.password,
          email: state.email,
        }

        AuthServices.register(formData)
          .then((response) => router.push('/log-in'))
          .catch((error) => {
            console.log(error)
            if (error.response) {
              for (let property in error.response.data) {
                state.errors.push(`${property}: ${error.response.data[property]}`)
              }
            } else if (error.message) {
              state.errors.push('Something went wrong. Please try again')
              console.log(JSON.stringify(err))
            }
          })
      }
    }

    return {
      ...toRefs(state),
      submitForm,
    }
  },
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
