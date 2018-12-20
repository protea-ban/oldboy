<template>
<div class="container">
  <div class="row">
    <div class="col-md-12">
      <div class="panel panel-default">
        <div class="panel-heading">
          <h3 class="panel-title">用户登录</h3>
        </div>
        <div class="panel-body">
        <p>
          <input type="text" placeholder="请输入用户名" v-model="username">
        </p>
        <p>
          <input type="password" placeholder="请输入密码" v-model="password">
        </p>
          <p>
            <input type="button" value="登录" @click="doLogin">
          </p>
        </div>
      </div>
    </div>
  </div>
</div>
</template>
<script>
  export default{
    name: "Vlogin",
    data(){
      return {
        username:'',
        password:''
      }
    },
    methods:{
      doLogin(){
        var that = this;
        this.$axios.request({
          url:'http://127.0.0.1:8000/api/v1/auth/',
          method:'POST',
          data:{
            user:this.username,
            pwd:this.password
          },
          headers:{
            'Content-Type': 'application/json',
          },
        }).then(function (arg) {
          // console.log(that.username);
          if(arg.data.code === 1000){
            // 将token和username放到Cookie中
            that.$store.commit('saveToken', {username:that.username, token:arg.data.token});

            // 跳转到登录前的页面 query.backUrl是自己定义的
            var url = that.$route.query.backUrl;
            if (url){
              that.$router.push({path:url})
            }else {
              that.$router.push({path:'/'})
            }
          }else {
            alert(arg.data.error);
          }
        }).catch(function (arg) {
          console.log('发生错误');

        })


      }
    }
  }

</script>

<style scoped>

</style>
