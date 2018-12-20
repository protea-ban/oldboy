<template>
  <div class="">
    <h1>测试</h1>
    <Vbutton typed = 'success'>测试按钮</Vbutton>
    <Vbutton typed = 'info'>info按钮</Vbutton>
    <Vbutton typed = 'danger'>danger按钮</Vbutton>

  </div>

</template>

<script>
import Vbutton from './Vbutton'
export default {
  name:'Vtest',
  data(){
    return{

    }
  },
  components:{
    Vbutton
  }
}
</script>

<style scoped>
</style>
