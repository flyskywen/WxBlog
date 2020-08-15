<template>
  <div v-if="filminfo">
    <img :src="filminfo.poster" class="poster"/>
    <h2>{{filminfo.name}}</h2>

    <h3>演职人员</h3>
    <swiper perview="4" class="actorswiper" myclassname="actorswiper">
      <div class="swiper-slide" v-for="data in filminfo.actors" :key="data.name">
        <img :src="data.avatarAddress"/>
        <p>{{data.name}}</p>
      </div>
    </swiper>
    <h3>剧照</h3>
    <swiper perview="3" class="photoswiper" myclassname="photoswiper">
      <div class="swiper-slide" v-for="(data,index) in filminfo.photos" :key="index">
        <img :src="data"/>
      </div>
    </swiper>
  </div>
</template>
<script>
import axios from 'axios'
import swiper from './Detail/DetailSwiper'
import { HIDE_TABBAR_MUTATION, SHOW_TABBAR_MUTATION } from '@/type'
// import bus from '@/bus'
export default {
  data () {
    return {
      filminfo: null
    }
  },
  props: ['id'],

  beforeMount () {
    // console.log("hidetabbar","发麻药了")
    // bus.$emit("maizuo",false)
    // this.$store.state.isTabbarShow = false

    this.$store.commit(HIDE_TABBAR_MUTATION, false)// 第一个参数就是mutation名字
  },

  mounted () {
    // console.log('要id获取详情信息', this.$route.params.id, this.id)
    axios({
      url: `https://m.maizuo.com/gateway?filmId=${this.id}&k=4359832`,
      headers: {
        'X-Client-Info': '{"a":"3000","ch":"1002","v":"5.0.4","e":"15610855429195524981146"}',
        'X-Host': 'mall.film-ticket.film.info'
      }
    }).then(res => {
      console.log(res.data)
      this.filminfo = res.data.data.film
    })
  },

  beforeDestroy () {
    console.log('showtabbar')
    // bus.$emit("maizuo",true)
    // this.$store.state.isTabbarShow = true
    this.$store.commit(SHOW_TABBAR_MUTATION, true)// 第一个参数就是mutation名字
  },

  components: {
    swiper
  }
}
</script>

<style lang="scss" scoped>
.poster{
  width:100%;
}
</style>
