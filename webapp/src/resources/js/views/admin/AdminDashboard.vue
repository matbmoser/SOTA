<template>
<Dashboard>
  <ListaUsuarios header="Admin Usuarios" v-if="renderComponent" :edit="true" :Usuarios="usuarios" :roles="roles"/>
  <LoadingToast position="center"  group='load'/>
  <ErrorToast position="center" group='err'/>
</Dashboard>
</template>
<script>
    import ErrorToast from "../../components/toasts/ErrorToast.vue";
    import LoadingToast from "../../components/toasts/LoadingToast.vue";
    import {ToastSeverity} from 'primevue/api';
    import ListaUsuarios from "../../components/ListaUsuarios.vue";
    import axios from "axios";
    export default {
        data() {
            return {
                loading: false,
                usuarios: [],
                roles: [],
                renderComponent: true
            }
        },
        methods: {
            fetchRoles(){
                 var self = this;
                axios
                    .get('/api/roles',{
                        headers: {
                            Authorization: 'Bearer ' + this.$store.state.jwtToken,
                        }
                    })
                    .then(response => {
                        this.loading = false;
                        this.$toast.removeAllGroups();
                        this.roles = response.data.roles;
                        let i = 0;
                        this.dir = {}
                        while(i < this.roles.length){
                            this.dir[this.roles[i]["id"]]=this.roles[i]["nombre"];
                            i++;
                        }
                        console.log(this.dir)
                        let j = 0;
                        let lenUsr = this.usuarios.length;
                        while(j < lenUsr){
                            this.usuarios[j]["rol"] = this.dir[this.usuarios[j]["idRol"]]
                            console.log(this.usuarios[j]["rol"])
                            j++;
                        }
                        
                    }).catch(error =>{
                        this.$toast.removeAllGroups();
                        self.displayToastMessage(ToastSeverity.ERROR, "¡No ha sido posible recoger los roles!", "Intente otra vez más tarde...");
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
                    .get('/api/users', {
                        headers: {
                            Authorization: 'Bearer ' + this.$store.state.jwtToken,
                        }
                    })
                    .then(response => {
                        this.loading = false;
                        this.$toast.removeAllGroups();
                        this.usuarios = response.data.users;

                    }).catch(error =>{
                        this.$toast.removeAllGroups();
                        self.displayErrorMessage();
                    });
            },
            displayErrorMessage() {
                this.loading = false;
                this.$toast.add({severity:ToastSeverity.INFO, summary: '¡Todavía no existen usuarios!', group:'err', detail: "Espera que se produzcan en el parking... <i class='pi pi-exclamation-triangle' style='font-size:1em'></i>"});
            },
            startLoading() {
                this.loading = true;
                this.$toast.add({severity:ToastSeverity.SUCCESS, summary:"Espere por favor...", group:'load', detail: "<h3>Cargando usuarios...</h3>"});
            },
        },
        mounted() {
            this.startLoading();
            this.fetchAll();
            this.fetchRoles();
        },
        components:{
            "ListaUsuarios":ListaUsuarios,
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

