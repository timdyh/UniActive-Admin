import zhLocale from "element-ui/lib/locale/lang/zh-CN"
const cn = {
  routeName: {
    home: "主页",
    activityManagement: "活动管理",
    reviewedtable: "待审核的活动",
    passedtable: "已通过的活动",
    denyedtable: "已驳回的活动",
    upload: "上传",
    ForumManagement: "论坛管理",
    usersManagement: "用户管理",
    usersList: "用户列表",
    usersFeedback: "用户反馈",
    systemSettings: "系统设置"
  },
  userDropdownMenu: {
    changePassword: "修改密码",
    logout: "退出登录"
  },

  ...zhLocale //  合并element-ui内置翻译
}

export default cn
