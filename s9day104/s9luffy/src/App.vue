<template>
  <div id="app">
    <Vheader></Vheader>
    <router-view/>
  </div>
</template>

<script>
// 引入bootstrap
import 'bootstrap/dist/css/bootstrap.min.css'
import Vheader from './components/Vheader'
export default {
  name: 'App',
  components:{
    Vheader
  }
}
</script>

<style>

</style>
