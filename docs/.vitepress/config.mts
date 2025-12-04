import { defineConfig } from 'vitepress'
import fs from 'fs'
import path from 'path'

// Function to generate sidebar dynamically
function getSidebar() {
  const docsDir = path.resolve(__dirname, '..')
  const sidebar = []
  
  // Get all directories in docs
  const dirs = fs.readdirSync(docsDir).filter(file => {
    return fs.statSync(path.join(docsDir, file)).isDirectory() && !file.startsWith('.') && file !== 'public'
  })

  dirs.forEach(dir => {
    const dirPath = path.join(docsDir, dir)
    const files = fs.readdirSync(dirPath).filter(file => file.endsWith('.md'))
    
    const items = files.map(file => {
      const name = path.basename(file, '.md')
      return {
        text: name === 'index' ? 'Overview' : name,
        link: `/${dir}/${name}`
      }
    }).sort((a, b) => {
      // 'index' or 'Overview' always comes first
      if (a.text === 'Overview') return -1
      if (b.text === 'Overview') return 1
      return a.text.localeCompare(b.text)
    })

    sidebar.push({
      text: dir.charAt(0).toUpperCase() + dir.slice(1).replace(/_/g, ' '),
      collapsed: true,
      items: items
    })
  })

  return sidebar
}

export default defineConfig({
  title: "Redis Reference",
  description: "Redis Command Reference",
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Commands', link: '/string/' }
    ],
    sidebar: getSidebar(),
    search: {
      provider: 'local'
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/redis/redis-doc' }
    ]
  }
})
