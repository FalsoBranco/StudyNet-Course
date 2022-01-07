import http from '../plugins/axios'

class AuthServices {
  login(userInfo) {
    return http.post('/api/v1/token/login/', userInfo)
  }
  register(userInfo) {
    return http.post('/api/v1/users/', userInfo)
  }
  logout(token) {
    const config = {
      headers: {
        Authorization: `token ${token}`,
      },
    }
    return http.post('api/v1/token/logout', {}, config)
  }
}

export default new AuthServices()

// const logout = async (token) => {
//   await axios
//     .post(
//       'api/v1/token/logout',
//       {},
//       {
//         headers: {
//           Authorization: `token ${token}`,
//         },
//       }
//     )
//     .then((response) => {
//       response.data
//     })
//     .catch((error) => console.log(error.message))
//   axios.defaults.headers.common['Authorization'] = ''
//   localStorage.removeItem('token')
//   useUserStore().removeToken()
//   router.push('/')
// }
