<template>
<Dashboard>
  <ListaVehiculos header="Mis Vehiculos" v-if="renderComponent" :Vehiculos="vehiculos" :TipoVehiculos="tipovehiculos"/>
  <LoadingToast position="center"  group='load'/>
  <ErrorToast position="center" group='err'/>
</Dashboard>
</template>
<script>
    import ErrorToast from "../../components/toasts/ErrorToast.vue";
    import LoadingToast from "../../components/toasts/LoadingToast.vue";
    import {ToastSeverity} from 'primevue/api';
    import ListaVehiculos from "../../components/ListaVehiculos.vue";
    import axios from "axios";
    export default {
        data() {
            return {
                loading: false,
                vehiculos: [],
                tipovehiculos: [],
                renderComponent: true
            }
        },
        methods: {
            fetchTipoVehiculos(){
                 var self = this;
                axios
                    .get('/api/vehiculos/tipos',{
                        headers: {
                            Authorization: 'Bearer ' + this.$store.state.jwtToken,
                        }
                    })
                    .then(response => {
                        this.loading = false;
                        this.$toast.removeAllGroups();
                            let i = 0;
                            let tipos = [];
                            let data = response.data.tipoVehiculos;
                            while(i < data.length){
                                let ve = data[i];
                                let tipo = {};
                                tipo["id"] = ve["id"];
                                tipo["tipo"] = "Segmento ["+ve["segmento"]+"] - "+ve["clasificacion"].charAt(0).toUpperCase() + ve["clasificacion"].slice(1);
                                tipos.push(tipo);
                                i++;
                            }
                            this.tipovehiculos = tipos;
                    }).catch(error =>{
                        this.$toast.removeAllGroups();
                        self.displayToastMessage(ToastSeverity.ERROR, "No ha sido posible recoger el tipo de vehiculo!", "Intente otra vez más tarde...");
                    });
            },
            displayToastMessage(severity, summary, message) {
                this.loading = false;
                this.$toast.add({severity:severity, summary: summary, group:'err', detail: message});
            },
            /**
             * Updates the number of users with the lenght of a JSON list of all users from the back-end.
             * After this function is called use the forceUpdate() function to update the table.
             * uses API endpoint GET /api/user/
             *
             * @see forceUpdate()
             */
            fetchAll() {
                var self = this;
                axios
                    .get('/api/vehiculos/user/'+this.$store.state.currentUser.id, {
                        headers: {
                            Authorization: 'Bearer ' + this.$store.state.jwtToken,
                        }
                    })
                    .then(response => {
                        this.loading = false;
                        this.$toast.removeAllGroups();
                        this.vehiculos = response.data.vehiculos;
                    }).catch(error =>{
                        this.$toast.removeAllGroups();
                        self.displayErrorMessage();
                    });
            },
            displayErrorMessage() {
                this.loading = false;
                this.$toast.add({severity:ToastSeverity.INFO, summary: '¡Todavía no tienes vehículos!', group:'err', detail: "Puedes añadirlos aquí, haciendo click en el botón <i class='pi pi-plus' style='font-size:1em'></i>"});
            },
            startLoading() {
                this.loading = true;
                this.$toast.add({severity:ToastSeverity.SUCCESS, summary:"Espere por favor...", group:'load', detail: "<h3>Cargando vehiculos...</h3>"});
            },
        },
        mounted() {
            this.fetchTipoVehiculos();
            this.startLoading();
            this.fetchAll();
        },
        components:{
            "ListaVehiculos":ListaVehiculos,
            "ErrorToast": ErrorToast,
            "LoadingToast": LoadingToast
        }
    }
</script>

<style scoped>
    .p-panel {
        box-shadow: 0 .5rem 1rem rgba(0,0,0,.15) !important;
        margin: 50px 0px;
    }

    .p-panel .p-panel-header {
        border: 1px solid #f7f7f7;
        padding: 1rem 1.25rem;
        background: #f7f7f7;
        color: #212529;
        border-top-right-radius: 4px;
        border-top-left-radius: 4px;
    }

    table {
        font-family: 'Open Sans', sans-serif;
        width: 750px;
        border-collapse: collapse;
        margin: 10px 10px 0 10px;
    }

    .t.row {
        margin: 0 !important;
    }

    table .p-datatable-thead tr th {
        text-transform: uppercase !important;
        text-align: left !important;
        background: #5600ff !important;
        color: #FFF !important;
    }

    table td:last-child {
        border-right: none;
    }

    table tbody tr:nth-child(2n) td {
        background: #e4d6ff;
    }
</style>

