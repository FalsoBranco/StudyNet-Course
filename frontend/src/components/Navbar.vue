<script setup>
import { useUserStore } from '../stores/user'
</script>

<template>
  <nav class="navbar is-info" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a href="/" class="navbar-item is-size-4">StudyNet</a>
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
          <template v-if="!useUserStore().userAuthentication">
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
