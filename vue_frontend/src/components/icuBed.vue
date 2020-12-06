<template>
    <app>
        <v-layout wrap v-for="person in hospitals" 
            :key="person.name">
          <v-layout wrap v-if="person.name =='Birdem'">
            <v-flex
            xs12 sm6 md3 lg2 
            v-for="bed in person.bed.icu" :key="bed">
              <v-card color="green" 
                flat
                class="text-center ma-2">
                  <div class="subheading ma-3 py-4">
                    <h2 style="color:white;">Bed {{bed}}</h2>
                    <icuBooked :passion="person.role"/>
                  </div>
              </v-card>  
            </v-flex> 

            <!-- Booked part end --> 
            <v-flex
            xs12 sm6 md3 lg2 
            v-for="bed in person.bed.emergency" :key="bed">
              <v-card color="grey" 
                flat
                class="text-center ma-2"
                >
                  <div class="subheading ma-3 py-4">
                    <h2>Bed {{bed}}</h2>
                    <icuVacant/>
                  </div>
                </v-card>
            </v-flex>
            </v-layout>
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