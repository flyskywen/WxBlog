<template>
  <div>
    <v-touch v-on:swipeleft="onSwipeLeft" v-on:swiperight="onSwipeRight">
      <div style="background:red;height:100px">center</div>
    </v-touch>
    <mt-button type="default">default</mt-button>
    <mt-button type="primary">primary</mt-button>
    <mt-button type="danger">danger</mt-button>

    <mt-swipe :auto="14000" id="mint-swipe" :showIndicators="false">
      <mt-swipe-item>1</mt-swipe-item>
      <mt-swipe-item>2</mt-swipe-item>
      <mt-swipe-item>3</mt-swipe-item>
    </mt-swipe>

    <mt-index-list>
      <mt-index-section index="A">
        <mt-cell title="Aaron"></mt-cell>
        <mt-cell title="Alden"></mt-cell>
        <mt-cell title="Austin"></mt-cell>
      </mt-index-section>
      <mt-index-section index="B">
        <mt-cell title="Baldwin"></mt-cell>
        <mt-cell title="Braden"></mt-cell>
      </mt-index-section>
      ...
      <mt-index-section index="Z">
        <mt-cell title="Zack"></mt-cell>
        <mt-cell title="Zane"></mt-cell>
      </mt-index-section>
    </mt-index-list>

  </div>
</template>
<script>
import Vue from 'vue'
var VueTouch = require('vue-touch')
Vue.use(VueTouch, {name: 'v-touch'})

export default {

  methods: {
    onSwipeLeft(){
      console.log("left");
    },
    onSwipeRight(){
      console.log("right")
    }
  },

  beforeRouteEnter (to, from, next) {
    console.log('局部盘查')
    // if (false) {
    //   next()
    // } else {
    //   next('/login')
    // }
    // 在渲染该组件的对应路由被 confirm 前调用
    // 不！能！获取组件实例 `this`
    // 因为当守卫执行前，组件实例还没被创建
    next()
  }
}
</script>
<style lang="scss">
#mint-swipe{
  height: 200px;
  .mint-swipe-indicator.is-active{
    background:red;
  }
}

</style>
