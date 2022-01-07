import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home/Home.vue'
import About from '../views/About/About.vue'
import SignUp from '../views/SignUp/SignUp.vue'
import LogIn from '../views/Login/LogIn.vue'
import Courses from '../views/Courses/Courses.vue'
import Course from '../views/Course/Course.vue'
import Account from '../views/Dashboard/Account.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      name: 'Home',
      path: '/',
      component: Home,
    },
    {
      name: 'About',
      path: '/about',
      component: About,
    },
    {
      name: 'SingUp',
      path: '/signup',
      component: SignUp,
    },
    {
      name: 'LogIn',
      path: '/log-in',
      component: LogIn,
    },
    {
      name: 'Account',
      path: '/dashboard/account',
      component: Account,
    },
    {
      name: 'Courses',
      path: '/courses',
      component: Courses,
    },
    {
      name: 'Course',
      path: '/course/:slug',
      component: Course,
    },
  ],
})

export default router
