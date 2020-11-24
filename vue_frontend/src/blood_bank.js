import Vue from 'vue'
import blood_bank from './blood_bank.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(blood_bank),
}).$mount('#app')
