<template>
  <div id="login">
    <div class="loginConbox">
      <div class="header">
      </div>
      <div class="loginBox">
        <div class="loginCon">
          <p class="title">UniActive后台管理系统</p>
          <el-card shadow="always" class="login-module" v-if="smdl">
            <div slot="header" class="clearfix formTitlt">
              <span>登录</span>
              <span class="titIconbox">
            </span>
            </div>
            <el-form :model="loginForm" status-icon label-width="100px" class="demo-ruleForm">
              <el-form-item>
                <el-input type="text" v-model="loginForm.username" auto-complete="off" placeholder="请输入登录账号"></el-input>
              </el-form-item>
              <el-form-item>
                <el-input type="password" v-model="loginForm.password" auto-complete="off"
                          placeholder="请输入登录密码"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button class="subBtn" type="primary" @click="submit">登录</el-button>
              </el-form-item>
            </el-form>
          </el-card>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      smdl: true,
      loginForm: {
        username: "",
        password: ""
      }
    }
  },
  methods: {
    submit () {
      let that = this
      if (this.loginForm.username === "" || this.loginForm.password === "") {
        this.$message({
          showClose: true,
          message: "账号或密码不能为空",
          type: "error"
        })
        return false
      } else {
        let data = new FormData()
        data.append("username", this.loginForm.username)
        data.append("password", this.loginForm.password)
        this.$axios.post("http://114.115.134.188/api/login/", data) // 需要改/api/login/
          .then((response) => {
            // console.log(response)
            if (response.data.code === 1) {
              // 将 username 设置为 token 存储在 store，仅为测试效果，实际存储 token 以后台返回为准
              that.$store.dispatch("setToken", that.loginForm.username)
                .then(() => {
                  that.$router.push({path: "/"})
                }).catch(res => {
                  that.$message({
                    showClose: true,
                    message: res,
                    type: "error"
                  })
                })
            } else {
              that.$message({
                showClose: true,
                message: response.data.message,
                type: "error"
              })
            }
          })
          .catch((error) => { // 请求失败处理
            console.log(error)
          })
      }
    }
  }
}
</script>
<style lang="scss">
  #login {
    width: 100%;
    height: 100%;
    background-color: #2d3a4b;
    .loginConbox{
      background: #2d3a4b;
    }
    .header {
      height: 60px;
      position: relative;
      background: #2d3a4b;
      /*border-bottom: 1px solid rgba(255, 255, 255, 0.3);*/
      .logo{
        margin-left: 30px;
        width: 500px;
        float: left;
        height: 40px;
        padding-top: 10px;
        img{
          height: 100%;
        }
      }
    }

    .loginBox {
      .iconcolor {
        color: #409EFF;
      }

      padding: 74px 0 118px;

      .loginCon {
        width: 990px;
        margin: auto;
        position: relative;
        height: 388px;

        .el-card__header {
          border-bottom: 0px;
        }
        .title{
          font-size: 136px;
          font-weight: 600;
          color: #ffffff;
          width: 500px;
          float: left;
          margin-top: 20px;
          &:first-child{
            font-size: 40px;
            margin-top: 130px;
            margin-bottom: 20px;
          }
        }
        .login-module {
          width: 380px;
          height: 280px;
          margin-top: 60px;
          border: none;
          position: absolute;
          right: 0;

          .formTitlt {
            font-size: 18px;
            font-weight: 400;

            .titIconbox {
              float: right;

              .pointer {
                cursor: pointer;
              }
            }
          }
        }

        .el-form-item__content {
          margin-left: 0px !important;

          .subBtn {
            width: 100%;
          }
        }
      }

      .el-input__inner, .el-button, .el-card, .el-message {
        border-radius: 0px !important;
      }

      .el-form-item__content .ico {
        position: absolute;
        top: 0px;
        left: 0px;
        z-index: 999;
        width: 40px;
        height: 39px;
        text-align: center;
        border-right: 1px solid #ccc;
      }

      .ewmbox {
        width: 100%;
        height: 240px;
        margin-top: -25px;

        .ewm {
          width: 140px;
          height: 140px;
          margin: 20px auto;

          p {
            font-size: 12px;
            padding-left: 40px;
            margin: 0;
          }
        }

        .ewmicon {
          width: 140px;
          margin: 20px auto 0;

          .iconfont {
            float: left;
          }

          p {
            font-size: 12px;
            padding-left: 40px;
            margin: 0;
          }
        }
      }
    }
  }
</style>
