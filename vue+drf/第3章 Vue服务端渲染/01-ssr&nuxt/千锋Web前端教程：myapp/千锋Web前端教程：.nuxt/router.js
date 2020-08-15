import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'

const _40942213 = () => interopDefault(import('..\\pages\\center.vue' /* webpackChunkName: "pages_center" */))
const _f640caa2 = () => interopDefault(import('..\\pages\\cinema.vue' /* webpackChunkName: "pages_cinema" */))
const _01d04d42 = () => interopDefault(import('..\\pages\\film.vue' /* webpackChunkName: "pages_film" */))
const _45dd9984 = () => interopDefault(import('..\\pages\\film\\comingsoon.vue' /* webpackChunkName: "pages_film_comingsoon" */))
const _8332334c = () => interopDefault(import('..\\pages\\film\\nowplaying.vue' /* webpackChunkName: "pages_film_nowplaying" */))
const _a1986932 = () => interopDefault(import('..\\pages\\detail\\_myid.vue' /* webpackChunkName: "pages_detail__myid" */))

Vue.use(Router)

if (process.client) {
  if ('scrollRestoration' in window.history) {
    window.history.scrollRestoration = 'manual'

    // reset scrollRestoration to auto when leaving page, allowing page reload
    // and back-navigation from other pages to use the browser to restore the
    // scrolling position.
    window.addEventListener('beforeunload', () => {
      window.history.scrollRestoration = 'auto'
    })

    // Setting scrollRestoration to manual again when returning to this page.
    window.addEventListener('load', () => {
      window.history.scrollRestoration = 'manual'
    })
  }
}
const scrollBehavior = function (to, from, savedPosition) {
  // if the returned position is falsy or an empty object,
  // will retain current scroll position.
  let position = false

  // if no children detected and scrollToTop is not explicitly disabled
  if (
    to.matched.length < 2 &&
    to.matched.every(r => r.components.default.options.scrollToTop !== false)
  ) {
    // scroll to the top of the page
    position = { x: 0, y: 0 }
  } else if (to.matched.some(r => r.components.default.options.scrollToTop)) {
    // if one of the children has scrollToTop option set to true
    position = { x: 0, y: 0 }
  }

  // savedPosition is only available for popstate navigations (back button)
  if (savedPosition) {
    position = savedPosition
  }

  return new Promise((resolve) => {
    // wait for the out transition to complete (if necessary)
    window.$nuxt.$once('triggerScroll', () => {
      // coords will be used if no selector is provided,
      // or if the selector didn't match any element.
      if (to.hash) {
        let hash = to.hash
        // CSS.escape() is not supported with IE and Edge.
        if (typeof window.CSS !== 'undefined' && typeof window.CSS.escape !== 'undefined') {
          hash = '#' + window.CSS.escape(hash.substr(1))
        }
        try {
          if (document.querySelector(hash)) {
            // scroll to anchor by returning the selector
            position = { selector: hash }
          }
        } catch (e) {
          console.warn('Failed to save scroll position. Please add CSS.escape() polyfill (https://github.com/mathiasbynens/CSS.escape).')
        }
      }
      resolve(position)
    })
  })
}

export function createRouter() {
  return new Router({
    mode: 'history',
    base: decodeURI('/'),
    linkActiveClass: 'nuxt-link-active',
    linkExactActiveClass: 'nuxt-link-exact-active',
    scrollBehavior,

    routes: [{
      path: "/center",
      component: _40942213,
      name: "center"
    }, {
      path: "/cinema",
      component: _f640caa2,
      name: "cinema"
    }, {
      path: "/film",
      component: _01d04d42,
      name: "film",
      children: [{
        path: "comingsoon",
        component: _45dd9984,
        name: "film-comingsoon"
      }, {
        path: "nowplaying",
        component: _8332334c,
        name: "film-nowplaying"
      }]
    }, {
      path: "/detail/:myid?",
      component: _a1986932,
      name: "detail-myid"
    }, {
      path: "/",
      redirect: "/film/nowplaying"
    }],

    fallback: false
  })
}
