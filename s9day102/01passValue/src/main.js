import Vue from 'vue'
import App from './App.vue'

import VueRouter from 'vue-router'
Vue.use(VueRouter)

import Vheader from './components/Vheader'
import Vcontent from './components/Vcontent'
import Vfooter from './components/Vfooter'

const router = new VueRouter({
  routes:[
    {path:'/',component:Vheader},
    {path:'/citys',component:Vcontent},
    {path:'/addCity',component:Vfooter},
  ]
})

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
