<template>
  <div id="app">
    {{msg}}
    <Vheader></Vheader>
    <Vcontent></Vcontent>
    <Vfooter></Vfooter>
  </div>
</template>

<script>
import Vheader from './components/Vheader'
import Vcontent from './components/Vcontent'
import Vfooter from './components/Vfooter'

export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components: {
    Vheader,
    Vcontent,
    Vfooter
  }
}
</script>

<style>

</style>
