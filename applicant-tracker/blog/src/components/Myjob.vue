<template>
  <div>
    <nav-c /><br />
    <v-simple-table fixed-header height="300px">
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">Job Title</th>
            <th class="text-left">Name of Company</th>
            <th>Salary</th>
            <th>Job type</th>
            <th>Applicant</th>
            <th class="text-left">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item,index) in applications" :key="index">
            <td>{{ item.job.title }}</td>
            <td>{{ item.job.company_name }}</td>
            <td>{{ item.job.salary }}</td>
            <td>{{ item.job.job_type }}</td>
            <td>{{ item.applicant.email }}</td>

            <td>
              <v-icon small @click="opendailog(index)">mdi-eye</v-icon> &nbsp;
              <v-icon small @click="deletee(item.id)">
                mdi-delete
              </v-icon>
            </td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
     <v-dialog v-model="dialog" width="600px">
            <v-card>
              <v-card-title>
                <span class="text-h5">SUBMITTED RESPONSE</span> </v-card-title
              ><br />
              <v-card-text>
               <span style="font-weight: bold">Name</span> :  
                {{n}}<br /><br />
                <span style="font-weight: bold">Email</span> :
                {{e}}<br /><br />
                <span style="font-weight: bold">Introduction</span> : 
                {{view.introduction}}<br /><br />
                <span style="font-weight: bold">Qualification</span> :
                {{view.qualification }}<br /><br />
                <span style="font-weight: bold">Experiance</span> :
                {{view.experiance}}<br /><br />
                <span style="font-weight: bold">Skills</span> :
                {{view.skills}}<br /><br />
                <span style="font-weight: bold">Phone no</span> :
                {{view.phone}}<br /><br />
                <span style="font-weight: bold">Submited on</span> :
                {{view.submitted_on}}<br /><br />
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="green darken-1" text @click="close()">
                  Cancel
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
            <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5">Are you sure you want to delete this application?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="dialogDelete=false">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItem()">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
  </div>
</template>

<script>
import NavC from "./NavCa.vue";
import axios from "axios";
export default {
  components: { NavC },
  data() {
    return {
      dialog:false,
      dialogDelete:false,
      applications: [],
      view:[],
    };
  },
  mounted() {
    this.getapplied();
  },
  methods: {
    getapplied() {
      this.id = JSON.parse(localStorage.getItem("userinfo"));

      axios
        .get('/applications/'+this.id.email)
        .then((res) => {
          this.applications = res.data;
        })
        .catch((error) => {
          this.$alert(error);
        });
    },
    deletee(item){
      this.i=item
      this.dialogDelete=true
    },
    deleteItem() {
     
      axios
        .delete("/application/delete/"+ this.i )
        .then((res) => {
          this.applications = res.data
          if (res.status == 200) {
            this.$alert("Successfully deleted") 
             this.$router.go()           
          }
          if(res.status==400){
            this.$alert(res)
          }
        })
       
    },
    opendailog(index){
      this.dialog=true
      this.view=this.applications[index]
      this.n=this.applications[index].applicant.name
      this.e=this.applications[index].applicant.email
    },
    close(){
      this.dialog=false
    }
  },
};
</script>

<style>
.v-data-table > .v-data-table__wrapper > table {
  margin-right: auto !important;
  margin-left: auto !important;
  width: 90%;
  border-spacing: 0;
}
</style>