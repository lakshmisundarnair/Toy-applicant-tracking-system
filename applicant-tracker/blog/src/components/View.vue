<template>
<div>
    <loading/><br>
    <v-alert
    class="mx-auto"
      color="#2A3B4D"
      dark
      dense
      icon="mdi-message-text"
      prominent
       v-for="(item,index) in applications"
          :key="item"
      style="box-shadow: 0 12px 15px 0 rgb(0 0 0 / 24%), 0 17px 50px 0 rgb(0 0 0 / 19%);width: 90%;">
    <v-row aalign="center" >
        <v-col class="grow">
           <span style="font-weight: 100;">Applications reicived for : </span>{{item.title}}  <span style="font-weight: 100; font-size:12px;"> created on : {{item.created_at}} </span>  
        </v-col>
        <v-col class="shrink" >
          <v-btn style="top: -6px;" v-bind="attrs"
          v-on="on" @click="returnindex(index)">View Applications</v-btn>
   
            
        </v-col>
    </v-row>
    </v-alert>
       <v-dialog
      v-model="dialog"
      width="600px"
    >
       <v-card>
        <v-card-title>
          <span class="text-h5">CANDIDATE DETIALS</span>
          
        </v-card-title>
        <v-card-title>
          <span style="font-size:15px;">No of candidate applied: </span>&nbsp;{{count}}
        </v-card-title>
          <v-card-text v-for="items in applicants" :key="items"><br>
          <span style="font-weight: bold;">Name</span> : {{items.applicant.name}}<br><br>
          <span style="font-weight: bold;">Email</span> : {{items.applicant.email}}<br><br>
          <span style="font-weight: bold;">Self Intro by Candidate</span> : {{items.introduction}}<br><br>
          <span style="font-weight: bold;">Qualification</span> : {{items.qualification}} <br><br>
          <span style="font-weight: bold;">Experiance</span> : {{items.experiance}}<br><br>
          <span style="font-weight: bold;">Skills</span> : {{items.skills}}<br><br>
          <span style="font-weight: bold;">Phone no</span> : {{items.phone}}<br><br>
          <span style="font-weight: bold;">Application Submitted on</span> : {{items.submitted_on}}<br><br>
          ***************************************************************************************
          </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="green darken-1"
            text
            @click="close()"
           >
            Cancel
          </v-btn>
        </v-card-actions>
  
      </v-card>
     </v-dialog> 
</div>
  
</template>

<script>
import Loading from './NavR.vue'
import axios from 'axios'
export default {
    data(){
    return{
      dialog: false,
      applications:[],
      job:[],
      applicants:[]
    }
    },
    components:{Loading},
    mounted(){
      this.getapplication()
    },
    methods:{
      getapplication(){
        this.id=JSON.parse(localStorage.getItem("userinfo"))
      
      axios.get('/jobs/'+this.id.email).then((res)=>{
        this.applications=res.data
        
        
        
      }).catch((error)=>{this.$alert(error)})
      },
       returnindex(index){
         var arr=[]
         this.dialog=true
         var json=this.applications

          for(var i=0;i<json[index].application.length;i++){
           arr.push(json[index].application[i])
          }
          
          this.applicants=arr
          
          this.count=json[index].application.length

    },
    close(){
      this.dialog=false
    }
    }
}
</script>

<style>

</style>