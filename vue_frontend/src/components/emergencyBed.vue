<template>
    <app>
        <v-layout wrap> 
          <v-span v-for="person in booking" :key="person">
            <v-flex 
             v-if = "person.bedType == 'emergency' && person.hospital == hospitalName && person.status != 'Released'">
              <v-card color="green" flat class="text-center ma-2">
                <div class="subheading ma-3 py-4">
                  <h4 style="color:white;font-size:20px;text-transform: uppercase;">{{person.patient_name}} {{person.role}}</h4>
                  <emgBooked :name="person.patient_name" :mobile="person.mobile" :disease="person.disease" :address="person.patient_address"/>
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
          v-for="bed in (items.bed.emergency-items.booked.emergency)" 
          :key="bed">
            <span v-if="items.name == hospitalName">
              <v-card color="grey" 
                flat
                class="text-center ma-2"
                >
                  <div class="subheading ma-3 py-4">
                    <h2>Bed {{bed}}</h2>
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
 props: ['booking','hospitals', 'hospitalName']
}
</script>