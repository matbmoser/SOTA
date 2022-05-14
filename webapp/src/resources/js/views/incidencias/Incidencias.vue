<template>
<Dashboard>
  <ListaIncidencias header="Mis Incidencias" v-if="renderComponent" :edit="false" :Incidencias="incidencias"/>
  <LoadingToast position="center"  group='load'/>
  <ErrorToast position="center" group='err'/>
</Dashboard>
</template>
<script>
    import ErrorToast from "../../components/toasts/ErrorToast.vue";
    import LoadingToast from "../../components/toasts/LoadingToast.vue";
    import {ToastSeverity} from 'primevue/api';
    import ListaIncidencias from "../../components/ListaIncidencias.vue";
    import axios from "axios";
    export default {
        data() {
            return {
                loading: false,
                incidencias: [],
                renderComponent: true
            }
        },
        methods: {
            
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
                    .get('/api/incidencias/user/'+this.$store.state.currentUser.id, {
                        headers: {
                            Authorization: 'Bearer ' + this.$store.state.jwtToken,
                        }
                    })
                    .then(response => {
                        this.loading = false;
                        this.$toast.removeAllGroups();
                        this.incidencias = response.data.incidencias;

                    }).catch(error =>{
                        this.$toast.removeAllGroups();
                        self.displayErrorMessage();
                    });
            },
            displayErrorMessage() {
                this.loading = false;
                this.$toast.add({severity:ToastSeverity.INFO, summary: '¡Todavía no tienes Incidencias!', group:'err', detail: "Puedes abrirlas en los tickets, haciendo click en abrir incidencia <i class='pi pi-exclamation-triangle' style='font-size:1em'></i>"});
            },
            startLoading() {
                this.loading = true;
                this.$toast.add({severity:ToastSeverity.SUCCESS, summary:"Espere por favor...", group:'load', detail: "<h3>Cargando incidencias...</h3>"});
            },
        },
        mounted() {
            this.startLoading();
            this.fetchAll();
        },
        components:{
            "ListaIncidencias":ListaIncidencias,
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

