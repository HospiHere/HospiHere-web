<template>
  <v-card>
    <v-card-title>
      Blood Bank
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search Blood"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="donors"
      :search="search"
    ></v-data-table>
  </v-card>
</template>

<script>
  import firebase from 'firebase/app'
  import 'firebase/firestore'
  import Vue from 'vue'
  import { firestorePlugin } from 'vuefire'

  Vue.use(firestorePlugin)

  const db = firebase.initializeApp({ projectId: 'hospihere-bd' }).firestore()

  export default {
    data () {
      return {
        search: '',
        headers: [
          {
            text: 'Mobile',
            align: 'start',
            sortable: false,
            value: 'phone',
          },
          { text: 'Gender', value: 'gender' },
          { text: 'Blood Group', value: 'bloodGroup' },
        ],
        donors: [],
      }
    },

    firestore: {
      donors: db.collection('bank'),
    }
  }
</script>




