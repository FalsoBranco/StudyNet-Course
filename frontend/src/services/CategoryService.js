import http from '../plugins/axios'

class CategoryService {
  listAll() {
    return http.get('/api/v1/courses/categories/')
  }
}

export default new CategoryService()
