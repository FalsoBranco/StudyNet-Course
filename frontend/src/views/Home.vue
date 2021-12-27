<script>
import { ref } from 'vue'
import { onMounted } from 'vue-demi'
import axios from 'axios'
import CourseItem from '../components/CourseItem.vue'
export default {
  name: 'home',
  components: { CourseItem },
  setup() {
    const newCourses = ref([])
    onMounted(() => {
      axios
        .get('/api/v1/courses/new-courses')
        .then((response) => {
          newCourses.value = response.data
        })
        .catch((err) => {
          console.log(err)
        })
    })
    return {
      newCourses,
    }
  },
}
</script>

<template>
  <div class="home">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Welcome to StudyNet</h1>
        <h2 class="subtitle">An online place for learning what you want</h2>
      </div>
    </div>
    <section class="section">
      <div class="container">
        <div class="columns is-multiline">
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info">
                <i class="far fa-comments"></i>
              </span>
              <h2 class="is-size-4 my-4">Study at your own pace</h2>
              <p>This is just some random placeholder text</p>
            </div>
          </div>

          <div class="column is-12 has-text-centered">
            <router-link to="/signup" class="button is-info is-size-3 my-6"
              >Click to get started</router-link
            >
          </div>
          <div v-for="course in newCourses" :key="course" class="column is-3">
            <CourseItem :course="course" />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
