<template>
  <div>
      <swiper :key="looplist.length" ref="myswiper">
        <div class="swiper-slide" v-for="data in looplist" :key="data.bannerId">
          <img :src="data.imgUrl"/>
        </div>
      </swiper>
    <filmheader :class="isFixed?'fixed':''"></filmheader>
    <router-view></router-view>
  </div>
</template>

<script>
import swiper from '@/views/Film/Swiper'
import filmheader from '@/views/Film/FilmHeader'
import { Indicator } from 'mint-ui'

import axios from 'axios'
export default {
  data () {
    return {
      looplist: [],
      isFixed: false
    }
  },

  components: {
    swiper,
    filmheader
  },
  mounted () {
    Indicator.open({
      text: '加载中...',
      spinnerType: 'fading-circle'
    })

    axios({
      url: 'https://m.maizuo.com/gateway?type=2&cityId=110100&k=5553387',
      headers: {
        'X-Client-Info': '{"a":"3000","ch":"1002","v":"5.0.4","e":"15610855429195524981146"}',
        'X-Host': 'mall.cfg.common-banner'

      }
    }).then(res => {
      console.log(res.data)
      this.looplist = res.data.data

      Indicator.close()
    })

    window.onscroll = this.handleScroll
  },

  beforeDestroy () {
    // console.log("beforeDestroy")
    window.onscroll = null
  },

  methods: {
    handleScroll () {
      // console.log(document.documentElement.scrollTop,this.$refs.myswiper.$el.offsetHeight)
      if (document.documentElement.scrollTop >= this.$refs.myswiper.$el.offsetHeight) {
        // console.log("fixed")
        this.isFixed = true
      } else {
        // console.log("unfixed")
        this.isFixed = false
      }
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
