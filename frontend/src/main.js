import Vue from 'vue';
import Vuex from 'vuex';
import App from './App.vue';
import router from './router';
import store from './store';
import VueClipboard from 'vue-clipboard2'
 
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap-vue/dist/bootstrap-vue.css';

// 다이얼로그
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

// 토글버튼
import ToggleButton from 'vue-js-toggle-button';

// 메인페이지 range-slider
// https://www.vuescript.com/custom-slider-control-vuejs/
import VueSlider from 'vue-slider-component';
import 'vue-slider-component/theme/default.css';

Vue.use(VueClipboard)
VueClipboard.config.autoSetContainer = true
Vue.config.productionTip = false;
Vue.use(Vuex);
Vue.use(BootstrapVue);
Vue.use(VueSweetalert2);
Vue.use(ToggleButton);
Vue.component('VueSlider', VueSlider);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
