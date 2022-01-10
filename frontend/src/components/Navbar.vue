<script setup>
import { computed } from 'vue'
import { useUserStore } from '../stores/user'

const UserStore = useUserStore()

const isLogged = computed(() => {
  return UserStore.token ? true : false
})
</script>

<template>
  <nav class="navbar is-info" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item is-size-4">StudyNet</router-link>
    </div>

    <div class="navbar-menu" id="navbar-item">
      <div class="navbar-start">
        <router-link class="navbar-item" to="/">Home</router-link>
        <router-link class="navbar-item" to="/about">About </router-link>
        <router-link class="navbar-item" to="/courses">Courses </router-link>
      </div>
    </div>
    <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
          <template v-if="!isLogged">
            <router-link to="/signup" class="button is-primary">
              <strong>Sign up</strong>
            </router-link>
            <router-link to="/log-in" class="button is-light"> Log in </router-link>
          </template>
          <template v-else>
            <router-link :to="{ name: 'Account' }" class="button is-info">Dashboard</router-link>
          </template>
        </div>
      </div>
    </div>
  </nav>
</template>
