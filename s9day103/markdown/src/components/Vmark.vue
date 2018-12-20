<template>
  <div>
    请输入文章名称：<input type="text" name="" value="">
    <button class="btn btn-success" >提交</button>
    <div class="marked">
      <textarea class="editor" v-model="markValue"></textarea>
      <div class="show" v-html="currentValue" ref="t"></div>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
  import Marked from 'marked'
  export default {
    name: 'Vmark',
    data(){
      return {
        markValue:''
      }
    },
    methods: {
      // addOneNote(){
      //     var json = {
      //       title: this.titleHandler,
      //       markdown: this.markdownHandler,
      //       content: this.$refs.t.innerText
      //     };
      //     console.log(json);
      //   this.$store.dispatch('addOneNote',json)
      // }
    },
    computed: {
      // markedStr: function () {
      //   return Marked(this.markdownHandler)
      // },
      // titleHandler:{
      //   set:function (newvalue) {
      //       this.$store.state.note.title = newvalue
      //     },
      //   get:function () {
      //     return this.$store.state.note.title
      //   }
      // },
      // markdownHandler:{
      //    set:function (newvalue) {
      //       this.$store.state.note.markdown = newvalue
      //     },
      //   get:function () {
      //     return this.$store.state.note.markdown
      //   }
      // }
      currentValue(){
        return Marked(this.markValue);
      }
    }
  }
</script>

<style scoped>
  .marked {
    width: 800px;
    height: 600px;
    margin: 0 auto;
  }

  .editor, .show {
    width: 395px;
    float: left;
    border: 1px solid black;
    height: 600px;
  }
</style>
