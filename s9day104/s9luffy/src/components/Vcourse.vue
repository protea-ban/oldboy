<template>
<div class="container">
  <div class="row">
    <div class="col-md-12">
      <div class="panel panel-default">
        <div class="panel-heading">
          <h3 class="panel-title">我的课程</h3>
        </div>
        <div class="panel-body">
          <div v-for="item in courseList">
            <div style="width: 350px;float: left">
              <h3><router-link :to="{name:'detail', params:{id:item.id}}">{{item.title}}</router-link></h3>
              <p>{{item.level}}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>
<script>
  export default{
    name: "Vcourse",
    data(){
      return {
        courseList:[]
      }
    },
    mounted:function () {
      // Vue页面加载时自动执行
      this.initCourse();
    },
    methods:{
      initCourse(){
        // 通过ajax向接口发送请求，并获取课程列表
        // axios 发送ajax请求
        // 第一步：在main.js中设置
        // 第二步：使用axios发送请求

        var that = this;

        this.$axios.request({
          url:'http://127.0.0.1:8000/api/v1/course/',
          method:'GET'
        }).then(function (ret) {
          // ajax请求发送成功后，获取响应的内容
          if(ret.data.code === 1000){
            // console.log(ret.data.data);
            that.courseList = ret.data.data;
          }else{
            alert('----');

          }
        }).catch(function (ret) {
          // ajax请求发送失败后，获取响应的内容
        })
      }
    }
  }
</script>

<style scoped>

</style>
