<template>
  <v-app id="inspire">
    <MainHeader />
    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
      fdjfhlkdj
      </v-container>
    </v-content>
    <v-footer
      color="indigo"
      app
    >
      <span class="white--text">&copy; 2020</span>
    </v-footer>
  </v-app>
</template>

<script>
  import MainHeader from "@/components/MainHeader"
  export default {
    components:{
      MainHeader
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