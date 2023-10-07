<template>
  <el-table
    :data="students"
    style="width: 100%"
    stripe
    border
    height="550"
    :default-sort="{ prop: 'english', order: 'descending' }"
  >
    <!-- 可选参数: stripe 斑马底纹  border 边框  height="550" 整个表格的高度 均为可选设计参数 -->

    <el-table-column fixed="left" prop="name" label="姓名" width="180" sortable />
    <!--可选参数 固定在左侧或右侧: fixed="right" -->

    <el-table-column prop="english" label="英语成绩" width="180" sortable />
    <!-- 可选参数 排序: sortable 或者 sortable="", 不可以用sortable="true", 原因不明  -->

    <el-table-column prop="math" label="数学成绩" width="180" />
    <el-table-column prop="chinese" label="语文成绩" width="180" />
  </el-table>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
const students = ref([])

const getStudentScores = () => {
  console.log('成功进入了函数getStudentScores中')
  axios
    .get('/api/getStudentScores')
    .then((response) => {
      console.log(response.data)
      students.value = response.data
    })
    .catch((error) => {
      console.error(error)
    })
  console.log('成功退出了函数getStudentScores')
}

onMounted(getStudentScores) // 在mounted钩子中调用getStudentScores()
</script>
