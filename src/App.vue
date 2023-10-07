<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
      <RouterLink to="/table">Table</RouterLink>
      <RouterLink to="/table2">Table2</RouterLink>
      <RouterLink to="/table3">Table3</RouterLink>
    </nav>

    <RouterView />
  </div>
</template>
