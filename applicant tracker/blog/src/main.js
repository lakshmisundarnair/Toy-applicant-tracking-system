import Vue from 'vue'
import axios from 'axios'
import App from './App.vue'
import VueRouter from 'vue-router'
import Login from './components/Login'
import Home from './components/Home'
import Homec from './components/Homec'
import Myjob from './components/Myjob'
import View from './components/View'
import VueSimpleAlert from "vue-simple-alert";
import 'bootstrap/dist/css/bootstrap.min.css'
import '@/assets/css/main.css'
import vuetify from './plugins/vuetify'
Vue.use(VueSimpleAlert)
Vue.use(VueRouter)
axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://127.0.0.1:8000';
const routes=[
  {path:'/',name:'login',component:Login},  
  {path:'/recuriter',name:'recruiter',component:Home},
  {path:'/candidate',name:'candidate',component:Homec},
  {path:'/applied',name:'myjob',component:Myjob},
  {path:'/view',name:'view',component:View},
]
const router=new VueRouter({
  routes
})
Vue.config.productionTip = false

new Vue({
  router:router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
