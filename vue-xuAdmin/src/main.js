// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// import Vue from "vue"
// import axios from "axios"
// import ElementUI from "element-ui"
import App from "./App.vue"
import router from "./router"
import store from "./vuex"
import i18n from "./i18n/i18n"

// import "element-ui/lib/theme-chalk/index.css"
// import "font-awesome/css/font-awesome.css"
import "@/router/permission"

Vue.config.productionTip = false
// Vue.use(ElementUI)

// 设置基础URL
axios.defaults.baseURL = ""
// 设置请求超时时间
axios.defaults.timeout = 5000

Vue.prototype.$axios = axios

/* eslint-disable no-new */
new Vue({
  el: "#app",
  router,
  store,
  i18n,
  render: h => h(App),
  components: {App},
  template: "<App/>"
})
