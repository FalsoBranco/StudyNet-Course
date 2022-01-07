import http from '../plugins/axios'
class CommentService {
  listAll(courseSlug, lesson, token) {
    return http.get(`/api/v1/courses/${courseSlug}/${lesson}/get-comments/`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    })
  }
  create(course, lesson, comment, token) {
    return http.post(`/api/v1/courses/${course}/${lesson}/`, comment, {
      headers: {
        Authorization: `Token ${token}`,
      },
    })
  }
}

export default new CommentService()
