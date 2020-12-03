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
        <icuBed :booked="booked" :hospitals="hospitals"/>
      </v-tab-item>    
      <v-tab-item>
        <!-- Emergency bed-->
        <emergency-bed :team="team"/>
      </v-tab-item>
      <v-tab-item>
        <!-- Ward bed-->
        <v-card flat>
          <v-card-title class="headline">
            An even better title
          </v-card-title>
          <v-card-text>
            <p>
              Maecenas ullamcorper, dui et placerat feugiat, eros pede varius nisi, condimentum viverra felis nunc et lorem. Sed hendrerit. Maecenas malesuada. Vestibulum ullamcorper mauris at ligula. Proin faucibus arcu quis ante.
            </p>

            <p class="mb-0">
              Etiam vitae tortor. Curabitur ullamcorper ultricies nisi. Sed magna purus, fermentum eu, tincidunt eu, varius ut, felis. Aliquam lobortis. Suspendisse potenti.
            </p>
          </v-card-text>
        </v-card>
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

Vue.use(firestorePlugin)
const db = firebase.initializeApp({ projectId: 'hospihere-bd' }).firestore()

  export default {
    components:{
      icuBed,
      EmergencyBed,
    },
    firestore: {
      booked: db.collection('booking'),
      hospitals: db.collection('hospitals'),
    },
    data () {
      return {
        dialog: false,
        booked: [],
        hospitals: [],
        tabs: null,
        text: 'Lorem ipsum dolor sit amet. Ut laboris nisi ut aliquip ex ea commodo consequat.',
      }
    },
  }
</script>
