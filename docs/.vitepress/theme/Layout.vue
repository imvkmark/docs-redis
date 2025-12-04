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
          repo="imvkmark/docs-redis"
          repo-id="R_kgDOQieiow"
          category="Announcements"
          category-id="DIC_kwDOQieio84CzZA8"
          mapping="pathname"
          strict="0"
          reactions-enabled="1"
          emit-metadata="0"
          input-position="bottom"
          :theme="isDark ? 'dark' : 'light'"
          lang="zh-CN"
          loading="lazy"
        />
      </div>
    </template>
  </Layout>
</template>
