import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({ isAuthenticated: false, token: '' }),
  getters: {
    userToken: (state) => state.token,
    userAuthentication: (state) => state.isAuthenticated,
  },
  actions: {
    initializeStore() {
      let token = localStorage.getItem('token')
      if (token) {
        this.token = token
        this.isAuthenticated = true
      } else {
        this.token = ''
        this.isAuthenticated = false
      }
    },
    setToken(token) {
      this.token = token
    },
    removeToken() {
      this.token = ''
      this.isAuthenticated = false
    },
  },
})
