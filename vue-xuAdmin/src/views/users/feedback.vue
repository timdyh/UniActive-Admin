<template>
    <div style="padding: 10px">
        <div style="background: #fff; border-radius: 8px; padding: 8px;">
            <div>
                <el-button type="primary" @click="showFeedback()">刷新页面</el-button>
            </div>
        </div>
        <div>
              <el-table :data="feedbackList" style="width: 100%" border>
                  <el-table-column type="index" min-width="10%">
              </el-table-column>
              <el-table-column prop="email" label="账号" min-width="20%">
                <template slot-scope="scope"> {{ scope.row.fields.provider }} </template>
              </el-table-column>
              <el-table-column prop="opinion" label="反馈时间" min-width="20%">
                <template slot-scope="scope"> {{ scope.row.fields.time.replace(/T/g,' ').replace(/Z/g,'') }} </template>
              </el-table-column>
              <el-table-column prop="opinion" label="反馈意见" min-width="50%">
                <template slot-scope="scope"> {{ scope.row.fields.opinion }} </template>
              </el-table-column>
            </el-table>
        </div>
    </div>
</template>

<script>
export default {
  name: "feedback",
  data () {
    return {
      input: "",
      feedbackList: []
    }
  },
  mounted () {
    this.showFeedback()
  },
  methods: {
    showFeedback () {
      this.$axios.get("http://114.115.134.188/api/get_feedback/")
        .then((response) => {
          // console.log(response)
          if (response.data.code === 1) {
            // console.log(response.data.list)
            this.feedbackList = response.data.list
          } else {
            // console.log(response.data.message)
          }
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
