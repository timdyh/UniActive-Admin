<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 8px;">
            <div>
                <el-button type="primary" @click="showAct()">刷新页面</el-button>
            </div>
        </div>
        <div>
            <el-table :data="actList" style="width: 100%" border>
                <el-table-column type="expand">
                  <template slot-scope="props">
                    <el-form label-position="left" inline class="demo-table-expand">
                      <el-form-item label="发布时间">
                        <span>{{ props.row.fields.apply_time.replace(/T/g,' ').replace(/Z/g,'') }}</span>
                      </el-form-item>
                      <el-form-item label="起始时间">
                        <span>{{ props.row.fields.start_time.replace(/T/g,' ').replace(/Z/g,'') }}</span>
                      </el-form-item>
                      <el-form-item label="结束时间">
                        <span>{{ props.row.fields.end_time.replace(/T/g,' ').replace(/Z/g,'') }}</span>
                      </el-form-item>
                      <el-form-item label="最大容量">
                        <span>{{ props.row.fields.max_num }}</span>
                      </el-form-item>
                      <el-form-item label="活动地点">
                        <span>{{ props.row.fields.place }}</span>
                      </el-form-item>
                    </el-form>
                  </template>
                </el-table-column>
              <el-table-column prop="name" label="活动标题" min-width="auto">
                <template slot-scope="scope"> {{ scope.row.fields.name }} </template>
              </el-table-column>
              <el-table-column prop="holder" label="发布者" min-width="auto">
                <template slot-scope="scope"> {{ scope.row.fields.holder }} </template>
              </el-table-column>
              <el-table-column prop="introduction" label="活动简介" min-width="auto">
                <template slot-scope="scope"> {{ scope.row.fields.introduction }} </template>
              </el-table-column>
              <el-table-column prop="labels" label="活动标签" min-width="auto">
                <template slot-scope="scope">
                <el-tag type="primary" v-show=handleLabel1Show(scope.$index)>
                              {{scope.row.fields.label1}}</el-tag>
                          <el-tag type="success" v-show=handleLabel2Show(scope.$index)>
                              {{scope.row.fields.label2}}</el-tag>
                          <el-tag type="warning" v-show=handleLabel3Show(scope.$index)>
                              {{scope.row.fields.label3}}</el-tag>
                          <el-tag type="info" v-show=handleLabel4Show(scope.$index)>
                              {{scope.row.fields.label4}}</el-tag>
                          <el-tag type="danger" v-show=handleLabel5Show(scope.$index)>
                              {{scope.row.fields.label5}}</el-tag>
                </template>
              </el-table-column>
              <el-table-column label="操作" min-width="auto">
                  <template slot-scope="scope">
                    <el-button
                      size="medium"
                      type="success"
                      @click="handlePass(scope.$index, scope.row)">通过</el-button>
                    <el-button
                      size="medium"
                      type="danger"
                      @click="handleDeny(scope.$index, scope.row)">驳回</el-button>
                  </template>
                </el-table-column>
            </el-table>
        </div>
    </div>
</template>

<script>
export default {
  name: "reviewedActTable",
  data () {
    return {
      input: "",
      actList: []
    }
  },
  mounted () {
    this.showAct()
  },
  methods: {
    showAct () {
      this.$axios.get("http://114.115.134.188/api/show_reviewedActivities/")
        .then((response) => {
          // console.log(response)
          if (response.data.code === 1) {
            // console.log(response.data.list)
            this.actList = response.data.list
          } else {
            // console.log(response.data.message)
          }
        })
    },
    handlePass (index, row) {
      // console.log(index, row)
      let data = new FormData()
      data.append("id", this.actList[index].pk)
      this.$axios.post("http://114.115.134.188/api/pass_activity/", data)
        .then((response) => {
          // console.log(response)
          if (response.data.code === 1) {
            // console.log(response.data.message)
            this.actList.splice(index, 1)
          } else {
            // console.log(response.data.message)
          }
          this.$message({
            showClose: true,
            message: "success",
            type: "success"
          })
        })
        .catch((error) => { // 请求失败处理
          console.log(error)
        })
    },
    handleDeny (index, row) {
      this.$prompt("请输入理由", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        inputValidator: (value) => { // 点击按钮时，对文本框里面的值进行验证
          if (!value || value.trim().length === 0) {
            return "输入不能为空"
          }
        }
      }).then(({ value }) => {
        this.$message({
          type: "success",
          message: "你的理由是: " + value
        })
        // console.log(index, row)
        let data = new FormData()
        data.append("id", this.actList[index].pk)
        data.append("reject", value)
        this.$axios.post("http://114.115.134.188/api/deny_activity/", data)
          .then((response) => {
            // console.log(response)
            if (response.data.code === 1) {
              // console.log(response.data.message)
              this.actList.splice(index, 1)
            } else {
              // console.log(response.data.message)
            }
          })
          .catch((error) => { // 请求失败处理
            console.log(error)
          })
      }).catch(() => {
        this.$message({
          type: "info",
          message: "取消输入"
        })
      })
    },
    handleLabel1Show (index) {
      return this.actList[index].fields.label1 != null & this.actList[index].fields.label1 !== ""
    },
    handleLabel2Show (index) {
      return this.actList[index].fields.label2 != null & this.actList[index].fields.label2 !== ""
    },
    handleLabel3Show (index) {
      return this.actList[index].fields.label3 != null & this.actList[index].fields.label3 !== ""
    },
    handleLabel4Show (index) {
      return this.actList[index].fields.label4 != null & this.actList[index].fields.label4 !== ""
    },
    handleLabel5Show (index) {
      return this.actList[index].fields.label5 != null & this.actList[index].fields.label5 !== ""
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
