<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">User Profile</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-file-input label="File input" v-model="file"></v-file-input>
              </v-col>
              <v-col cols="12">
                <v-text-field label="Password*" type="password" prepend-icon="lock" required v-model="key"></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click="CreateFile">Load</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
import FileList from "@/plugins/requests/FileList"
export default {
  props: ['dialog'],
  data: () => ({
    request: new FileList,
    filetext: null,
    file: null,
    key: null,
    ipserver: null,
    content: null,
    token: localStorage.getItem("token"),
  }),
  methods:{
    CreateFile(){
      console.log(this.file.name)
        this.request.CreateFile(this.token, this.file.name, this.file.size, this.key)
        .then((responseData) => {
          this.UploadFile(responseData.data.server_ip, responseData.data.file_id)
      })
    },
    UploadFile(server_ip, file_id){
      let reader = new FileReader()
      reader.readAsText(this.file)
      reader.onload = function() {
        let request = new FileList
        request.uploadFile(localStorage.getItem("token"), server_ip, file_id, reader.result)
          .then((responseData) => {
          console.log(responseData)
      })
      };
    }
  }
}
</script>