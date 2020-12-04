import Vue from "vue"
import hljs from 'highlight.js/lib/core';
window.hljs = hljs;
import javascript from "highlight.js/lib/languages/javascript"
import 'github-markdown-css';


hljs.registerLanguage("javascript", javascript)
Vue.directive("highlight", function(el) {
    let blocks = el.querySelectorAll("pre code")
    blocks.forEach((block) => {
        hljs.highlightBlock(block)
    })
})

