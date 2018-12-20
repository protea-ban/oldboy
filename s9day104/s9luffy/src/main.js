// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import store from './store/store'
// 在Vue的全局变量中设置了 $axios=axios
// 在组件中使用：this.$axios
Vue.prototype.$axios = axios;
Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});

router.beforeEach(function (to, from , next) {
  if (to.meta.requireAuth){
    // 要去的url只有登录成功后才能访问
    if(store.state.token){
      next()
    }else {
      next({name:'login',query:{backUrl:to.fullPath}})
    }
  }else {
    next()
  }
})
