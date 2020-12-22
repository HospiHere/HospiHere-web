<template>
<v-app>
  <v-card>
    <v-toolbar
      dark
      flat
    >
    <v-toolbar-title><h2>Bed Management</h2></v-toolbar-title>
      <template v-slot:extension>
        <v-tabs
          v-model="tabs"
        >
          <v-tab>
            ICU bed
          </v-tab>
          <v-tab>
            Emergency Bed
          </v-tab>
          <v-tab>
            Ward Bed
          </v-tab>
        </v-tabs>
      </template>
    </v-toolbar>

    <v-tabs-items v-model="tabs">
      <!-- ICU bed-->
      <v-tab-item>
        <icuBed :booking="booking" :hospitals="hospitals" :hospiName="hospital" :hospitalName="hospitalName"/>
      </v-tab-item>

      <!-- Emergency bed-->    
      <v-tab-item>
        <emergency-bed :booking="booking" :hospitals="hospitals" :hospitalName="hospitalName"/>
      </v-tab-item>
      
      <!-- Ward bed-->
      <v-tab-item>
        <ward-bed :booking="booking" :hospitals="hospitals" :hospitalName="hospitalName"/>
      </v-tab-item>
      
    </v-tabs-items>
  </v-card>
  </v-app>
</template>


<script>
  import firebase from 'firebase/app'
  import 'firebase/firestore'
  import Vue from 'vue'
  import { firestorePlugin } from 'vuefire'

  import EmergencyBed from './components/emergencyBed.vue';
  import icuBed from "./components/icuBed";
  import WardBed from './components/wardBed.vue';

  Vue.use(firestorePlugin)
  const db = firebase.initializeApp({ projectId: 'hospihere-bd' }).firestore()

  var hospital = document.getElementById("hospitalName").value;
  console.log("....");
  console.log(hospital);
  console.log("...");

  export default {
    
    components:{
        icuBed,
        EmergencyBed,
        WardBed,
    },
    firestore: {
      booking: db.collection('booking'),
      hospitals: db.collection('hospitals'),
    },
    data () {
      return {
        dialog: false,
        booking: [],
        hospitals: [],
        tabs: null,
        hospitalName: hospital,
      }
    },
  }
</script>
