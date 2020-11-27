import Vue from 'vue'
import blood_bank from './blood_bank.vue'
import vuetify from './plugins/vuetify';

import 'vuetify/dist/vuetify.min.css'



Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(blood_bank)
}).$mount('#app')

