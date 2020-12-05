<template>
    <app>
        <div class="text-center">
            <v-dialog
            v-model="dialog"
            width="400"
            >
            <template v-slot:activator="{ on, attrs }">
                <v-btn
                color="blue-grey darken-2"
                dark
                v-bind="attrs"
                v-on="on"
                >
                VACANT
                </v-btn>
            </template>

            <v-card>
                <v-card-title class="headline grey lighten-2">
                Register Here
                </v-card-title>

                <div class="ma-3 py-4">
                    <bookingForm/>
                </div>

                <v-divider></v-divider>

                <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    color="primary"
                    text
                    @click="dialog = false"
                >
                    Close
                </v-btn>
                </v-card-actions>
            </v-card>
            </v-dialog>
        </div>
    </app>
</template>


<script>
import bookingForm from "./bookingForm";
  export default {
    data () {
      return {
        dialog: false,
      }
    },
    components:{
        bookingForm,
    }
  }
</script>