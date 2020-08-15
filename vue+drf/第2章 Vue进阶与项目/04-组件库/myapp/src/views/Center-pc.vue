<template>
  <div>
    center
     <el-button type="danger" :loading="true">默认按钮</el-button>

      <el-radio v-model="radio" label="1">vue</el-radio>
      <el-radio v-model="radio" label="2">react</el-radio>

      <el-switch
        v-model="value"
        active-color="#13ce66"
        inactive-color="#ff4949">
      </el-switch>

       <el-alert
        title="成功提示的文案"
        type="success">
      </el-alert>

      <el-button type="text" @click="open">点击打开 Message Box</el-button>

      <el-popover
        placement="bottom"
        title="标题"
        width="200"
        trigger="click"
        content="这是一段内容,这是一段内容,这是一段内容,这是一段内容。">
        <el-button slot="reference">click 激活</el-button>
      </el-popover>

      <el-carousel :interval="4000" type="card" height="200px">
        <el-carousel-item v-for="item in 6" :key="item">
          <h3 class="medium">{{ item }}</h3>
        </el-carousel-item>
      </el-carousel>

      <el-backtop target=".page-component__scroll .el-scrollbar__wrap"></el-backtop>
  </div>
</template>
<script>
export default {

  data () {
    return {
      radio: '2',
      value: false
    }
  },

  methods: {
    open () {
      // this.$alert('这是一段内容111', '标题名称111', {
      //     confirmButtonText: '确定11',
      //     callback: action => {
      //       this.$message({
      //         type: 'info',
      //         message: `action: ${ action }`
      //       });
      //       // console.log(act)
      //     }
      //   });
      this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$message({
          type: 'success',
          message: '删除成功!'
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    }
  },

  beforeRouteEnter (to, from, next) {
    console.log('局部盘查')
    // if (false) {
    //   next()
    // } else {
    //   next('/login')
    // }
    // 在渲染该组件的对应路由被 confirm 前调用
    // 不！能！获取组件实例 `this`
    // 因为当守卫执行前，组件实例还没被创建
    next()
  }
}
</script>
<style>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
