<!-- 组合式写法 -->

<template>
  <div><h1>这是table3, 用于学习数据库的查询</h1></div>

  <table>
    <thead>
      <tr>
        <th>姓名</th>
        <th>英语成绩</th>
        <th>数学成绩</th>
        <th>语文成绩</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(student, index) in students" :key="index">
        <td>{{ student.name }}</td>
        <td>{{ student.english }}</td>
        <td>{{ student.math }}</td>
        <td>{{ student.chinese }}</td>
      </tr>
    </tbody>
  </table>
</template>

<!-- vue3 组合式API语法格式写法: -->
<script setup>
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

<style scoped></style>
