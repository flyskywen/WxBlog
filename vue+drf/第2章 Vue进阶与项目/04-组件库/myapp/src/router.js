import Vue from 'vue'
import Router from 'vue-router'
import Film from '@/views/Film'
import Nowplaying from '@/views/Film/Nowplaying'
import Comingsoon from '@/views/Film/Comingsoon'
import Cinema from '@/views/Cinema'
import Center from '@/views/Center'
import Login from '@/views/Login'
import City from '@/views/City'
import Detail from '@/views/Detail'

Vue.use(Router)

// const auth = {
//   isLogin () {
//     return true
//   }
// }

const router = new Router({
  mode: 'hash',
  // base: process.env.BASE_URL,
  routes: [
    {
      path: '/film',
      component: Film,
      children: [
        {
          path: '/film/nowplaying', // /film/nowplaying
          component: Nowplaying
        },
        {
          path: 'comingsoon',
          component: Comingsoon
        },
        {
          path: '',
          redirect: '/film/nowplaying'
        }
      ]
    },
    {
      path: '/cinema',
      component: Cinema
    },
    {
      path: '/detail/:id', // /detail/aa 动态路由
      name: 'kerwindetail',
      component: Detail,
      props: true
    },
    {
      path: '/center',
      alias: '/my',
      component: Center
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/city',
      component: City
    },
    {
      path: '*',
      redirect: '/film'
    }
  ]
})
// 全局守卫
// router.beforeEach((to, from, next) => {
//   // ...
//   // console.log(to);
//   if(to.path==='/center'){
//     console.log("盘查")

//     if(auth.isLogin()){
//       next();
//     }else{
//       next("/login");
//     }
//   }else{
//     next();
//   }
// })

export default router
