import http from '../plugins/axios'
class QuizService {
  listAll(courseSlug, lesson, token) {
    return http.get(`/api/v1/courses/${courseSlug}/${lesson}/get-quiz/`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    })
  }
}

export default new QuizService()
