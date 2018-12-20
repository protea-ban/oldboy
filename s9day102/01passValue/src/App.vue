<template>
<div class="">
  <!-- <Vheader></Vheader> -->
  <!-- 绑定cityArr属性，用来传值 -->
  <!-- <Vcontent :cityArr='citys'></Vcontent> -->
  <!-- <Vfooter v-on:addMyCity = 'addOneCity'></Vfooter> -->
  <h1>hello ban</h1>
  <div class="">
    <!-- 使用 router-link 组件来导航. -->
    <!-- 通过传入 `to` 属性指定链接. -->
    <!-- <router-link> 默认会被渲染成一个 `<a>` 标签 -->
    <router-link to="/">Vheader</router-link>
    <router-link to="/citys">Vcontent</router-link>
    <router-link to="/addCity">Vfooter</router-link>
  </div>
  <!-- 路由出口 -->
  <!-- 路由匹配到的组件将渲染在这里 -->
  <router-view></router-view>
</div>
</template>

<script>
// 引入组件
import Vheader from './components/Vheader'
import Vcontent from './components/Vcontent'
import Vfooter from './components/Vfooter'

export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      citys:['北京','上海','广州','深圳']
    }
  },
  components:{
    Vheader,
    Vcontent,
    Vfooter,
  },
  methods: {
    addOneCity(str) {
      this.citys.push(str)
    }
  }
}
</script>

<style>
*{
  padding: 0;
  margin: 0;
}
</style>
