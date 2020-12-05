<template>
    <app>
        <v-layout wrap>
            <v-flex
            xs12 sm6 md3 lg2 
            v-for="person in team" 
            :key="person.name">
            <span v-if="person.name=='2'">
              <v-card color="green" 
                flat
                class="text-center ma-2"
                >
                  <div class="subheading ma-3 py-4">
                    <h2 style="color:white;">Bed {{person.name}}</h2>
                    <emgBooked :name="person.role"/>
                  </div>
                </v-card>
            </span>
            <!-- Booked part end --> 
            <span v-else>
              <v-card color="grey" 
                flat
                class="text-center ma-2"
                >
                  <div class="subheading ma-3 py-4">
                    <h2>Bed {{person.name}}</h2>
                    <emgVacant/>
                  </div>
                </v-card>
            </span>
            </v-flex>
        </v-layout>
    </app>
</template>

<script>
import emgBooked from "./emgBooked";
import emgVacant from "./emgVacant";

export default {
  components:{
      emgBooked,
      emgVacant,
  },
 props: ['team']
}
</script>