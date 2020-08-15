<template>
  <div>
    <ul>
      <li v-for="data in comingList" :key="data.filmId" @click="handleClick(data.isPresale,data.filmId)">
        <img :src="data.poster"/>
        <h3>{{data.name}}</h3>
        <p>观众评分{{data.grade}}</p>
        <p v-if="data.actors">主演:{{data.actors | actorfilter}}</p>
        <p v-else>暂无主演</p>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { MessageBox } from 'mint-ui';

export default {
  mounted () {

    if (this.comingList.length === 0) {
      // ajax请求
      this.$store.dispatch('getComingListAction')
    } else {
      console.log('使用缓存数据')
    }
  },
  computed: {
    ...mapState(['comingList'])
  },
  methods:{
    handleClick(data,id){
      if(!data){
        MessageBox({
          title: '提示',
          message: '没有排期，看看其他电影吧',
          showCancelButton: true
        }).then(res=>{
          // console.log(res);
          if(res==="confirm"){
            console.log("回到首页")
            this.$router.push(`/film/nowplaying`)
          }
        })
      }
      this.$router.push({ name: 'kerwindetail', params: { id: id } })
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
