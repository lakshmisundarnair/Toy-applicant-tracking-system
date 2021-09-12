<template>
<div >
   
<loading></loading>
    <h1><br/></h1>
    <h1></h1>
  <br>
 
<v-data-table
    :headers="headers"
    :items="desserts"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>My Jobs</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              New Item
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <div class="cointain">
                <v-row>
                  <v-col
                    cols="12"
                  >
                    <v-text-field
                      v-model="editedItem.title"
                      label="Job Title*"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                   
                  >
                    <v-text-field
                      v-model="editedItem.company_name"
                      label="Company Name & Location*"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    
                  >
                    <v-text-field
                      v-model="editedItem.salary"
                      label="Salary*"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    
                  >
                    <v-textarea
                      filled
                      auto-grow
                      v-model="editedItem.description"
                      label="Description*"
                    ></v-textarea>
                  </v-col>
                  <v-col
                    cols="12"
                  >
                    <v-select
                      :items="['Full Time','Part Time','Internship']"
                      v-model="editedItem.job_type"
                      label="Job Type*"
                    ></v-select></v-col><v-col
                    cols="12"
                  > <v-text-field
                      v-model="editedItem.qualification"
                      label="Qualification*"
                    ></v-text-field>
                     
                  </v-col>
                </v-row>
              </div>
              <small>*indicates required field</small>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="save"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5">Are you sure you want to delete this job?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm()">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>

  </v-data-table>
</div>
</template>
<script>

import Loading from './NavR.vue'
import axios from 'axios'
export default {
 
   data(){
    return{
     dialog: false,
      dialogDelete: false,
      headers: [
        { text: 'Job Title',align: 'start',sortable: false,value: 'title',},
        { text: 'Company Name  & Location', value: 'company_name' },
        { text: 'Salary', value: 'salary' },
        { text: 'Job Description', value: 'description' },
        { text: 'Job Type', value: 'job_type' },
        { text: 'Qualification', value: 'qualification' },
        { text: 'Created Date', value: 'created_at' },
        { text: 'Actions', value: 'actions', sortable: false },
      ],
      desserts: [],
      editedIndex: -1,
      editedItem: {
        title: '',
        company_name: '',
        salary: '',
        description: '',
        job_type: '',
        qualification:'',
     
      },
   
      
      msg:''
    }
   },
   
  
  components: { Loading },
 
  name:'home',
 
  computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

  
  created(){
    this.initialize()
  },
 methods: {
      initialize () {
        this.id = JSON.parse(localStorage.getItem("userinfo"));
        axios
        .get("/jobs/"+this.id.email)
        .then((res) => {
          
          if (res.status == 200) {
            this.desserts = res.data;
            
          }
        })
        .catch((error) => {
          this.$alert(error);
        });
        
      },

      editItem (item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
      
        this.editedIndex = item.id
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        
           
      axios
        .delete("/job/delete/"+ this.editedIndex)
        .then((res) => {
          this.applications = res.data
          if (res.status == 200) {
            this.$alert("Successfully deleted")
            this.$router.go()
            
          }
        })
        .catch((error) => {
          this.$alert(error)
        })
        this.closeDelete()
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete () {
        this.dialogDelete = false
      
      },

      save () {
        if (this.editedIndex > -1) {
          var json=this.editedItem
          axios
        .put("/job/edit/"+json.id,{
            title: json.title,
            company_name: json.company_name,
            description:  json.description,
            qualification: json.qualification,
            job_type: json.job_type,
            salary: json.salary
            } )
        .then((res) => {
          this.applications = res.data;
          if (res.status == 200) {
            this.$router.go()
            this.$alert("Changes Modified Successfully");
            close()
          }
        })
        .catch((error) => {
          this.$alert(error)
        })
       
        } else if (this.editedItem.title == '' &&
        this.editedItem.qualification == '' &&
        this.editedItem.job_type == '' &&
        this.editedItem.company_name == '' &&
        this.editedItem.salary == ''&&
        this.editedItem.description==''
      ){
        this.$alert("Please fill the required fields");
      }else{
          var json2=this.editedItem
          axios
        .post("/create/job/"+this.id.email,  {
            title: json2.title,
            company_name: json2.company_name,
        salary:json2.salary,
        description: json2.description,
        job_type: json2.job_type,
        qualification: json2.qualification

            })
        .then((res) => {
          this.applications = res.data;
          if (res.status == 200) {
            this.$router.go()
            this.$alert("Job Created Successfully");
            close()
          }
        })
        .catch((error) => {
          this.$alert(error)
        })
       
        }
        this.close()
      },
    },
  

}
</script>
<style lang="scss">
.contain {
    width: 100%;
    padding: 12px;
    margin-right: auto;
    margin-left: auto;
}
</style>

