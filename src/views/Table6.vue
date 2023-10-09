<template>
  <h1>增加了按钮, 实现了删除功能, 实现了弹窗方式更新数据.</h1>
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
  <br />
  <br />
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

    <el-table-column label="Operations" width="280">
      <template #default="scope">
        <el-button size="small" @click="editRow(scope.row)">Edit</el-button>
        <!-- scope即为表格的当前行. 将当前行数据传入函数editRow,并执行函数中的动作 -->

        <el-button size="small" type="danger" @click="handleDelete(scope.row.name)"
          >Delete</el-button
        >
      </template>
    </el-table-column>
  </el-table>

  <el-dialog v-model="dialogFormVisible" title="Edit Student Data">
    <!-- v-model 双向动态绑定 -->
    <el-form :model="editForm">
      <!-- 用:说明表格 editForm是一个变量, :是实现单向数据绑定的一种便捷方式,这里只能从外部获取数据然后写入表格中,而传不出去. 要传出去, 则要靠下面的v-model.-->
      <el-form-item label="Name" label-width="140px">
        <el-input v-model="editForm.name" autocomplete="off" />
        <!-- 注意这个时候用的是v-model双向绑定,直接将数据写入了虚拟表editForm中 -->
      </el-form-item>
      <el-form-item label="English Score" label-width="140px">
        <el-input v-model="editForm.english" autocomplete="off" />
      </el-form-item>
      <el-form-item label="Math Score" label-width="140px">
        <el-input v-model="editForm.math" autocomplete="off" />
      </el-form-item>
      <el-form-item label="Chinese Score" label-width="140px">
        <el-input v-model="editForm.chinese" autocomplete="off" />
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">Cancel</el-button>
        <el-button type="primary" @click="saveEditedData"> Save </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script lang="ts" setup>
import { ref, onMounted, reactive } from 'vue'
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

const handleDelete = (name) => {
  axios
    .delete('/api/deleteStudentScore', { data: { name } })
    .then((response) => {
      console.log(response.data)
      searchStudentsMulti()
    })
    .catch((error) => {
      console.error(error)
    })
}

const dialogFormVisible = ref(false)
// Create a reactive object for editing student data //ref和reactive功能类似, ref适用于简单数据和对象, reactive适用于复杂数据和对象
const editForm = reactive({
  name: '',
  english: '',
  math: '',
  chinese: ''
})

const editRow = (rowData) => {
  // Populate the editForm with the data of the selected row 将当前中的数据传入了本函数. 并进一步将数据 存入 editForm 这个虚拟的表/变量 中.
  editForm.name = rowData.name
  editForm.english = rowData.english
  editForm.math = rowData.math
  editForm.chinese = rowData.chinese

  // Show the edit dialog
  dialogFormVisible.value = true
}

const saveEditedData = () => {
  // Send the edited data to the server (you can modify this part)
  const name = editForm.name
  const english = editForm.english
  const math = editForm.math
  const chinese = editForm.chinese
  axios
    .put('/api/updateStudentScore', { name, english, math, chinese }) // Use the appropriate endpoint for updating data
    .then((response) => {
      console.log(response.data)
      // Optionally, refresh the student data after editing
      searchStudentsMulti()
      dialogFormVisible.value = false // Close the dialog after saving
    })
    .catch((error) => {
      console.error(error)
    })
}

onMounted(searchStudentsMulti) // 在mounted钩子中调用getStudentScores()
</script>

<style>
.input-with-select .el-input-group__prepend {
  background-color: var(--el-fill-color-blank);
}
</style>
