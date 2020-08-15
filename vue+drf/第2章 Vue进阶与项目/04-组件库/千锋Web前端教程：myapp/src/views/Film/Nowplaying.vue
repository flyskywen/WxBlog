<template>
  <div>
    nowplaying
    <ul v-infinite-scroll="loadMore"
    infinite-scroll-distance="0"
    infinite-scroll-disabled="loading"
    infinite-scroll-immediate-check="false"
    >
      <li v-for="data in datalist" :key="data.filmId" @click="handleChangePage(data.filmId)">
        <img :src="data.poster"/>
        <h3>{{data.name}}</h3>
        <p>观众评分{{data.grade}}</p>
        <p v-if="data.actors">主演:{{data.actors | actorfilter}}</p>
        <p v-else>暂无主演</p>
      </li>
    </ul>
    <div v-show="isShow">正在加载中.....</div>
  </div>
</template>
<script>
import axios from 'axios'
import Vue from 'vue'
Vue.filter('actorfilter', function (data) {
  // console.log(data);
  var newlist = data.map(item => item.name)
  return newlist.join(' ')
})

export default {
  data () {
    return {
      datalist: [],
      loading: false,
      current: 1,
      total: 0,
      isShow: true
    }
  },

  mounted () {
    // axios.get("https://m.maizuo.com/gateway?cityId=110100&pageNum=1&pageSize=10&type=1&k=4271989").then(res=>{
    //   console.log(res.data);
    // })
    // $.ajax $.get
    axios({
      url: 'https://m.maizuo.com/gateway?cityId=110100&pageNum=1&pageSize=10&type=1&k=4271989',
      headers: {
        'X-Client-Info': '{"a":"3000","ch":"1002","v":"5.0.4","e":"15610855429195524981146"}',
        'X-Host': 'mall.film-ticket.film.list'
      }
    }).then(res => {
      console.log(res.data)
      this.datalist = res.data.data.films
      this.total = res.data.data.total
    })
  },
  methods: {
    handleChangePage (id) {
      console.log(id)
      // 编程式导航-路径跳转
      // this.$router.push(`/detail/${id}`)

      // 编程式导航-名字跳转
      this.$router.push({ name: 'kerwindetail', params: { id: id } })
    },
    loadMore () {
      console.log('到底了')
      this.loading = true // 禁用

      this.current++

      if (this.datalist.length === this.total) {
        this.isShow = false
        return
      }
      axios({
        url: `https://m.maizuo.com/gateway?cityId=110100&pageNum=${this.current}&pageSize=10&type=1&k=4271989`,
        headers: {
          'X-Client-Info': '{"a":"3000","ch":"1002","v":"5.0.4","e":"15610855429195524981146"}',
          'X-Host': 'mall.film-ticket.film.list'
        }
      }).then(res => {
        // console.log(res.data)
        this.datalist = [...this.datalist, ...res.data.data.films]
        this.loading = false
      })
    }
  }
}
</script>

<style lang="scss" scoped>
  ul{
    li{
        padding:10px;
        overflow: hidden;
      img{
        float:left;
        width:100px;
      }
    }
  }
</style>
