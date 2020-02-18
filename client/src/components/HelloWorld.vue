<template>
  <div class="hello">
    Login:
    <input type="text" v-model="login">
    <input type="text" v-model="password">
    <button @click="loginRequest()">Login</button>
    <br>

    Register:
    <input type="text" v-model="regLogin">
    <input type="text" v-model="regPassword">
    <button @click="regRequest()">Registration</button>  
  </div>
</template>

<script>
import axios from "axios";
import qs from 'qs';
export default {
  name: 'HelloWorld',
  data() {
    return {
      msg: "HEllo,ping",
      regLogin:'zolk9897',
      regPassword:'zolk1111',
      login:"zolk9897",
      password:"zolk1111"
    }
  },
  props: {
    
  },
  methods: {
    regRequest(){
      var CryptoJS = require("crypto-js");
      const data = { 'username': this.regLogin, "password": CryptoJS.SHA256(this.regPassword).toString(CryptoJS.enc.Base64) };
      const url = 'http://localhost:5000/api/register';
      const options = {
        method: 'POST',
        headers: { 'content-type': 'application/x-www-form-urlencoded' },
        data: qs.stringify(data),
        url,
      };
      axios(options)
      .then(function(response){
        console.log(response)
      });   
    },
    loginRequest(){
      var CryptoJS = require("crypto-js");
      const data = { 'username': this.login, "password": CryptoJS.SHA256(this.password).toString(CryptoJS.enc.Base64)  };
      const url = 'http://localhost:5000/api/login';
      const options = {
        method: 'POST',
        headers: { 'content-type': 'application/x-www-form-urlencoded' },
        data: qs.stringify(data),
        url,
      };
      axios(options)
      .then(function(response){
        console.log(response)
      });   
    },
  },
  created(){
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
