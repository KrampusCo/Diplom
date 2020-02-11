<template>
  <div class="hello">
    Login:
    <input type="text" name="login">
    <input type="text" name="password">
    
    <button>Login</button>
    <br>
    Register:
    <input type="text" name="reglogin">
    <input type="text" name="regPassword">
    <input type="text" name="regRepPassword">
    <button>Registration</button>  
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: 'HelloWorld',
  data() {
    return {
      msg: "HEllo,ping"
    }
  },
  props: {
    
  },
  methods: {
    getMessage(){
      const path = 'http://localhost:5000/ping';
      axios.get(path)
      .then((res)=>{
        this.msg+="-"+res.data;
      })
      .catch((error)=>{
        console.log(error)
      })
    }
  },
  created(){
    this.getMessage();
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
