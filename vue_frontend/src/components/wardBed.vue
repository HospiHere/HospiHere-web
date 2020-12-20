<template>
    <app>
        <v-layout wrap> 
          <v-span v-for="person in booking" :key="person">
            <v-flex 
             v-if = "person.bedType == 'ward' && person.hospital == 'hospiName'">
              <v-card color="green" flat class="text-center ma-2">
                <div class="subheading ma-3 py-4">
                  <h2 style="color:white;">Bed {{hospiName }}</h2>
                  <wardBooked :name="person.patient_name" :mobile="person.mobile" :disease="person.disease"/>
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
          v-for="bed in items.bed.ward" 
          :key="bed">
            <span v-if="items.name == 'Monwara'">
              <v-card color="grey" 
                flat
                class="text-center ma-2"
                >
                  <div class="subheading ma-3 py-4">
                    <h2>Bed {{bed}}</h2>
                    <wardVacant/>
                  </div>
                </v-card>
            </span>
          </v-flex>
        </v-layout>
    </app>
</template>

<script>
import wardBooked from "./wardBooked";
import wardVacant from "./wardVacant";

export default {
  components:{
      wardBooked,
      wardVacant,
  },
 props: ['booking','hospitals','hospiName']
}
</script>