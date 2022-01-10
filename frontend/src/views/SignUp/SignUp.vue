<script>
import router from '../../router'

import { reactive, toRefs } from 'vue'
import AuthService from '../../services/AuthService'
import { validateRegister } from './helper'

export default {
  setup() {
    const registerState = reactive({
      username: '',
      email: '',
      password: {
        password: '',
        confirm: '',
      },
      errors: [],
    })

    const submitForm = () => {
      registerState.errors = validateRegister(registerState)

      if (!registerState.errors.length) {
        const formData = {
          username: registerState.username,
          password: registerState.password.password,
          email: registerState.email,
        }

        AuthService.register(formData)
          .then((response) => router.push('/log-in'))
          .catch((error) => {
            console.log(error)
            if (error.response) {
              for (let property in error.response.data) {
                registerState.errors.push(`${property}: ${error.response.data[property]}`)
              }
            } else if (error.message) {
              registerState.errors.push('Something went wrong. Please try again')
              console.log(JSON.stringify(err))
            }
          })
      }
    }

    return {
      ...toRefs(registerState),
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
                  v-model="password.password"
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
                  v-model="password.confirm"
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
