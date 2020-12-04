const cdn = {
    externals: {
        vue: "Vue",
        vuex: "Vuex",
        "vue-router": "VueRouter",
        axios: "axios",
        //   "element-ui": "ELEMENT",
    },
    css: [
        //   'https://lib.baomitu.com/element-ui/2.13.2/theme-chalk/index.css'
        "https://cdn.jsdelivr.net/npm/v-charts/lib/style.min.css",
    ],
    js: [
        "https://cdn.bootcss.com/vue/2.6.10/vue.min.js",
        "https://cdn.bootcss.com/vue-router/3.1.3/vue-router.min.js",
        "https://cdn.bootcss.com/vuex/3.1.2/vuex.min.js",
        //   'https://lib.baomitu.com/element-ui/2.13.2/index.js',
        "https://cdn.bootcss.com/axios/0.19.2/axios.min.js",
        "https://cdn.jsdelivr.net/npm/vue/dist/vue.js",
        "https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js",
        "https://cdn.jsdelivr.net/npm/v-charts/lib/index.min.js",
    ],
}

module.exports = {
    configureWebpack: (config) => {
        config.externals = cdn.externals
    },
    chainWebpack: (config) => {
        // 如果使用多页面打包，使用vue inspect --plugins查看html是否在结果数组中
        config.plugin("html").tap((args) => {
            // html中添加cdn
            args[0].cdn = cdn
            return args
        })
    },
}

// module.exports = {
//     configureWebpack: {
//         externals: {
//             vue: "Vue",
//             vuex: "Vuex",
//             "vue-router": "VueRouter",
//             axios: "axios",
//         },
//     },
// }

// module.exports = {
//     configureWebpack: (config) => {
//         config.externals = {
//             vue: "Vue",
//             // "element-ui": "ELEMENT",
//             "vue-router": "VueRouter",
//             vuex: "Vuex",
//             axios: "axios",
//         }
//     },
//     chainWebpack: (config) => {
//         const cdn = {
//             // 访问https://unpkg.com/element-ui/lib/theme-chalk/index.css获取最新版本
//             css: ["//unpkg.com/element-ui@2.10.1/lib/theme-chalk/index.css"],
//             js: [
//                 "//unpkg.com/vue@2.6.10/dist/vue.min.js", // 访问https://unpkg.com/vue/dist/vue.min.js获取最新版本
//                 "//unpkg.com/vue-router@3.0.6/dist/vue-router.min.js",
//                 "//unpkg.com/vuex@3.1.1/dist/vuex.min.js",
//                 "//unpkg.com/axios@0.19.0/dist/axios.min.js",
//                 // "//unpkg.com/element-ui@2.10.1/lib/index.js",
//             ],
//         }

//         // 如果使用多页面打包，使用vue inspect --plugins查看html是否在结果数组中
//         config.plugin("html").tap((args) => {
//             // html中添加cdn
//             args[0].cdn = cdn
//             return args
//         })
//     },
// }
