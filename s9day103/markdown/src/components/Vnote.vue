<template>
<div class="container">
  <div class="row">
    <div class="col-md-3">
      <div class="panel panel-default">
        <div class="panel-heading">
          <h3 class="panel-title">我的笔记列表</h3>
        </div>
        <div class="panel-body">
          <!-- 笔记列表 -->
          <VnoteShow></VnoteShow>
        </div>
      </div>
    </div>

    <div class="col-md-9">
      <div class="panel panel-default">
        <div class="panel-heading">
          
        </div>
        <div class="panel-body">
          <Vmark></Vmark>
          <!-- markdown编辑器 -->
        </div>
      </div>

    </div>
  </div>
</div>
</template>
<script>
  import VnoteShow from './VnoteShow'
  import Vmark from './Vmark'
  export default{
    name: "Vnote",
    data(){
      return {
        noteLists:[
          {id:1,title:"今天很辛苦",content:"你说什么"},
          {id:2,title:"今天很辛苦2",content:"你说什么2"},
        ]
      }
    },
    components:{
      Vmark,
      VnoteShow
    }
  }
</script>

<style scoped>

</style>
