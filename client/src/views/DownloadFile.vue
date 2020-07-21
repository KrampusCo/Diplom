<template>
  <v-app>
    <MainHeader />
    <v-content>
      <v-container

        class="fill-height"
        fluid
        >
        <v-row
          align="center"
          justify="center"
          >
          <v-col
            cols="12"
            sm="8"
            md="4"
            align="center"
            justify="center"
            v-if="file"
            >
              <v-img
                :src="require(`../assets/svg/png.svg`)"
                srcset lazy-src

                heigth="200px"
                width="200px"
                ></v-img>
              Название: {{file.name}}<br>
              Дата загрузки: {{file.date}}<br>
              Размер: {{file.size}}<br>
              <v-text-field
                id="email"
                label="Пароль от файла"
                prepend-icon="key"
                type="password"
                >
              </v-text-field>
              <v-btn
                text
                color="deep-purple accent-4"
                @click="downloadFile"
                >
                Скачать
              </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
    <MainFooter/>
  </v-app>
</template>

<script>
  import MainHeader from "@/components/MainHeader"
  import MainFooter from "@/components/MainFooter"
  import DownloadFile from "@/plugins/requests/DownloadFile"
  export default {
    components:{
      MainHeader,
      MainFooter,
    },
    props: {
      source: String,
    },
    data: () => ({
     request: new DownloadFile,
     link: null,
     file: null,
     content: ""
    }),
    methods: {
      downloadFile(){
        this.request.downloadFile(this.file.file_id)
        .then((responseData) => {
          console.log(responseData)
          this.content = responseData.data.byte
          let a = document.createElement("a");
          let file = new Blob([this.content], {type: 'application/json'});
          a.href = URL.createObjectURL(file);
          a.download = this.file.name;
          a.click()
        })
      },
    },
    created(){
      this.link = this.$route.query.sharing_link
      this.request.FileInfo(this.link)
      .then((responseData) => {
        console.log(responseData)
        this.file = responseData.data
      })
    }  
  }
</script>

<style scoped="">
h1{
  font-size:3rem;
  font-weight: 300;
}
</style>