<script setup>
import axios from 'axios'
import { onMounted, reactive, ref } from 'vue-demi'
import { useUserStore } from '../../stores/user'
import { useRoute } from 'vue-router'
import CourseService from '../../services/CourseService'
import CommentService from '../../services/CommentService'
import QuizService from '../../services/QuizService'

const store = useUserStore()

const route = useRoute()
const courseSlug = route.params.slug
const course = ref({})
const errors = ref([])
const comments = ref([])
const comment = reactive({
  name: '',
  content: '',
})
const quiz = ref({})
const quizResult = ref('')
const selectedAnswer = ref('')
const activeLesson = ref(null)

onMounted(() => {
  CourseService.getDetail(courseSlug, store.userToken).then((response) => {
    const data = response.data
    course.value = data
    document.title = course.value.title
  })
})

function submitComment() {
  errors.value = []
  if (comment.name === '') {
    errors.value.push('the name must be filled out')
  }
  if (comment.content === '') {
    errors.value.push('the content must be filled out')
  }
  if (!errors.value.length) {
    console.log(courseSlug)
    CommentService.create(courseSlug, activeLesson.value.slug, comment, store.userToken)
      .then((response) => {
        comment.name = ''
        comment.content = ''
        comments.value.push(response.data)
      })
      .catch((err) => console.log(err.message))
  }
}
function submitQuiz() {
  if (selectedAnswer.value) {
    if (selectedAnswer.value === quiz.value.answer) {
      quizResult.value = 'correct'
    } else {
      quizResult.value = 'incorrect'
    }
  } else {
    alert('Select answer first')
  }
}
function setActiveLesson(lesson) {
  activeLesson.value = lesson
  if (lesson.lesson_type === 'quiz') {
    getQuiz()
  } else {
    getComments()
  }
  console.log(activeLesson)
}
function getComments() {
  CommentService.listAll(courseSlug, activeLesson.value.slug, store.userToken).then((response) => {
    comments.value = response.data
  })
}
function getQuiz() {
  console.log(activeLesson.value.slug)
  QuizService.listAll(courseSlug, activeLesson.value.slug, store.userToken).then((response) => {
    quiz.value = response.data
  })
}
</script>
<template>
  <div class="courses">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">{{ course.title }}</h1>
      </div>
    </div>
    <section class="section">
      <div class="container">
        <div class="columns content">
          <div class="column is-2">
            <h2>Table of contents</h2>

            <ul>
              <li v-for="lesson in course.lessons" :key="lesson.id">
                <a @click="setActiveLesson(lesson)" href="#">{{ lesson.title }}</a>
              </li>
            </ul>
          </div>
          <div class="column is-10">
            <template v-if="store.userAuthentication">
              <template v-if="activeLesson">
                <h2>{{ activeLesson.title }}</h2>
                {{ activeLesson.long_description }}
                <hr />
                <template v-if="activeLesson.lesson_type === 'quiz'">
                  <h3>{{ quiz.question }}</h3>
                  <div class="control">
                    <label for="opt1" class="radio">
                      <input
                        type="radio"
                        name="quiz_answer"
                        id="opt1"
                        :value="quiz.opt1"
                        v-model="selectedAnswer"
                      />{{ quiz.opt1 }}
                    </label>
                  </div>
                  <div class="control">
                    <label for="opt2" class="radio">
                      <input
                        type="radio"
                        name="quiz_answer"
                        id="opt2"
                        :value="quiz.opt2"
                        v-model="selectedAnswer"
                      />{{ quiz.opt2 }}
                    </label>
                  </div>
                  <div class="control">
                    <label for="opt3" class="radio">
                      <input
                        type="radio"
                        name="quiz_answer"
                        id="opt3"
                        :value="quiz.opt3"
                        v-model="selectedAnswer"
                      />{{ quiz.opt3 }}
                    </label>
                  </div>
                  <div class="control mt-4">
                    <button class="button is-info" @click="submitQuiz">Submit</button>
                  </div>

                  <template v-if="quizResult === 'correct'">
                    <div class="notification is-success mt-4">Correct</div>
                  </template>
                  <template v-else-if="quizResult === 'incorrect'">
                    <div class="notification is-danger mt-4">Try Again</div>
                  </template>
                </template>
                <template v-if="activeLesson.lesson_type === 'article'">
                  <article v-for="comment in comments" :key="comment.id" class="media box">
                    <div class="media-content">
                      <div class="content">
                        <p>
                          <strong>{{ comment.name }}</strong> {{ comment.created_at }}
                        </p>
                        {{ comment.content }}
                      </div>
                    </div>
                  </article>

                  <form @submit.prevent="submitComment">
                    <div class="field">
                      <label for="name" class="label">Name</label>
                      <div class="control">
                        <input
                          v-model="comment.name"
                          type="text"
                          class="input"
                          name="name"
                          id="name"
                        />
                      </div>
                    </div>
                    <div class="field">
                      <label for="content" class="label">Content</label>
                      <div class="control">
                        <textarea
                          v-model="comment.content"
                          class="textarea"
                          name="content"
                          id="content"
                        />
                      </div>
                    </div>
                    <div
                      v-for="(error, index) in errors"
                      :key="index"
                      class="notification is-danger"
                    >
                      {{ error }}
                    </div>
                    <div class="field">
                      <div class="control">
                        <button class="button is-link">Submit</button>
                      </div>
                    </div>
                  </form>
                </template>
              </template>
              <template v-else>
                <h2>Introduction</h2>
                <p>
                  {{ course.long_description }}
                </p>
              </template>
            </template>
            <template v-else>
              <h2>Restricted access</h2>
              <p>You need to have an account to continue</p>
            </template>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
