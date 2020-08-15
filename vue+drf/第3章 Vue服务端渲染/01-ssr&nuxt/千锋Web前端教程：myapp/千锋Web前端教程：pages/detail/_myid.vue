<template>
  <div v-if="filminfo">
    detail--{{$route.params.myid}}

    <img :src="filminfo.poster"/>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  layout:"detailtemplate",

  data(){
    return {
      filminfo:null
    }
  },

  asyncData(data) {
    console.log(data.params)

    return axios({
      url:`https://m.maizuo.com/gateway?filmId=${data.params.myid}&k=7153258`,
      headers:{
        'X-Client-Info': '{"a":"3000","ch":"1002","v":"5.0.4","e":"15610855429195524981146"}',
        'X-Host': 'mall.film-ticket.film.info'
      }
    }).then(res=>{
      return {
        filminfo:res.data.data.film
      }
    })
  },
}
</script>
<style lang="scss" scoped>

</style>
