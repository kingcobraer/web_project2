<!-- 组合式写法 -->

<template>
  <div>
    <h1>这是一个表格2</h1>

    <!-- 表单用于新增学生成绩 -->
    <form @submit.prevent="addStudentScore">
      <!-- ## 阻止表单提交. 类似固定写法 ##
      当表单被提交时，首先阻止表单的默认提交行为（例如页面刷新或跳转），然后调用 addStudentScore
      方法处理表单数据。 ## 这种做法在单页面应用SPA中很常见,因为我们通常希望通过 JavaScript
      处理表单数据，而不是通过传统的页面刷新方式。 -->

      <h2>新增学生成绩</h2>
      <div>
        <label for="name">姓名</label>
        <input type="text" id="name" v-model="newStudent.name" required /> ## 必填
      </div>
      <div>
        <label for="english">英语成绩</label>
        <input type="number" id="english" v-model="newStudent.english" required />
      </div>
      <div>
        <label for="math">数学成绩</label>
        <input type="number" id="math" v-model="newStudent.math" required />
      </div>
      <div>
        <label for="chinese">语文成绩</label>
        <input type="number" id="chinese" v-model="newStudent.chinese" required />
      </div>

      <button type="submit">新增学生</button>
    </form>

    <table>
      <thead>
        <tr>
          <th>姓名</th>
          <th>英语成绩</th>
          <th>数学成绩</th>
          <th>语文成绩</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(student, index) in students" :key="index">
          <td>{{ student.name }}</td>
          <td>{{ student.english }}</td>
          <td>{{ student.math }}</td>
          <td>{{ student.chinese }}</td>
          <td>
            <button @click="updateStudentScore(student)">修改</button>
            <button @click="deleteStudentScore(student.name)">删除</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<!-- vue3 组合式API语法格式写法: -->
<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const students = ref([])
const newStudent = ref({
  name: '',
  english: 0,
  math: 0,
  chinese: 0
})

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

const addStudentScore = () => {
  axios
    .post('/api/addStudentScore', newStudent)
    .then((response) => {
      console.log(response.data)
      getStudentScores()
      clearNewStudentData()
    })
    .catch((error) => {
      console.error(error)
    })
}

const updateStudentScore = (student) => {
  const name = student.name
  const english = newStudent.value.english
  const math = newStudent.value.math
  const chinese = newStudent.value.chinese
  axios
    .put('/api/updateStudentScore', { name, english, math, chinese })
    .then((response) => {
      console.log(response.data)
      getStudentScores()
    })
    .catch((error) => {
      console.error(error)
    })
}

const deleteStudentScore = (name) => {
  axios
    .delete('/api/deleteStudentScore', { data: { name } })
    .then((response) => {
      console.log(response.data)
      getStudentScores()
    })
    .catch((error) => {
      console.error(error)
    })
}

const clearNewStudentData = () => {
  newStudent.value.name = ''
  newStudent.value.english = 0
  newStudent.value.math = 0
  newStudent.value.chinese = 0
}

onMounted(getStudentScores) // 在mounted钩子中调用getStudentScores()
</script>

<style scoped>
table {
  border: solid 2px;
}

td,
th {
  border: solid 1px;
}
</style>

<!-- 选项式写法: -->
<!-- <script>
import axios from 'axios'

export default {
  data() {
    return {
      students: [],
      newStudent: {
        name: '',
        english: 0,
        math: 0,
        chinese: 0
      }
    }
  },
  mounted() {
    this.getStudentScores()
  },
  methods: {
    // 查
    getStudentScores() {
      axios
        .get('/api/getStudentScores')
        .then((response) => {
          console.log(response.data)
          this.students = response.data
        })
        .catch((error) => {
          console.error(error)
        })
    },

    // 增
    addStudentScore() {
      axios
        .post('/api/addStudentScore', this.newStudent)
        .then((response) => {
          console.log(response.data)
          this.getStudentScores()
          this.clearNewStudentData()
        })
        .catch((error) => {
          console.error(error)
        })
    },

    // 改   (将当前行的成绩, 修改为 表单中填写的成绩)
    updateStudentScore(student) {
      const name = student.name
      const english = this.newStudent.english
      const math = this.newStudent.math
      const chinese = this.newStudent.chinese
      axios
        .put('/api/updateStudentScore', { name, english, math, chinese })
        .then((response) => {
          console.log(response.data)
          this.getStudentScores()
        })
        .catch((error) => {
          console.error(error)
        })
    },

    // 删
    deleteStudentScore(name) {
      axios
        .delete('/api/deleteStudentScore', { data: { name } })
        .then((response) => {
          console.log(response.data)
          this.getStudentScores()
        })
        .catch((error) => {
          console.error(error)
        })
    },

    // 清空新学生数据
    clearNewStudentData() {
      this.newStudent.name = ''
      this.newStudent.english = 0
      this.newStudent.math = 0
      this.newStudent.chinese = 0
    }
  }
}
</script> -->
