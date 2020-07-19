<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="8">
        <div class="card kjfs">
          <p class="title"><i class="fa fa-th-large fa-lg"></i>快捷方式</p>
          <ul>
            <li><router-link to="/reviewedtable" class="kjfs kjfs-bluee"><span><i class="fa fa-sort-amount-asc"></i></span><span>待审核活动</span></router-link></li>
            <li><router-link to="/passedtable" class="kjfs kjfs-pinkk"><span><i class="fa fa-toggle-on"></i></span><span>已通过活动</span></router-link></li>
            <li><router-link to="/denyedtable" class="kjfs kjfs-yelloww"><span><i class="fa fa-expeditedssl"></i></span><span>已驳回活动</span></router-link></li>
          </ul>
          <ul>
            <li><router-link to="/forum" class="kjfs kjfs-grennn"><span><i class="fa fa-server"></i></span><span>活动论坛</span></router-link></li>
            <li><router-link to="/users" class="kjfs kjfs-purplee"><span><i class="el-icon-user"></i></span><span>用户列表</span></router-link></li>
            <li><router-link to="/usersfeedback" class="kjfs kjfs-lightBluee"><span><i class="el-icon-tickets"></i></span><span>用户反馈</span></router-link></li>
          </ul>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="card dbsx">
          <p class="title"><i class="fa fa-file-text-o"></i>系统数据</p>
          <ul>
            <li><router-link to="#"><span>待审核活动</span><span class="num">{{this.revNum}}</span></router-link></li>
            <li><router-link to="#"><span>已通过活动</span><span class="num">{{this.passNum}}</span></router-link></li>
          </ul>
          <ul>
            <li><router-link to="#"><span>已驳回活动</span><span class="num">{{this.denyNum}}</span></router-link></li>
            <li><router-link to="#"><span>系统用户数</span><span class="num">{{this.userNum}}</span></router-link></li>
          </ul>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="card bbxx">
          <p class="title"><i class="fa fa-server"></i>版本信息</p>
          <div class="table">
            <p><span class="tit">当前版本</span>v1.0.0</p>
            <p><span class="tit">基于框架</span>vue2.0 + element-ui</p>
            <p><span class="tit">作者</span>UniActive管理团队</p>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "mainIndex",
  components: {},
  data () {
    return {
      passNum: 0,
      denyNum: 0,
      revNum: 0,
      userNum: 0
    }
  },
  mounted () {
    this.get_Deny()
    this.get_Pass()
    this.get_Rev()
    this.get_Use()
  },
  methods: {
    get_Deny () {
      this.$axios.get("http://114.115.134.188/api/show_denyedActivities/")
        .then((response) => {
          // console.log(response)
          if (response.data.code === 1) {
            // console.log(response.data.list)
            this.denyNum = response.data.list.length
          } else {
            // console.log(response.data.message)
          }
        })
    },
    get_Pass () {
      this.$axios.get("http://114.115.134.188/api/show_passedActivities/")
        .then((response) => {
          // console.log(response)
          if (response.data.code === 1) {
            // console.log(response.data.list)
            this.passNum = response.data.list.length
          } else {
            // console.log(response.data.message)
          }
        })
    },
    get_Rev () {
      this.$axios.get("http://114.115.134.188/api/show_reviewedActivities/")
        .then((response) => {
          // console.log(response)
          if (response.data.code === 1) {
            // console.log(response.data.list)
            this.revNum = response.data.list.length
          } else {
            // console.log(response.data.message)
          }
        })
    },
    get_Use () {
      this.$axios.get("http://114.115.134.188/api/show_users/")
        .then((response) => {
          // console.log(response)
          if (response.data.code === 1) {
            // console.log(response.data.list)
            this.userNum = response.data.list.length
          } else {
            // console.log(response.data.message)
          }
        })
    }
  }
}
</script>

<style lang="scss">
  $top:top;
  $bottom:bottom;
  $left:left;
  $right:right;
  $leftright: ($left, $right);
  $pinkk: #eec2d3;
  $bluee: #409eff;
  $yelloww: #f4d884;
  $grennn: #89dda0;
  $purplee: #78a2ea;
  $lightBluee: #b8d6ff;

  $list: bluee pinkk yelloww grennn purplee lightBluee;
  $list1: $bluee $pinkk $yelloww $grennn $purplee $lightBluee;
  %shadow{
    background: #fff;
    -webkit-box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.2);
    box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.2);
    border-color: rgba(0, 0, 0, 0.2);
    .title{
      font-size: 14px;
      padding: 10px;
      i{
        margin-#{$right}: 5px;
      }
    }
  }

  @mixin flex($direction:row,$content:space-between){
    display: flex;
    flex-direction: $direction;
    justify-content: $content;
  }
  .card{
    color: #666;
    @extend %shadow;

    ul{
      @include flex;
      li{
        flex: 1;
        a{
          color: #666666;
          align-items:center;
          padding-#{$top}: 20px;
          padding-#{$bottom}: 20px;
          @include flex(column);
          span{
            height: 44px;
          }
          .num{
            line-height: 44px;
            font-size: 42px;
            color: $bluee;
            margin: 0px;
          }
        }
        .kjfs-bluee{
          color: $bluee;
        }
        .kjfs-pinkk{
          color: $pinkk;
        }
        .kjfs-yelloww{
          color: $yelloww;
        }
        .kjfs-grennn{
          color: $grennn;
        }
        .kjfs-purplee{
          color: $purplee;
        }
        .kjfs-lightBluee{
          color: $lightBluee;
        }
        &:hover{
          .kjfs-bluee{
            color: #ffffff;
            background: $bluee;
          }
          .kjfs-pinkk{
            color: #ffffff;
            background: $pinkk;
          }
          .kjfs-yelloww{
            color: #ffffff;
            background: $yelloww;
          }
          .kjfs-grennn{
            color: #ffffff;
            background: $grennn;
          }
          .kjfs-purplee{
            color: #ffffff;
            background: $purplee;
          }
          .kjfs-lightBluee{
            color: #ffffff;
            background: $lightBluee;
          }
        }
      }
    }
    .table{
      padding: 21px;
      p{
        height: 52px;
        line-height: 52px;
        border: 1px solid #cccccc;
        overflow: hidden;
        border-#{$top}: none;
        @include flex( null,start);
        &:first-child{
          border-#{$top}: 1px solid #cccccc;
        }
        span{
        }
        .tit{
          width: 90px;
          min-width: 90px;
          height: 100%;
          text-align: center;
          border-#{$right}: 1px solid #cccccc;
          margin-#{$right}: 18px;
        }
        span.gitbox{
          flex: 1;
          height: 100%;
          overflow: hidden;
          @include flex(row,start);
          a{
            &:first-child{
              margin-#{$right}: 30px;
            }
          }
        }
      }
    }
  }
</style>
