import Vue from 'vue'
import bed_management from './bed_management.vue'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(bed_management)
}).$mount('#app')
