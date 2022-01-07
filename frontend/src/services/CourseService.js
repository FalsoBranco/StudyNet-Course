import http from '../plugins/axios'

class CourseService {
  listFrontpage() {
    return http.get('/api/v1/courses/new-courses/')
  }
  listAll() {
    return http.get('/api/v1/courses/')
  }
  listByCategory({ id }) {
    if (!id) {
      return this.listAll()
    }
    return http.get(`/api/v1/courses/?category_id=${id}`)
  }
  getDetail(slug, token) {
    return http.get(`/api/v1/courses/${slug}`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    })
  }
}

export default new CourseService()
