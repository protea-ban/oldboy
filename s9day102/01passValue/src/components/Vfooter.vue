<template>
  <div class="footer">
    <button @click="addCity">添加一个城市</button>
  </div>
</template>
<script>
export default {
  name: "Vfooter",
  data: () => ({

  }),
  methods: {
    addCity() {
      this.$emit('addMyCity','杭州')
    }
  }
}
</script>
<style scoped>
</style>
