<script>
import { onMounted, ref } from 'vue'
import CourseItem from '../../components/CourseItem.vue'
import CourseService from '../../services/CourseService'
import CategoryService from '../../services/CategoryService'
export default {
  setup() {
    const courses = ref([])
    const categories = ref([])
    const activeCategory = ref({})

    function setActiveCategory(category) {
      activeCategory.value = category
      getCoursesByCategory()
    }

    function getCoursesByCategory() {
      CourseService.listByCategory(activeCategory.value).then(
        (response) => (courses.value = response.data)
      )
    }

    onMounted(() => {
      CourseService.listAll().then((response) => (courses.value = response.data))
      CategoryService.listAll().then((response) => (categories.value = response.data))
      getCoursesByCategory()
    })
    return { courses, categories, activeCategory, setActiveCategory }
  },
  components: { CourseItem },
}
</script>

<template>
  <div class="courses">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">Courses</h1>
      </div>
    </div>
    <section class="section">
      <div class="container">
        <div class="columns">
          <!-- Section Sidebar -->
          <div class="column is-2">
            <aside class="menu">
              <p class="menu-label">Categories</p>
              <ul class="menu-list">
                <li>
                  <a
                    :class="{ 'is-active': !activeCategory.id }"
                    @click="setActiveCategory({})"
                    href="#"
                    >All courses</a
                  >
                </li>
                <li v-for="category in categories" :key="category.id">
                  <a
                    :class="{ 'is-active': activeCategory.id === category.id }"
                    @click="setActiveCategory(category)"
                    href="#"
                    >{{ category.title }}</a
                  >
                </li>
              </ul>
            </aside>
          </div>
          <!-- End Section Sidebar -->

          <div class="column is-10">
            <div class="columns is-multiline">
              <div v-for="course in courses" :key="course.id" class="column is-4">
                <!-- Section card -->
                <CourseItem :course="course" />
                <!-- End Section Card -->
              </div>

              <!-- Section Pagination -->
              <div class="column is-12">
                <nav class="pagination">
                  <a href="#" class="pagination-previous">Previous</a>
                  <a href="#" class="pagination-next">Next</a>
                  <ul class="pagination-list">
                    <li>
                      <a href="" class="pagination-link is-current">1</a>
                    </li>
                    <li>
                      <a href="" class="pagination-link">2</a>
                    </li>
                  </ul>
                </nav>
              </div>
              <!-- End Section Pagination -->
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
