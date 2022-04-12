import { createApp } from 'vue';
import App from './App.vue';
import PrimeVue from 'primevue/config';
import Dialog from 'primevue/dialog';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Panel from "primevue/panel";
import Toast from 'primevue/toast';
import Router from './route.js'

import Dropdown from 'primevue/dropdown';

import ToastService from 'primevue/toastservice';

import 'primevue/resources/themes/saga-blue/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';
import 'primeflex/primeflex.css';

const app = createApp(App)
        .use(Router)
        .use(PrimeVue)
        .use(ToastService)
        .component('Dialog', Dialog)
        .component('Panel', Panel)
        .component('Dropdown', Dropdown)
        .component('Button', Button)
        .component('Toast', Toast)
        .component('InputText', InputText)
        .mount("#app");

require("./bootstrap");
