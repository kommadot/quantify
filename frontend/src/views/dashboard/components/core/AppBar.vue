<template>
  <v-app-bar
    id="app-bar"
    absolute
    app
    color="transparent"
    flat
    height="75"
  >
    <v-btn
      class="mr-3"
      elevation="1"
      fab
      small
      @click="setDrawer(!drawer)"
    >
      <v-icon v-if="value">
        mdi-view-quilt
      </v-icon>

      <v-icon v-else>
        mdi-dots-vertical
      </v-icon>
    </v-btn>



    <v-spacer />

    <v-text-field
      :label="$t('search')"
      color="secondary"
      hide-details
      style="max-width: 500px;"
    >
      <template
        v-if="$vuetify.breakpoint.mdAndUp"
        v-slot:append-outer
      >
        <v-btn
          class="mt-n2"
          elevation="1"
          fab
          small
        >
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </template>
    </v-text-field>

    <div class="mx-3" />

    <v-btn
      class="ml-2"
      min-width="0"
      text
      @click="login"
      dark
    >
      <v-icon>mdi-account</v-icon>
    </v-btn>
    <login-form :dialog="dialog" @closeForm="dialog=false" />
  </v-app-bar>
  
</template>

<script>
  import LoginForm from "@/components/base/LoginForm.vue"
  import { mapState, mapMutations, mapGetters } from 'vuex'

  export default {
    name: 'DashboardCoreAppBar',
    components:{
      LoginForm,
    },
    props: {
      value: {
        type: Boolean,
        default: false,
      },
    },
    data(){
      return {
      dialog:false,
      }
    },
    computed: {
      ...mapState(['drawer']),
      ...mapGetters(['isLoggedIn'])
    },

    methods: {
      ...mapMutations({
        setDrawer: 'SET_DRAWER',
      }),
      login(){
        if(this.isLoggedIn){
          this.$router.push("/pages/user")
        }
        else{
          this.dialog=true
        }
      },

    },
  }
</script>
