## 组件的使用

组件其实就是一小块一小块的功能块，这些功能块以 Vue 的方式进行了简写，并且可以重复利用，解耦。

#### 声明
```javascript
Vue.component('组件名',{
  data:function(){
    // 该处的data只能是函数
  },
  template:`以模板字符串为基础的模板`
})
```

```javascript
Vue.component(
      'Vheader',{
        data:function(){

        },
        template:`<div class="header">
                    <div class="w">
                      <div class="w-1">
                        <img src="./1.png" alt="777">
                      </div>
                      <div class="w-r">
                        <button>注册</button>
                        <button>登录</button>
                      </div>
                    </div>
                  </div>`
      }
    )
```

#### 在Vue中使用

先实例化一个 Vue ，

```javascript
var music = new Vue({
  el:"#app",
  data:{
    // 此处一定要返回数据，没有就返回一个空
    return {}

  },
  methods: {

  },
  computed:{

  }
})
```
在实例化 Vue 的内部可以以 `<组件名></组件名>` 的方式使用组件。

```html
<div id="app">
  <Vheader></Vheader>
  <Vheader></Vheader>
</div>
```
### vue-cli 的使用

安装，一定要加 `-g` 使之全局都能使用。

  `npm install -g vue-cli`

常用命令：
- 查看版本： `vue -V`
- 查看帮助：`vue --help`
- 查看模板： `vue list`

生成 vue-cli 项目

`vue init web-pack 01`

当显示`Use Sass?`提示时，选择 N 。安装成功后，会显示帮助，让进入项目目录中，运行 `npm install` 命令进行初始化，运行 `npm run dev` 来运行整个 vue-cli 项目。

此时，在浏览器中打开 `http://localhost:8080/`，得到项目的页面。只要不在 cmd 中关闭项目，更改代码会使得页面自动刷新。

在 vue-cli 项目下， main.js 是主要入口文件，App.vue 是默认组件文件。组件在 App.vue 文件中编辑。其中，`<template></template>` 中是页面结构，`<script></script>`中的是页面的业务逻辑，type 千万不能带，`<style></sytle>`中的是样式。

在 main.js 中有 `import App from './App.vue'` 说明在文件 App.vue 中肯定得需要 export default 。

```javascript
export default{
  name:"App",
  data(){
    return{
      msg:"hello world"
    }
  }
}
```
在 export default 中一定得有 `data(){}` 函数，且函数中一定要返回值，没有值也要返回空。在函数中返回的值可以用在 `<template></template>` 中。

export default 中都可以写之前 Vue 中内容。

注意：`<template></template>` 中只能有一个 div 大标签，其他标签都应该在这个 div 标签里面。

### 使用自己的组件
#### 创建
在 src 下面建立一个文件夹（components），里面存放自己定义的 vue 文件，即组件文件。

#### 引入
在 App.vue 文件中引入自定义的组件文件：
在 script 标签中 import 自定义的组件，其中文件类型 .vue 可以省略。
`import Vheader from './components/Vheader'`

#### 挂载

在 export default 里的 `components：{}` 中挂载组件，只写 name 默认表示为 `name：name` 。

```javascript
components: {
  Vheader
}
```

#### style 里的问题

为了给每个组件设置不同的样式，并使其不相互干扰，需要在 style 中加入 scoped 属性。如果没有 scoped 这个属性，所有的样式会被最后一个使用的组件样式所覆盖。
