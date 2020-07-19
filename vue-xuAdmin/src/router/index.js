import en from "../i18n/lang/en"
// import Vue from "vue"
import Router from "vue-router"
import Login from "@/views/login/index"
// import Layout from "@/views/layout/layout"
// import HomeMain from "@/views/index/mainIndex"

// 不是必须加载的组件使用懒加载
const Layout = () => import("@/views/layout/layout")
const HomeMain = () => import("@/views/index/mainIndex")
const Forum = () => import("@/views/forum/forum")
const Users = () => import("@/views/users/users")
const Feedback = () => import("@/views/users/feedback")
const ReviewedActTable = () => import("@/views/table/reviewedActTable")
const PassedActTable = () => import("@/views/table/passActTable")
const DenyedActTable = () => import("@/views/table/denyActTable")
const NotFound = () => import("@/views/page404")

/**
 * 重写路由的push方法
 */
const routerPush = Router.prototype.push
Router.prototype.push = function push (location) {
  return routerPush.call(this, location).catch(error => error)
}
Vue.use(Router)
let routeName = en.routeName
let defaultRouter = [
  { path: "/",
    redirect: "/index",
    hidden: true,
    children: []
  },
  {
    path: "/login",
    component: Login,
    name: "",
    hidden: true,
    children: []
  }
]

let addRouter = [
  {
    path: "/index",
    iconCls: "fa fa-dashboard", // 图标样式class
    name: routeName.home,
    component: Layout,
    alone: true,
    children: [
      {
        path: "/index",
        iconCls: "fa fa-dashboard", // 图标样式class
        name: "主页",
        component: HomeMain,
        children: []
      }
    ]
  },
  {
    path: "/404",
    component: NotFound,
    name: "404",
    hidden: true,
    children: []
  },
  {
    path: "/",
    iconCls: "fa fa-newspaper-o", // 图标样式class
    name: routeName.activityManagement,
    component: Layout,
    children: [
      {
        path: "/reviewedtable",
        iconCls: "fa fa-sort-amount-asc", // 图标样式class
        name: routeName.reviewedtable,
        component: ReviewedActTable,
        children: []
      },
      {
        path: "/passedtable",
        iconCls: "fa fa-toggle-on", // 图标样式class
        name: routeName.passedtable,
        component: PassedActTable,
        children: []
      },
      {
        path: "/denyedtable",
        iconCls: "fa fa-expeditedssl", // 图标样式class
        name: routeName.denyedtable,
        component: DenyedActTable,
        children: []
      }
    ]
  },
  {
    path: "/",
    iconCls: "fa fa-server",
    name: routeName.ForumManagement,
    component: Layout,
    children: [
      {
        path: "/forum",
        iconCls: "fa fa-server",
        name: routeName.ForumManagement,
        component: Forum,
        children: []
      }
    ]
  },
  {
    path: "/",
    iconCls: "el-icon-tickets",
    name: routeName.usersManagement,
    component: Layout,
    children: [
      {
        path: "/users",
        iconCls: "el-icon-user",
        name: routeName.usersList,
        component: Users,
        children: []
      },
      {
        path: "/usersfeedback",
        iconCls: "el-icon-tickets",
        name: routeName.usersFeedback,
        component: Feedback,
        children: []
      }
    ]
  },
  { path: "*",
    redirect: "/404",
    hidden: true,
    children: []
  }
]
export default new Router({
  routes: defaultRouter
})
export {defaultRouter, addRouter}
