<script setup>
import axios from 'axios'
import { onMounted, reactive, ref } from 'vue-demi'
import { useUserStore } from '../../stores/user'
import { useRoute } from 'vue-router'

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
const activeLesson = ref(null)

onMounted(() => {
  axios
    .get(`/api/v1/courses/${courseSlug}`, {
      headers: {
        Authorization: `Token ${useUserStore().token}`,
      },
    })
    .then((response) => {
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
    axios
      .post(`/api/v1/courses/${courseSlug}/${activeLesson.value.slug}/`, comment, {
        headers: {
          Authorization: `Token ${useUserStore().token}`,
        },
      })
      .then((response) => {
        comment.name = ''
        comment.content = ''
        comments.value.push(response.data)
      })
      .catch((err) => console.log(err.message))
  }
}
function setActiveLesson(lesson) {
  activeLesson.value = lesson
  console.log(lesson)
  getComments()
}
function getComments() {
  console.log('testeGetComments')
  axios
    .get(`/api/v1/courses/${courseSlug}/${activeLesson.value.slug}/get-comments/`, {
      headers: {
        Authorization: `Token ${useUserStore().token}`,
      },
    })
    .then((response) => {
      comments.value = response.data
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
                  <div v-for="(error, index) in errors" :key="index" class="notification is-danger">
                    {{ error }}
                  </div>
                  <div class="field">
                    <div class="control">
                      <button class="button is-link">Submit</button>
                    </div>
                  </div>
                </form>
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
