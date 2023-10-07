<!-- 组合式写法 -->

<template>
  <div><h1>这是table3, 用于学习数据库的查询</h1></div>

  <el-input v-model="searchTerm" placeholder="Please input" @input="searchStudents" />
  <!--  -->
  <br />
  <br />
  <h4>这是你刚刚输入的内容:</h4>
  <h1>{{ searchTerm }}</h1>
  <br /><br /><br /><br />

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

const searchTerm = ref('')

const students = ref([])

const searchStudents = () => {
  console.log('成功进入了函数searchStudents中')
  axios
    .get('/api/getStudentScoresSearchName', { params: { search: searchTerm.value } }) // 将搜索词作为查询参数传递})

    .then((response) => {
      console.log(response.data)
      students.value = response.data
    })
    .catch((error) => {
      console.error(error)
    })
  console.log('成功退出了函数getStudentScores')
}

onMounted(searchStudents) // 在mounted钩子中调用getStudentScores()
</script>

<style scoped></style>
