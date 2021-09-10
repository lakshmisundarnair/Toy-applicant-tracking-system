<template>
  <div>
    <nav-c />

    <v-col v-for="(item, index) in items" :key="index" cols="12">
      <v-card
        class="mx-auto"
        style="box-shadow: 0 12px 15px 0 rgb(0 0 0 / 24%), 0 17px 50px 0 rgb(0 0 0 / 19%);}"
        max-width="1144"
        max-height="100"
        outlined
        color="#385F73"
        dark
      >
        <v-card-title class="text-h6">
          {{ item.title }}
        </v-card-title>

        <v-card-subtitle>{{ item.company_name }} ,<span style="font-size:10px;"> Posted on: {{item.created_at}}</span></v-card-subtitle>

        <v-card-actions>
          <v-dialog v-model="dialog" width="600px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="primary"
                class="text-h9 apply"
                dark
                v-bind="attrs"
                v-on="on"
                @click="returnindex(index)"
              >
                Apply
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">JOB DESCRIPTION</span> 
                </v-card-title
              ><br />
              <v-card-text>
                <span style="font-size: 10px">Posted on :  
                {{ pass.created_at}}</span><br /><br />
                <span style="font-weight: bold">Job_Post</span> :  
                {{ pass.title}}<br /><br />
                <span style="font-weight: bold">Name of company</span> :
                {{ pass.company_name }}<br /><br />
                <span style="font-weight: bold">Salary</span> : 
                {{ pass.salary}}<br /><br />
                <span style="font-weight: bold">Job_type</span> :
                {{ pass.job_type }}<br /><br />
                <span style="font-weight: bold">Qualification</span> :
                {{ pass.qualification }}<br /><br />
                <span style="font-weight: bold">Description</span> :
                {{ pass.description }}<br /><br />
                
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="green darken-1" text @click="close()">
                  Cancle
                </v-btn>
                <v-dialog v-model="dialog2" persistent max-width="600px">
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      color="green darken-1"
                      text
                      dark
                      v-bind="attrs"
                      v-on="on"
                    >
                      Apply Now
                    </v-btn>
                  </template>
                  <v-card>
                    <v-card-title>
                      <span class="text-h5">Apply For {{ pass.title }}</span>
                    </v-card-title>
                    <v-card-text>
                      <div class="cont">
                        <v-row
                          ><input
                            type="hidden"
                            
                            v-model="pass.id"
                          />
                          <input
                            type="hidden"
                           
                            v-model="user.id"
                          />
                          <v-col cols="12"
                            ><v-text-field
                              label="Legal first name*"
                              
                              required
                              v-model="user.name"
                            ></v-text-field>
                          </v-col>

                          <v-col cols="12">
                            <v-text-field
                              label="Email*"
                              required
                              
                              v-model="user.email"
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12">
                            <v-textarea
                              v-model="intro"
                              filled
                              label="Self Introduction"
                              auto-grow
                            ></v-textarea>
                          </v-col>
                          <v-col cols="12"> </v-col>
                          <v-col cols="12" sm="6">
                            <v-text-field
                              label="Qualification*"
                              v-model="qualification"
                              required
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" sm="6">
                            <v-select
                              :items="['Fresher','0-1 years','1-3 years','3-5 years','5+ years']"
                              label="Experiance*"
                              v-model="experiance"
                              required
                            ></v-select>
                          </v-col>
                          <v-col cols="12" sm="6">
                            <v-text-field
                              label="Skills*"
                              v-model="skills"
                              required
                            >
                            </v-text-field>
                          </v-col>
                          <v-col cols="12" sm="6">
                            <v-text-field
                              label="Phone no*"
                              v-model="phone"
                              required
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </div>
                      <small>*indicates required field</small>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="blue darken-1" text @click="close()">
                        Close
                      </v-btn>
                      <v-btn color="blue darken-1" text @click="apply()">
                        Submit
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-card-actions>
      </v-card>
    </v-col>
  </div>
</template>

<script>
import NavC from "./NavCa.vue";
import axios from "axios";

export default {
  data() {
    return {
      dialog: false,
      dialog2: false,
      job_id: "",
      user_id: "",
      user_name: "",
      user_email: "",
      qualification: "",
      phone: "",
      intro: "",
      experiance: "",
      skills: "",
      applied: [],
      pass: [],
      items: [],
    };
  },
  mounted() {
    this.getjob();
  },
  methods: {
    getjob() {
      this.user = JSON.parse(localStorage.getItem("userinfo"));
      axios
        .get("/jobs/notapplied/"+this.user.id)
        .then((res) => {
          this.items = res.data;
          if(res.data==""){
            this.$alert("No Jobs Available yet to apply")
          }
        })
        .catch((error) => {
          this.$alert(error);
        });
    },
    returnindex(index) {
      this.pass = this.items[index];
    },
    apply() {
      if (this.intro == "" &&
        this.qualification == "" &&
        this.experiance == "" &&
        this.skills == "" &&
        this.phone == ""
      ) {
        this.$alert("Please fill the required fields");
      } else {
        axios
        .post("/application/create",  { job_id: this.pass.id,
            user_id: this.user.id,
            user_name: this.user.name,
            user_email: this.user.email,
            intro: this.intro,
            qualification: this.qualification,
            experiance: this.experiance,
            skills: this.skills,
            phone: this.phone} )
        .then((res) => {
          this.applications = res.data;
          if (res.status == 200) {
            this.$router.go()
            this.$alert("Application Submitted Successfully");
            close()
          }
        })
        .catch((error) => {
          this.$alert(error)
        })
        
          

       
      }
    },
    close() {
      (this.qualification = ""),
        (this.phone = ""),
        (this.intro = ""),
        (this.experiance = ""),
        (this.skills = ""),
        (this.dialog = false);
      this.dialog2 = false;
    },
  },

  components: { NavC },
};
</script>

<style lang="scss">
.apply {
  padding: 0 8px;
  position: absolute;
  margin-left: 1000px;
  margin-top: -90px;
}

.cont {
  max-width: 1185px;
  position: relative;
  top: 55%;
  left: 0%;
}
</style>