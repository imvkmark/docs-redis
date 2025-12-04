<script setup>
import DefaultTheme from 'vitepress/theme'
import { useData } from 'vitepress'
import Giscus from '@giscus/vue'

const { Layout } = DefaultTheme
const { isDark } = useData()
</script>

<template>
  <Layout>
    <template #doc-after>
      <div style="margin-top: 24px">
        <Giscus
          repo="your-repo/name"
          repo-id="your-repo-id"
          category="Announcements"
          category-id="your-category-id"
          mapping="pathname"
          strict="0"
          reactions-enabled="1"
          emit-metadata="0"
          input-position="top"
          :theme="isDark ? 'dark' : 'light'"
          lang="zh-CN"
          loading="lazy"
        />
      </div>
    </template>
  </Layout>
</template>
