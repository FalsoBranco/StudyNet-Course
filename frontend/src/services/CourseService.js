import http from '../plugins/axios'

class CourseService {
  listFrontpage() {
    return http.get('/api/v1/courses/new-courses/')
  }
  listFrontpage1() {
    let data = 1
    http.get('/api/v1/courses/new-courses/').then((response) => {
      data = response.data
    })
    return data
  }
}

export default new CourseService()
