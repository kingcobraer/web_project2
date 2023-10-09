<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div>
    <nav class="nav-container">
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
      <RouterLink to="/table">Table</RouterLink>
      <RouterLink to="/table2">Table2</RouterLink>
      <RouterLink to="/table3">Table3</RouterLink>
      <RouterLink to="/table4">Table4</RouterLink>
      <RouterLink to="/table5">Table5</RouterLink>
      <RouterLink to="/table6">Table6</RouterLink>
    </nav>

    <RouterView />
  </div>
</template>

<style>
/* 添加边框样式到RouterLink元素 */
.nav-container {
  /* 设置边框为2像素，颜色为#ccc，也就是灰色的背景色 */
  border: 2px solid #ccc;
  /* 设置内边距为10像素 */
  padding: 10px;
  /* 设置外边距的底部为20像素 */
  margin-bottom: 20px;
  /* 设置宽度为100% */
  width: 100%;
  /* 设置字体大小为20像素 */
  font-size: 20px;
  /* 设置文本居中 */
  text-align: center;
  /* 设置内边距的顶部为2个 rem */
  margin-top: 2rem;
  /* 设置容器为flex布局 */
  display: flex;
  /* 设置主轴上的对齐方式为居中 */
  justify-content: center;
  /* 设置交叉轴上的对齐方式为居中 */
  align-items: center;
  /* 设置flex容器是否换行 */
  flex-wrap: wrap;
  /* 设置容器中的子元素之间的间距为1个rem */
  gap: 1rem;
}
</style>
