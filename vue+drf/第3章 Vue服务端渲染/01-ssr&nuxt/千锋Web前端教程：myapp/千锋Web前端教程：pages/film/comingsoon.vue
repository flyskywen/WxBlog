<template>
  <div>
    comignsoon
    <ul>
      <li v-for="data in datalist" :key="data.id">
        {{data.nm}}
      </li>
    </ul>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  asyncData(data) {
    // console.log();
    return axios({
      url:process.server?"http://m.maoyan.com/ajax/movieOnInfoList?token=":"/ajax/movieOnInfoList?token=",
    }).then(res=>{
      console.log(res.data);
      return {
        datalist:res.data.movieList
      }// 状态
    })
  }
}
</script>
<style lang="scss" scoped>

</style>
