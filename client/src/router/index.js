import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Registration from "../views/Registration.vue"
import FileList from "../views/FileList.vue"
Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/registration',
    name: 'Registration',
    component: Registration,
  },
  {
    path: "/filelist",
    name: 'filelist',
    component: FileList
  }
]

const router = new VueRouter({
  routes
})

export default router
