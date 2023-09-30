//  本文件,一旦修改, 必须control + C 停止并重启vue项目.

import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// 配置vite官方文档: https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },

  // 配置反向代理:
  server: {
    proxy: {
      '/api': {
        // target: 'http://127.0.0.1:5000',
        target: 'http://127.0.0.1:8088',
        changeOrigin: true
      }
    }
  },
  base: './' // 手工添加, 设置这个为相对路径,解决vue项目子目录404问题. --未解决问题!--20230917
})
