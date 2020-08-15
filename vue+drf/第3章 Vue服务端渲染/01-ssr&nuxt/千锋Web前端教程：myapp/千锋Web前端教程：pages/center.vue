<template>
  <div>
    center
    <ul>
      <li v-for="data in datalist" :key="data">
        {{data}}
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  data(){
    return{
      datalist:["1111","2222","333"]
    }
  }
}
</script>
<style lang="scss" scoped>

</style>
