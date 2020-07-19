<template>
  <div>
    <h3>点击上传</h3>
    <div>
        <form action="">
            <input type="file" id="img">
            <el-button type="submit" @click.prevent="on_sumit">上传</el-button>
        </form>
        <el-button type="submit" @click="on_download">下载</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: "upload",
  data () {
    return {
    }
  },
  methods: {
    on_sumit () {
      let formData = new FormData()
      var img = document.getElementById("img").files[0]
      formData.append("image", img, img.name)
      console.log(formData)
      this.$axios({
        url: "http://114.115.134.188/api/upload_file/",
        method: "post",
        data: formData,
        headers: {
          "Content-Type": "multipart/form-data"
        }
      }).then(res => {
        console.log(res)
      })
    },
    on_download () {
      let filename = "video1.mp4"
      this.$axios.get("http://114.115.134.188/api/minidouyin_get_file/?student_id=16060606&user_name=tyu&file=1589707764v.mp4", {responseType: "blob"})
        .then((response) => {
          if (!response) {
            this.$message.error("下载失败")
            return false
          }
          console.log(response)
          // let contentDisposition = response["Content-Disposition"]
          // console.log(22222222222222222222222)
          // console.log(contentDisposition)
          // let patt = new RegExp("filename=([^;]+\\.[^\\.;]+);*")
          // let result = patt.exec(contentDisposition)
          // let filename = decodeURI(result[1])
          // console.log(filename)
          let url = window.URL.createObjectURL(response.data)
          let link = document.createElement("a")
          link.style.display = "none"
          link.href = url
          link.download = filename // 下载后文件名
          document.body.appendChild(link)
          link.click()
          document.body.removeChild(link) // 下载完成移除元素
          window.URL.revokeObjectURL(url)
        })
    }
  }

}
</script>

<style lang="scss">
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
  h3{
    margin: 55px 0 20px;
    font-weight: 400;
    color: #1f2f3d;
    font-size: 22px;
  }
  p{
    font-size: 14px;
    color: #5e6d82;
    line-height: 1.5em;
  }
</style>
