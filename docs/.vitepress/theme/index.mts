import DefaultTheme from 'vitepress/theme';
import giscusTalk from 'vitepress-plugin-comment-with-giscus';
import 'viewerjs/dist/viewer.min.css';
import imageViewer from 'vitepress-plugin-image-viewer';
import { useData, useRoute } from 'vitepress';

export default {
    ...DefaultTheme,
    enhanceApp(ctx) {
        DefaultTheme.enhanceApp(ctx);
    },
    setup() {
        // Get frontmatter and route
        const { frontmatter } = useData();
        const route = useRoute();

        // Obtain configuration from: https://giscus.app/
        giscusTalk({
            repo: 'imvkmark/docs-redis',
            repoId: 'R_kgDOQieiow',
            categoryId: 'DIC_kwDOQieio84CzZA8',
            mapping: 'pathname' // default: `pathname`
        }, {
            frontmatter, route
        });

        imageViewer(route);
    }
};