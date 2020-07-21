<template>
   <v-layout column>
      <v-flex d-flex>
         <v-card flat>
            <v-card
               class="mx-auto"
               min-width="250"
               max-width="250"
               align="center"
               justify="center"
               >
               <v-img
                  :src="require(`../assets/svg/${fileFormat[1]}.svg`)"
                  srcset lazy-src
                  heigth="100px"
                  width="100px"
                  ></v-img>
               <v-card-title>
                  {{fileName}}
               </v-card-title>
               <v-card-subtitle>
               </v-card-subtitle>
               <v-card-actions>
                  <v-btn icon><v-icon >cloud_download</v-icon></v-btn>
                     <v-btn
                     text
                     @click="showShare = !showShare"
                     color="purple"
                     >
                    share
                  </v-btn>
                  <v-spacer></v-spacer>
                  <v-btn
                     icon
                     @click="showDelite = !showDelite"
                     >
                     <v-icon color="red">{{ showDelite ? 'mdi-chevron-down' :  'mdi-bookmark-remove'}}</v-icon>
                  </v-btn>
               </v-card-actions>
               <v-expand-transition >
                  <div v-show="showDelite" > 
                     <v-divider></v-divider>
                     <v-card-text>
                        <span style="color:red" >Delite?</span>
                     </v-card-text>
                  </div>
               </v-expand-transition>
               <v-expand-transition>
                  <div v-show="showShare">
                     <v-divider></v-divider>
                     <v-card-text v-if="sharingLink">
                        http://localhost:8080/#/download?sharing_link={{sharingLink}}
                     </v-card-text>
                     <v-btn
                     icon>
                        <v-icon @click="SharingFile">{{ sharingLink ? 'mdi-share-off ' :  'mdi-share'}}</v-icon>
                     </v-btn>
                     
                     <v-btn text v-if="sharingLink">
                        Copy
                     </v-btn>
                  </div>
               </v-expand-transition>
            </v-card>
         </v-card>
      </v-flex>
   </v-layout>
</template>
<script>
import FileList from "@/plugins/requests/FileList"
export default {

   props: ['fileName', 'sharingLink', 'serverId', 'fileId' ],
   data: () => ({
      showDelite: false,
      showShare: false,
      fileFormat: null,
      filePath: null,
      request: new FileList,
      token: localStorage.getItem("token"),
   }),
   methods:{
      SharingFile() {
        this.request.SharingFile(this.token, this.serverId, this.fileId)
        .then((responseData) => {
          console.log(responseData)
          this.files = responseData.data.files
          this.sharingLink = responseData.data.sharing_link
        })
      }
   },
   beforeMount(){
      this.fileFormat = this.fileName.split(".")
      this.filePath = "@/public/"+this.fileFormat[1]+".svg"
      console.log(this.filePath)
   }
}
</script>