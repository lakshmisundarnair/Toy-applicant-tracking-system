<template>
<div>
   
     <div class="login-wrap">
       
            <div class="login-html">
                <h1   style="margin-top: 2ex; font-size:4ex; text-color:white;">Applicant Tracker</h1>
                
                <input id="tab-1" type="radio" name="tab" class="sign-in" checked><label for="tab-1" class="tab"  >Sign In</label>
                
                
                <div class="login-form">
                    <div class="sign-in-htm">
                       <form @submit.prevent="login">
                            <div class="group" style="display: block;">
                                <label  class="label" >Email</label>
                                <input name="username" v-model="input.username"  type="text" class="input" >
                            </div>
                            <div class="group" style="    display: block;">
                                <label  class="label">Password</label>
                                <input name="password" v-model="input.password" type="password" class="input" data-type="password">
                            </div>
                        
                            <div class="group">
                                <button class="button" type="submit" >Sign In</button>
                            </div>
                       </form>
                        <div class="hr"></div>
                         
                    
                    </div>
              

                </div>
            </div>
      
</div>
</div>
</template>

<script>
import axios from 'axios'
    export default {
        name: 'Login',
        a:String,
        result:[],
        isLogin:false,
        data() {
            return {
                input: {
                    username: "",
                    password: "",
                    msg:''
                }
            }
        },
        mounted(){
         var arr=JSON.parse(localStorage.getItem("userinfo")) 
          this.getmsg()
        let user=arr.type
            
        if(user=="candidate"){
        this.$router.push({ name: "candidate" })
        }
        if(user=="recruiter"){
        this.$router.push({ name: "recruiter" })
            }
        },
            
        methods: {
            login() {
                 var json=this.msg
                            
                if(this.input.username != "" && this.input.password != "") {
                    for(var i=0;i<json.length;i++){
                    if(this.input.username != json[i].email && this.input.password != json[i].password) {
                     this.$alert("invalid email id or password") 
                    }
                    if(json[i].type=="recruiter"){    
                    if(this.input.username == json[i].email && this.input.password == json[i].password) {
                       
                        localStorage.setItem("userinfo",JSON.stringify(json[i]))
                        this.$router.push({ name: "recruiter"})
                    }                   
                    }else if(json[i].type=="candidate") {
                        if(this.input.username == json[i].email && this.input.password == json[i].password) {
                      
                        localStorage.setItem("userinfo",JSON.stringify(json[i]))
                        this.$router.replace({ name: "candidate"})
                    }
                    } }
                    
                   
                    
                } else {
                    this.$alert("A username and password must be present");
                }
                
            },
              getmsg(){
             axios.get('/users').then((res)=>{
             this.msg=res.data
              
       
     }).catch((error)=>{
        this.$alert(error);
     })
    },
        }
    }
</script>
<style lang="scss">

</style>
