<template>
<div class="container">
  <div class="row">
    <div class="col-md-12">
      <div class="panel panel-default">
        <div class="panel-heading">
          <h3 class="panel-title">官网首页</h3>
        </div>
        <div class="panel-body">
        <ul>
          <li><a href='#'>我的笔记</a></li>
          <li><a href='#'>我的博客</a></li>
          <li><a href='#'>我的公司信息</a></li>
          <li><a href='#'>我的女朋友</a></li>
        </ul>
        </div>
      </div>
    </div>
  </div>
</div>
</template>
<script>
  export default{
    name: "Vmain",
    data(){
      return {

      }
    },
    created(){
      console.log(this.$route);
    }

  }
</script>

<style scoped>

</style>
