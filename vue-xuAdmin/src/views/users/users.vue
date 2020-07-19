<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 8px;">
            <div>
                <el-button type="primary" @click="showUser()">刷新页面</el-button>
            </div>
        </div>
        <div>
            <el-table :data="userList" style="width: 100%" border>
              <el-table-column prop="email" label="账号" min-width="auto">
                <template slot-scope="scope"> {{ scope.row.pk }} </template>
              </el-table-column>
              <el-table-column prop="nickname" label="昵称" min-width="auto">
                <template slot-scope="scope"> {{ scope.row.fields.nickname }} </template>
              </el-table-column>
              <el-table-column prop="gender" label="性别" min-width="auto">
                <template slot-scope="scope"> {{ handleGender(scope.$index) }} </template>
              </el-table-column>
              <el-table-column prop="status" label="状态" min-width="auto">
                <template slot-scope="scope">
                  <el-tag type="success" v-show=statusCommon(scope.$index)>正常</el-tag>
                  <el-tag type="danger" v-show=!statusCommon(scope.$index)>封禁</el-tag>
                </template>
              </el-table-column>
              <el-table-column prop="create_time" label="注册时间" min-width="auto">
                <template slot-scope="scope"> {{ scope.row.fields.create_time.replace(/T/g,' ').replace(/Z/g,'') }} </template>
              </el-table-column>
              <el-table-column prop="last_login" label="上次登录" min-width="auto">
                <template slot-scope="scope"> {{ scope.row.fields.last_login }} </template>
              </el-table-column>
              <el-table-column label="操作" min-width="auto">
                  <template slot-scope="scope">
                    <el-button v-bind:type="!statusCommon(scope.$index) ? 'success' : 'danger'"
                      @click="handleUser(scope.$index)">{{statusCommon(scope.$index) ? '封禁' : '解封'}}</el-button>
                  </template>
              </el-table-column>
<!--              <el-table-column prop="labels" label="兴趣标签" min-width="auto">-->
<!--                <template slot-scope="scope">-->
<!--                <el-tag type="primary" v-show=handleLabel1Show(scope.$index)>-->
<!--                              {{scope.row.fields.label1}}</el-tag>-->
<!--                          <el-tag type="success" v-show=handleLabel2Show(scope.$index)>-->
<!--                              {{scope.row.fields.label2}}</el-tag>-->
<!--                          <el-tag type="info" v-show=handleLabel3Show(scope.$index)>-->
<!--                              {{scope.row.fields.label3}}</el-tag>-->
<!--                          <el-tag type="warning" v-show=handleLabel4Show(scope.$index)>-->
<!--                              {{scope.row.fields.label4}}</el-tag>-->
<!--                          <el-tag type="danger" v-show=handleLabel5Show(scope.$index)>-->
<!--                              {{scope.row.fields.label5}}</el-tag>-->
<!--                </template>-->
<!--              </el-table-column>-->
            </el-table>
        </div>
    </div>
</template>

<script>
export default {
  name: "users",
  data () {
    return {
      input: "",
      userList: []
    }
  },
  mounted () {
    this.showUser()
  },
  methods: {
    showUser () {
      this.$axios.get("http://114.115.134.188/api/show_users/")
        .then((response) => {
          // console.log(response)
          if (response.data.code === 1) {
            // console.log(response.data.list)
            this.userList = response.data.list
          } else {
            // console.log(response.data.message)
          }
        })
    },
    handleGender (index) {
      if (this.userList[index].fields.gender === 1) {
        return "男"
      } else {
        return "女"
      }
    },
    statusCommon (index) {
      return this.userList[index].fields.status === 0
    },
    handleLabel1Show (index) {
      return this.userList[index].fields.label1 != null & this.userList[index].fields.label1 !== ""
    },
    handleLabel2Show (index) {
      return this.userList[index].fields.label2 != null & this.userList[index].fields.label2 !== ""
    },
    handleLabel3Show (index) {
      return this.userList[index].fields.label3 != null & this.userList[index].fields.label3 !== ""
    },
    handleLabel4Show (index) {
      return this.userList[index].fields.label4 != null & this.userList[index].fields.label4 !== ""
    },
    handleLabel5Show (index) {
      return this.userList[index].fields.label5 != null & this.userList[index].fields.label5 !== ""
    },
    handleUser (index) {
      // console.log(index)
      this.$message({
        showClose: true,
        message: "",
        type: "success"
      })
      let data = new FormData()
      data.append("email", this.userList[index].pk)
      this.$axios.post("http://114.115.134.188/api/change_user_status/", data)
        .then((response) => {
          // console.log(response)
          if (response.data.code === 1) {
            // console.log(response.data.message)
            this.userList[index].fields.status = 1 - this.userList[index].fields.status
          } else {
            // console.log(response.data.message)
          }
        })
        .catch((error) => { // 请求失败处理
          // console.log(error)
        })
    }
  }
}
</script>

<style>
  .demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
</style>
