<template>
    <app>
        <v-layout wrap>
            <v-flex
            xs12 sm6 md3 lg2 
            v-for="person in booked" 
            :key="person.name">
            <span v-if="person.bedType=='icu'">
              <v-card color="green" 
                flat
                class="text-center ma-2"
                >
                  <div class="subheading ma-3 py-4">
                    <h2 style="color:white;">Bed {{person.bedType}}</h2>
                    <icuBooked :passion="person.role"/>
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
                    <icuVacant/>
                  </div>
                </v-card>
            </span>
            </v-flex>
        </v-layout>
    </app>
</template>

<script>
import icuBooked from "./icuBooked";
import icuVacant from "./icuVacant";

export default {
  components:{
      icuBooked,
      icuVacant,
  },
 props: ['booked','hospitals']
}
</script>