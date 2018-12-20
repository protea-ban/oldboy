<template>
  <li>
    <h2>标题</h2>
    <p>内容</p>
  </li>
</template>
<script>
  export default{
    name: "VnoteItem",
    data(){
      return {

      }
    },
    props:{
      data:Object
    }

  }
</script>

<style scoped>
ul li{
  list-style-type: none;
}
</style>
