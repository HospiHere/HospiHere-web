<template>
    <app>
        <div class="text-center">
            <v-dialog
            v-model="dialog"
            width="500"
            >
            <template v-slot:activator="{ on, attrs }">
                <v-btn
                color="light-green darken-4"
                dark
                v-bind="attrs"
                v-on="on"
                >
                Booked
                </v-btn>
            </template>

            <v-card>
                <v-card-title class="headline grey lighten-2">
                Patient Information
                </v-card-title>
                <v-card-text></v-card-text>
                
                <v-card-text>
                    Name : {{name}}
                </v-card-text>
                <v-card-text>
                    Mobile Number : {{mobile}}
                </v-card-text>
                <v-card-text>
                    Address : {{address}}
                </v-card-text>
                <v-card-text>
                    Disease : {{disease}}
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    color="primary"
                    text
                    @click="dialog = false"
                >
                    OK
                </v-btn>
                </v-card-actions>
            </v-card>
            </v-dialog>
        </div>
    </app>
</template>


<script>
  export default {
    data () {
      return {
        dialog: false,
      }
    },
    props: ['name','mobile','disease', 'address']
  }
</script>
