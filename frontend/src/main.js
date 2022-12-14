// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'

Vue.config.productionTip = false
// set a prototype for http
Vue.prototype.$http = axios

/* eslint-disable no-new */
/* eslint indent: ["error", 4, { "ignoredNodes": ["ConditionalExpression"] }] */
new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
})
