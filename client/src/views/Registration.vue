<template>
  <v-app id="inspire">
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
          >
            <v-card class="elevation-12">
              <v-toolbar
                color="deep-purple accent-7"
                dark
                flat
              >
              
              <v-toolbar-title @click="bool_login=false" v-bind:class="{ active: !bool_login }">регистрация</v-toolbar-title>
                <v-spacer></v-spacer>
              <v-toolbar-title  @click="bool_login=true" v-bind:class="{ active: bool_login }">вход</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field v-if="bool_login"
                    label="Введите логин" 
                    v-model=login_data.login
                    name="login"
                    prepend-icon="person"
                    type="text"
                  ></v-text-field>
                  <v-text-field v-if="bool_login"
                    label="Введите пароль"
                    name="password"
                    prepend-icon="lock"
                    type="password"
                    v-model=login_data.password 
                  ></v-text-field>
                  <v-text-field v-if="!bool_login"
                    label="Введите логин"
                    name="login"
                    prepend-icon="person"
                    type="text"
                    v-model=registration_data.login
                  ></v-text-field>
                  <v-text-field v-if="!bool_login"
                    label="Введите пароль"
                    name="password"
                    prepend-icon="lock"
                    type="password"
                    v-model=registration_data.password
                  ></v-text-field>
                  <v-text-field v-if="!bool_login"
                    id="password"
                    label="Повторите пароль"
                    name="password"
                    prepend-icon="lock"
                    type="password"
                  ></v-text-field>
                  <v-text-field v-if="!bool_login"
                    id="email"
                    label="Введите Email"
                    name="email"
                    prepend-icon="mail"
                    type="email"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <a v-if="bool_login">Забыли пароль?</a>
                <v-spacer></v-spacer>
                <v-btn class="white--text" color="deep-purple accent-7" v-if="bool_login" @click="sigin_in">
                 Войти
                </v-btn>
                <v-btn class="white--text" color="deep-purple accent-7" v-if="!bool_login" @click="registration">Зарегестрироваться</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  import LoginRegistrations from"@/plugins/requests/LoginRegistration"
  export default {
    props: {
      source: String,
    },
    data: () => ({
      bool_login: true,
      request: new LoginRegistrations,
      responseData: null,
      login_data: {
        login: null,
        password: null,
      },
      registration_data: {
        login: null,
        password: null,
      }
    }),
    methods:{
      sigin_in() {
        this.request.login(this.login_data)
        .then((responseData) => {
          this.responseData = responseData;
          localStorage.setItem('token', this.responseData.data.data.token);
          this.$router.push({name:"filelist"})
        })
      },
      registration() {
        this.request.registration(this.registration_data)
        .then((responseData) => {
          this.responseData = responseData;
          this.bool_login=true
          this.registration_data.login = null
          this.registration_data.password = null
        })
      }
    },
}
</script>

<style scoped="">
.active{
  text-decoration: underline;
  text-transform: uppercase;
}
</style>