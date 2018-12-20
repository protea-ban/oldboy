<template>
  <div class="content">
    <ul>
      <li v-for="item in cityArr" :key="item.key">
        {{item}}
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  name: "Vcontent",
  data: () => ({

  }),
  props: {
    cityArr:Array
  }
}
</script>
<style scoped>
</style>
