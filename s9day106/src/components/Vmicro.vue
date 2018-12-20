<template>
<div class="container">
  <div class="row">
    <div class="col-md-12">
      <div class="panel panel-default">
        <div class="panel-heading">
          <h3 class="panel-title">路飞学位：{{title}}</h3>
        </div>
        <div class="panel-body">
        <ul>

        </ul>
        </div>
      </div>
    </div>
  </div>
</div>
</template>
<script>
  export default{
    name: "Vmicro",
    data(){
      return {
        title:null

      }
    },
    mounted(){
      this.initMicro();
    },
    methods:{
      initMicro(){
        var that = this;

        this.$axios.request({
          url:'http://127.0.0.1:8000/api/v1/micro/',
          method: 'GET',
          // 认证时需要传参 将token传过去
          params:{
            token:this.$store.state.token
          }
        }).then(function (arg) {
          if(arg.data.code === 1000){
            that.title = arg.data.title
          }
        })
      }
    }
  }
</script>

<style scoped>

</style>
