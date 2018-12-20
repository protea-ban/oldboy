import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Vmain from '@/components/Vmain'
import Vcourse from '@/components/Vcourse'
import Vdetail from '@/components/Vdetail'
import Vmicro from '@/components/Vmicro'
import Vnews from '@/components/Vnews'
import Vlogin from '@/components/Vlogin'

Vue.use(Router);

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'Vmain',
      component: Vmain
    },
    {
      path: '/course',
      name: 'Vcourse',
      component: Vcourse
    },
    {
      path: '/detail/:id',
      name: 'detail',
      component: Vdetail
    },
    {
      path: '/micro',
      name: 'micro',
      component: Vmicro,
      meta:{
        requireAuth:true
      }

    },
    {
      path: '/news',
      name: 'news',
      component: Vnews,
      meta:{
        requireAuth:true
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Vlogin
    },
  ]
})
