<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
      color = "deep-purple accent-7"
      dark
      >
      <v-list dense>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>settings_phone</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Contact</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      app
      color="deep-purple accent-7"
      dark
      >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" ></v-app-bar-nav-icon>
      <v-toolbar-title><span style="font-family: 'Roboto', sans-serif;">Midnight Cloud</span></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-title><span style="font-family: 'Roboto', sans-serif;" @click.stop="loadWindow = !loadWindow" >Загрузить файл</span></v-toolbar-title>
    </v-app-bar>
    <v-content>
      <v-container fluid grid-list-sm>
          <v-flex d-flex xs12 order-xs5>
            <v-layout column>
              <v-flex d-flex>
                <v-card   flat>
                  <v-card-text><span style="font-family: 'Roboto', sans-serif;font-size: 30px">Ваши файлы:</span></v-card-text>
                </v-card>
              </v-flex>
            </v-layout>
          </v-flex>
          <v-layout row wrap>
          <div v-for="file in files" :key="file.date">
            <v-flex d-flex xs12 order-xs5>
              <v-layout column>
                <v-flex d-flex>
                  <v-card flat>
                    <v-card-text><span style="font-family: 'Roboto', sans-serif;font-size: 20px">{{file.date}}</span></v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-flex>
            <v-flex d-flex xs12 order-xs5 >
              <v-row>
                <v-col >
                  <FileCard v-bind:file-name="file.name"></FileCard>
                </v-col>
              </v-row>
            </v-flex>
          </div>
        </v-layout>
      </v-container>
    </v-content>
    <v-footer
      color="indigo"
      app
      >
      <span class="white--text">&copy; 2020 Калинин Евгений</span>
    </v-footer>
    <LoadFile v-bind:dialog="loadWindow"></LoadFile>
  </v-app>
</template>
<script>
  import FileList from "@/plugins/requests/FileList"
  import FileCard from "@/components/FileCard"
  import LoadFile from "@/components/LoadFile"
  export default {
    components:{
      FileCard,
      LoadFile
    },
    props: {
      source: String,
    },
    data: () => ({
      request: new FileList,
      drawer: false,
      show: false,
      token: localStorage.getItem("token"),
      files: null,
      loadWindow: false
    }),
    methods:{
      AllFiles() {
        this.request.AllUserFile(this.token)
        .then((responseData) => {
          console.log(responseData)
          this.files = responseData.data.files
        })
      },
    },
    beforeMount(){
      this.AllFiles()
    }
  }
</script>