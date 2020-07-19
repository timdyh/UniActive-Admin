<template>
  <div class="page404">
    <div class="i404">
      <div>404</div>
      <p>您的访问页面可能被删除或者不存在</p>
      <a href="/">返回首页</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "page404",
  mounted () {
  }
}
</script>

<style lang="scss">
  .page404{
    width: 100%;
    height: 100%;
    overflow: hidden;
    & >div{
      width: 100%;
      height: 100%;
     }
    .i404{
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      p{
        font-size: 20px;
        color: #3d95ff;
        margin-top: 2px;
        text-align: center;
      }
      div {
        font-size: 200px;
        color: #3d95ff;
        margin-top: 2px;
        text-align: center;
      }
      a{
        display: block;
        width: 150px;
        height: 50px;
        color: #ffffff;
        background: #56a9ff;
        margin-top: 35px;
        line-height: 50px;
        text-align: center;
        border-radius: 50px;
        font-size: 18px;
      }
    }
  }

</style>
