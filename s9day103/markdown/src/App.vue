<template>
  <div id="app">
    <Vheader></Vheader>
    <router-view/>
  </div>
</template>

<script>
// 引入bootstrap
import 'bootstrap/dist/css/bootstrap.min.css'
// 引入模板
import Vheader from './components/Vheader'
import $ from 'jquery'
export default {
  name: 'App',
  components:{
    Vheader
  },
  // 创建后加载该方法
  created(){

  },
  // 页面加载完之后调用该方法
  mounted(){
    // ajax中的this会指向ajax，所以在这将Vue的this赋值给_this
    // var _this = this;

    // var data = [
    //   {id:1,title:"今天很辛苦",content:"你说什么"},
    //   {id:2,title:"今天很辛苦2",content:"你说什么2"},
    // ];
    // $.ajax({
    //   url:'http://127.0.0.1:9527/api/comments/',
    //   methods:'get',
    //   success:function(data){
    //     // console.log(data);
    //     _this.$store.state.allList = data;
    //   }
    // })
  }
}
</script>

<style>

</style>
