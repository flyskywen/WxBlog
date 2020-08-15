import Vue from 'vue' // ES6 模块导入方式  commonJS var Vue = require("vue")
import App from './App.vue' // var app = require("./App.vue")
import router from './router'
import store from './store'
import AllA from './module/moduleA' // 导入所有的接口
import { A1 as MyA1 } from './module/moduleB' // 只导入某个几个接口

// 引入element UI
// import ElementUI from 'element-ui';
// import 'element-ui/lib/theme-chalk/index.css';
// Vue.use(ElementUI);

// 引入mint-ui
import MintUI from 'mint-ui'
import 'mint-ui/lib/style.css'
Vue.use(MintUI)

Vue.config.productionTip = false

console.log(AllA, MyA1)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#box')
