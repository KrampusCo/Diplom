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
                     <v-card-text v-if="shareLink">
                        {{shareLink}}
                     </v-card-text>
                     <v-btn
                     icon>
                        <v-icon>{{ shareLink ? 'mdi-share-off ' :  'mdi-share'}}</v-icon>
                     </v-btn>
                     
                     <v-btn text v-if="shareLink">
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

export default {
   props: ['fileName'],
   data: () => ({
      showDelite: false,
      showShare: false,
      shareLink: "http://localhost:5000/sTyhP",
      fileFormat: null,
      filePath: null,
   }),
   beforeMount(){
      this.fileFormat = this.fileName.split(".")
      this.filePath = "@/public/"+this.fileFormat[1]+".svg"
      console.log(this.filePath)
   }
}
</script>