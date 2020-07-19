import enLocale from "element-ui/lib/locale/lang/en"
const en = {
  routeName: {
    home: "home",
    activityManagement: "activityManagement",
    reviewedtable: "reviewedtable",
    passedtable: "passedtable",
    denyedtable: "denyedtable",
    upload: "upload",
    ForumManagement: "ForumManagement",
    usersManagement: "usersManagement",
    usersList: "usersList",
    usersFeedback: "usersFeedback",
    systemSettings: "systemSettings"
  },
  userDropdownMenu: {
    changePassword: "changePassword",
    logout: "logout"
  },

  ...enLocale //  合并element-ui内置翻译
}

export default en
