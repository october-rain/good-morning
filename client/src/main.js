import Vue from "vue"
import App from "./App.vue"
import router from "./router"
import store from "./store"

import "./assets/styles/reset.css"
import "./assets/styles/border.css"
import 'simplemde/dist/simplemde.min.css'
import 'highlight.js/styles/atom-one-dark.css';

import fastClick from "fastclick"
import VueSimplemde from 'vue-simplemde'
import hljs from 'highlight.js';
import 'github-markdown-css';

window.hljs = hljs;
Vue.component('vue-simplemde', VueSimplemde)
Vue.config.productionTip = false
fastClick.attach(document.body)

new Vue({
    router,
    store,
    render: (h) => h(App),
}).$mount("#app")
