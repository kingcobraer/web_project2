<template>
  <h1>多条件查询</h1>
  <br /><br />
  <div class="mt-4">
    <el-input
      v-model="input3"
      placeholder="Please input"
      class="input-with-select"
      @input="searchStudentsMulti"
    >
      <template #prepend>
        <el-select
          v-model="select"
          placeholder="Select"
          style="width: 115px"
          @change="searchStudentsMulti"
        >
          <el-option label="姓名" value="name" />
          <el-option label="英语成绩" value="english" />
          <el-option label="数学成绩" value="math" />
        </el-select>
      </template>
      <template #append>
        <el-button :icon="Search" />
      </template>
    </el-input>
  </div>
  <h1>选择的是: {{ select }}</h1>
  <h1>输入的是: {{ input3 }}</h1>
  <br /><br />
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
import { Search } from '@element-plus/icons-vue'
const input3 = ref('')
const select = ref('')

import axios from 'axios'
const students = ref([])
const searchStudentsMulti = () => {
  console.log('成功进入了函数searchStudentsMulti中')
  axios
    .get('/api/getStudentScoresSearchMulti', {
      params: { search: { col: select.value, content: input3.value } }
    }) // 将搜索词作为查询参数传递, 后端将接受到search中的整个对象

    .then((response) => {
      console.log(response.data)
      students.value = response.data
    })
    .catch((error) => {
      console.error(error)
    })
  console.log('成功退出了函数getStudentScoresMulti')
}

onMounted(searchStudentsMulti) // 在mounted钩子中调用getStudentScores()
</script>

<style>
.input-with-select .el-input-group__prepend {
  background-color: var(--el-fill-color-blank);
}
</style>
