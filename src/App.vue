<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Home from '@/views/Home.vue'
</script>

<template>
  <div>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
      <RouterLink to="/table">Table</RouterLink>
      <RouterLink to="/table2">Table2</RouterLink>
    </nav>

    <RouterView />

    <Home />
  </div>
</template>
