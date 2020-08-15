<template>
  <div>
    <tabbar v-show="isTabbarShow"></tabbar>
    <!-- 路由容器 -->
    <section>
      <router-view></router-view>
    </section>
  </div>
</template>

<script>
// 全局组件
// import Vue from 'vue'
// Vue.component("navbar",navbar)
// Vue.component("sidebar",sidebar)
// ES6 导出
import tabbar from '@/components/Tabbar'
import { mapState } from 'vuex' // ES6导出
// import bus from '@/bus'
export default {
  data () {
    return {
      // isShow:true
    }
  },
  methods: {

  },
  components: {
    tabbar
  },

  // computed:{
  //   isShow(){
  //     return this.$store.state.isTabbarShow
  //   }
  // }，
  computed: {
    ...mapState(['isTabbarShow']) // ES6展开合并运算符

  }

  // beforeMount() {
  //   console.log("从这里开始订阅消息了")
  //   bus.$on("maizuo",(data)=>{
  //     // console.log("被通知了maizuo",data)
  //     this.isShow = data;
  //   })
  // }
}
</script>

<style lang="scss">
*{
  margin:0;
  padding:0;
}

html{
  height: 100%;

}
li{
  list-style: none;
}

section{
  margin-bottom: 50px;
}
</style>
