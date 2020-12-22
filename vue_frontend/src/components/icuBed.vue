<template>
    <app>
        <v-layout wrap> 
          <v-span v-for="person in booking" :key="person">
            <v-flex 
             v-if = "person.bedType == 'icu' && person.hospital == hospitalName && person.status != 'Released'">
              <v-card color="green" flat class="text-center ma-2">
                <div class="subheading ma-3 py-4">
                  <h2 style="color:white;">Bed {{person.role}}</h2>
                  <icuBooked :name="person.patient_name" :mobile="person.mobile" :disease="person.disease" :address="person.patient_address"/>
                </div>
              </v-card>
            </v-flex>
          </v-span>
        </v-layout> 
         <!-- Booked part end --> 
         
        <v-layout wrap
        v-for="items in hospitals" 
        :key="items.name"> 
          <v-flex
          xs12 sm6 md3 lg2 
          v-for="bed in (items.bed.icu-items.booked.icu)" 
          :key="bed">
            <span v-if="items.name == hospitalName">
              <v-card color="grey" 
                flat
                class="text-center ma-2"
                >
                  <div class="subheading ma-3 py-4">
                    <h2>Bed {{bed}}</h2>
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
 props: ['booking','hospitals', 'hospitalName']
}
</script>