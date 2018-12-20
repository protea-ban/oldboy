<template>
<div class="container">
  <div class="row">
    <div class="col-md-12">
      <div class="panel panel-default">
        <div class="panel-heading">
          <h3 class="panel-title">课程详情</h3>
        </div>
        <div class="panel-body">
          <p>{{detail.course}}</p>
          <p>{{detail.img}}</p>
          <p>{{detail.level}}</p>
          <p>{{detail.slogon}}</p>
          <p>{{detail.title}}</p>
          <p>{{detail.why}}</p>
          <div>
            <ul v-for="item in detail.chapter">
              <li>{{item.name}}</li>
            </ul>
          </div>
          <div>
            <h3>推荐课程</h3>
            <ul v-for="item in detail.recommends">
              <!--<li>{{item.title}}</li>-->
              <!--方法一 失败 只是换了url 没有进行组件重新加载 -->
              <!--<li><router-link :to="{name:'detail', params:{id:item.id}}">{{item.title}}</router-link></li>-->

              <li @click="changeDetail(item.id)">{{item.title}}</li>
            </ul>
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
        detail:{
          course:null,
          img:null,
          level:null,
          slogon:null,
          title:null,
          why:null,
          chapter:[],
          recommends:[],
        }
      }
    },
    mounted:function () {
      // Vue页面加载时自动执行

      // 初始化时是获取url中的id
      var nid = this.$route.params.id;
      this.initDetail(nid);
    },
    methods:{
      initDetail(nid){
        // 现在是直接传id值
        // 通过ajax向接口发送请求，并获取课程列表
        // axios 发送ajax请求
        // 第一步：在main.js中设置
        // 第二步：使用axios发送请求

        var that = this;

        // 获取url中的id
        // var nid = this.$route.params.id;
        this.$axios.request({
          url:'http://127.0.0.1:8000/api/v1/course/'+ nid + '/',
          method:'GET'
        }).then(function (ret) {
          // ajax请求发送成功后，获取响应的内容
          if(ret.data.code === 1000){
            that.detail = ret.data.data;
          }else{
            alert(ret.data.error);

          }
        }).catch(function (ret) {
          // ajax请求发送失败后，获取响应的内容
        })
      },
      changeDetail(id){
        // 重新定向页面
        this.initDetail(id);
        // push重新加载组件
        this.$router.push({name:'detail', params:{id:id}});
      }
    }
  }
</script>

<style scoped>

</style>
