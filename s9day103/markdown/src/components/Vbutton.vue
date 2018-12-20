<template>
<button class="btn" :class="currentBtn">
  <slot>
    按钮
  </slot>
</button>
</template>

<script>
export default {
  name:'Vbutton',
  data(){
    return{

    }
  },
  props: {
    typed:String
  },
  computed:{
    currentBtn(){
      return {
        "btn-success": this.typed == 'success'?true:false,
        "btn-info": this.typed == 'info'?true:false,
        "btn-danger": this.typed == 'danger'?true:false,
      }
    }
  }
}
</script>

<style scoped>
</style>
