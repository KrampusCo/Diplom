<template >
  <v-app >
    <MainHeader />

    <v-content >
      <v-container
        class="fill-width"
        fluid
        black
        py-6
        py-md-12
        deep-purple accent-7
        >
      <section id="home-hero" class="container py-6 py-md-12 white--text py-4 py-md-12 container--fluid" >
         <div class="v-responsive mx-auto pa-6" style="min-height:20vh;max-width:1304px;">
            <div class="v-responsive__content">
               <div class="container pa-0">
                  <div class="row align-center">
                     <div class="col-md-7 col-12">
                        <div class="v-responsive overflow-visible" style="max-width:625px;">
                           <div class="v-responsive__content">
                              <div class="base-title home-hero__title mb-4">
                                 <div class="v-markdown">
                                    <h1>
                                      Ваше безопасное облачное хранилище
                                    </h1>
                                 </div>
                              </div>
                              <div class="font-weight-light mb-3 title text--lighten-4 grey--text">
                                 <div class="v-markdown">
                                    <p>
                                      Данное облачное хранилище использует шифрование перед отправкой ваших данных на сервер хранения
                                      для того что бы защитить ваши файлы от злоумышлеников.
                                    </p>
                                 </div>
                              </div>
                              <div class="py-4"></div>
                              <div class="d-flex flex-wrap justify-left justify-sm-center justify-md-start align-center mx-n2">
                                <router-link to="/registration/" class="primary--text ma-2 grow v-btn v-btn--router theme--light elevation-6 v-size--x-large white">
                                <span class="v-btn__content">
                                  <i aria-hidden="true" class="v-icon notranslate v-icon--left mdi mdi-file theme--light" style="font-size:20px;">
                                  </i>
                                 Начать
                                 </span>
                                </router-link>
                                <a href="/ru/introduction/why-vuetify/" class="ma-1 grow v-btn v-btn--depressed v-btn--flat v-btn--outlined v-btn--router theme--light v-size--x-large white--text">
                                  <span class="v-btn__content">
                                    <i aria-hidden="true" class="v-icon notranslate v-icon--left mdi mdi-github theme--light" style="font-size:20px;">
                                    </i>
                                  Github
                                  </span>
                                </a>
                                <a href="https://github.com/vuetifyjs/vuetify" target="_blank" rel="nofollower noopener" class="ma-2 grow v-btn v-btn--depressed theme--light v-size--x-large grey lighten-5" style="min-width:187px;"><span class="v-btn__content">
                                  <i aria-hidden="true" class="notranslate  theme--light" style="font-size:20px;">
                                  </i>
                                 Почему Midnight Cloud?
                                 </span>
                                </a>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-md-5 col-12">
                        <div class="v-card--hero  v-sheet ">
                          <v-img src="@/assets/cloud.png">
                        </v-img>
                      </div>
                     </div>
                  </div>
               </div>
            </div>
         </div>
        </section>
      </v-container>
      <v-container>
        <h1 style="padding: 10px 0 20px 0">Почему именно Midnight Cloud?</h1>
        <section class="row align-center">
          <v-card
    class="mx-auto"
    max-width="344"
          >
            <v-card-text>
              <p class="display-1 text--primary">
                Использование шифрования
              </p>
              <div class="v-card--hero  v-sheet ">
                <v-img src="@/assets/key.png"></v-img>
              </div>
              <p></p>
              <div class="text--primary" style="min-height: 154px">
                Ваши данные будут храниться <br>
                в нечитаемом виде. <br>
                Передача ключей ведётся <br>
                методом F2F(friend-to-friend).<br>
                Это значит что доступ к ключу <br>
                имеете только вы и ваши друзья<br>
                которым вы его доверите.
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn
                text
                color="deep-purple accent-4"
              >
                Читать больше
              </v-btn>
            </v-card-actions>
          </v-card>
            <v-card
            class="mx-auto"
            max-width="344"
          >
            <v-card-text>
              <p class="display-1 text--primary">
                Полностью анонимно
              </p>
              <div class="v-card--hero  v-sheet ">
                <v-img src="@/assets/anonym.png"></v-img>
              </div>
              <p></p>
              <div class="text--primary" style="min-height: 154px">
                Определить владельца файла<br>
                сторонним лицам невозможно.<br>
                При регистрации от вас потребуется<br>
                Только E-mail, логин и пароль.
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn
                text
                color="deep-purple accent-4"
              >
                Читать больше
              </v-btn>
            </v-card-actions>
          </v-card>
            <v-card
            class="mx-auto"
            max-width="344"
          >
            <v-card-text>
              <p class="display-1 text--primary">
                Распределение нагрузок
              </p>
              <div class="v-card--hero  v-sheet ">
                <v-img src="@/assets/server.png"></v-img>
              </div>
              <p></p>
              <div class="text--primary" style="min-height: 154px">
                Для хранения используется<br>
                несколько серверов<br>
                Данная технология позволяет<br>
                с большей скоростью загружать<br>
                ваши файлы.
              </div>
            </v-card-text>
            <v-card-actions>
              <v-btn
                text
                color="deep-purple accent-4"
              >
                Читать больше
              </v-btn>
            </v-card-actions>
          </v-card>
        </section>
      </v-container>
    </v-content>
    <MainFooter/>
  </v-app>
</template>

<script>
  import MainHeader from "@/components/MainHeader"
  import MainFooter from "@/components/MainFooter"
  export default {
    components:{
      MainHeader,
      MainFooter,
    },
    props: {
      source: String,
    },
    data: () => ({
     
    }),
    methods: {
      
    }
  }
</script>

<style scoped="">
h1{
  font-size:3rem;
  font-weight: 300;
}
</style>