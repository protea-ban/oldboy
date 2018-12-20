// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

// 全局配置 element-ui
import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(Element, { size: 'small', zIndex: 3000 })
Vue.config.productionTip = false

// // 引入Vuex
// import Vuex from 'vuex'
// Vue.use(Vuex);
//
// // 如果在模块化构建系统中，请确保在开头调用了 Vue.use(Vuex)
// const store = new Vuex.Store({
//   state: {
//     // 这里面的状态跟每个组件的数据数据属性有关系
//     allList:[]
//   },
//   mutations: {
//
//   }
// })


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  // store,
  components: { App },
  template: '<App/>'
})
