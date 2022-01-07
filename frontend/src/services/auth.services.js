import http from '../plugins/axios'

class AuthServices {
  register(userInfo) {
    console.log(userInfo)
    return http.post('/api/v1/users/', userInfo)
  }
}

export default new AuthServices()
