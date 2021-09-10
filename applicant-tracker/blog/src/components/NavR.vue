<template>

    <div class="wrap">
  
    <div class="html">
    <nav  class="navbar">
    <img src="icon.png" alt="">   
    <a class="navbar-brand" style="margin-left: -350px;" href="#"> Applicant Tracker</a>  
    <ul>
        <li>
            <router-link to="/recuriter">Home</router-link>
        </li>
        
         <li>
            <router-link to="/view">Applications</router-link>
            
        </li>
        <li>
        <a  href="#" @click="logout">Logout</a>
        </li>
    </ul>
  </nav>
</div>
</div>
 
</template>

<script>

    export default {
         mounted(){
   let user=localStorage.getItem("userinfo")
            
        if(!user){
        this.$router.push({ name: "login" })
        }
   },
        
          
      methods: {
           
             logout() {
                localStorage.clear()
                this.$router.push({ path: "/" })
            }
    }
        
 
      
    }
</script>
