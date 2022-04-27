import { createApp } from 'vue';
import App from './App.vue';
import router from './route.js';
import store from './store.js';
//import gAuthPlugin from 'vue3-google-oauth2';
import DataView from "primevue/dataview";
import Card from 'primevue/card';
import Dropdown from 'primevue/dropdown';
import Sidebar from 'primevue/sidebar';
import Fieldset from 'primevue/fieldset';
import PrimeVue from 'primevue/config';
import InputText from 'primevue/inputtext';
import Panel from "primevue/panel";
import Chart from 'primevue/chart';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup'; 
import Row from 'primevue/row';  
import MultiSelect from 'primevue/multiselect';
import Textarea from 'primevue/textarea';
import ConfirmationService from 'primevue/confirmationservice';
import ConfirmPopup from 'primevue/confirmpopup';
import TabMenu from 'primevue/tabmenu';

import 'primevue/resources/themes/bootstrap4-light-blue/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';
import 'primeflex/primeflex.css';
//let gauthClientId = "825285713961-v7u7q28eh85pqci1neence8c2okd5ke3.apps.googleusercontent.com";
createApp(App)
    .use(PrimeVue)
    .use(store)
    .use(ConfirmationService)
    //.use(gAuthPlugin, { clientId: gauthClientId, scope: 'profile email', prompt: 'select_account', fetch_basic_profile: true })
    .use(router)
    .component("DataView", DataView)
    .component("Card", Card)
    .component('DataTable', DataTable)
    .component('Sidebar', Sidebar)
    .component('Column', Column)
    .component('Row', Row)
    .component('ColumnGroup', ColumnGroup)
    .component('Fieldset', Fieldset)
    .component('Button', Button)
    .component('InputText', InputText)
    .component('Dropdown', Dropdown)
    .component('Panel', Panel)
    .component('Chart', Chart)
    .component('Dropdown', Dropdown)
    .component('Dialog', Dialog)
    .component('MultiSelect', MultiSelect)
    .component('Textarea', Textarea)
    .component('ConfirmPopup', ConfirmPopup)
    .component('TabMenu', TabMenu)
    .mount('#app');
//# sourceMappingURL=main.js.map

require("./bootstrap");

