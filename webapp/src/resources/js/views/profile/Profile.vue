<template>
    <Dashboard>
        <Card class="main-container">
            <template #content>
                <Card class="sub-container">
                <template #title>
                    <div class="flex justify-content-center align-items-center">
                        <Avatar class="avatar" icon="pi pi-user" :label="currentUser.nombre[0]+currentUser.apellido1[0]" size="xlarge" shape="circle" />
                    </div>
                </template>
                <template #content>
                    <div class="user p-grid p-fluid">
                        <div class="p-field p-col-12 p-md-6">
                            Username:
                            <span class="p-float-label">
                                <InputText class="disabledInput" id="email" type="text" v-model="currentUser.username" disabled/>
                            </span>
                        </div>
                        <div class="p-field p-col-12 p-md-6">
                            Nombre:
                            <span class="p-float-label">
                                <InputText class="disabledInput" id="email" type="text" v-model="nombre" disabled/>
                            </span>
                        </div>
                        <div class="p-field p-col-12 p-md-6">
                            Email:
                            <span class="p-float-label">
                                <InputText class="disabledInput" id="email" type="text" v-model="currentUser.email" disabled/>
                            </span>
                        </div>
                        <div class="p-field p-col-12 p-md-6">
                            Rol:
                            <span class="p-float-label">
                                <InputText class="disabledInput" id="email" type="text" v-model="currentRole.nombre" disabled/>
                            </span>
                    </div>
                    </div>
                    <div class="p-field p-col-12 p-md-6">
                        <br>
                        <strong>Permisos:</strong> 
                        <br>
                        <div class="flex justify-content-between m-2"><span class="permit">Digital Twin:</span> <TriStateCheckbox :class="digitalTwinComputed" v-model="digitalTwin" :disabled='true'/></div>
                        <div class="flex justify-content-between m-2"><span class="permit">Portal de Incidencias:</span> <TriStateCheckbox :class="incidenciasComputed" v-model="incidencias" :disabled='true' /></div>
                        <div class="flex justify-content-between m-2"><span class="permit">Portal de Administración:</span>  <TriStateCheckbox :class="adminPortalComputed" v-model="adminPortal" :disabled='true'/></div>
                    </div>
                </template>
                <template #footer>
                    <span class="p-buttonset p-col-12 p-md-4 center">
                        <Button class="p-button-danger p-button-outlined" @click="deleteUser($event, currentUser.id)" icon="pi pi-times" label="Delete profile" />
                        <Button @click="toEdit()" label="Edit" icon="pi pi-user-edit" iconpos="left" />
                    </span>
                </template>
                </Card>
            </template>
      </Card>
    </Dashboard>
</template>

<script>
    import { inject, toRefs } from "vue";
    import axios from "axios";

    export default {
        components: {
            
        },
        data() {
            // define view data
            return {
                currentUser: this.$store.state.currentUser,
                currentRole: this.$store.state.currentRole,
                token: this.$store.state.jwtToken,
                nombre: this.$store.state.currentUser.nombre + " " + this.$store.state.currentUser.apellido1 + " " + (this.$store.state.currentUser.apellido2 == null ? '' : this.$store.state.currentUser.apellido2),
                adminPortal: false,
                incidencias: false,
                digitalTwin: false,
            }
        },
        computed:{
            adminPortalComputed(){
                if(this.adminPortal){
                    return "okCheck";
                }
                return "nokCheck";
            },
            digitalTwinComputed(){
                if(this.digitalTwin){
                    return "okCheck";
                }
                return "nokCheck";
            },
            incidenciasComputed(){
                if(this.incidencias){
                    return "okCheck";
                }
                return "nokCheck";
            }
        },
        methods: {
            // delete your own user profile
            deleteUser(event, id) {
                this.$confirm.require({
                    target: event.currentTarget,
                    message: 'Do you want to delete your user profile?',
                    icon: 'pi pi-info-circle',
                    acceptClass: 'p-button-danger',
                    accept: () => {
                        var vm = this;

                        axios.delete(
                          "/api/user",{
                              headers: {
                                  'Content-Type': 'application/json',
                                  'Authorization': 'Bearer ' + vm.token
                              }
                            },
                            {
                             "id": id
                            }
                            ).then(function (response) {
                                if (response.data.success) {
                                    try {
                                        //Magically doesnt work
                                        vm.$gAuth.signOut();
                                        // clear all the data from the store, when deleting user profile
                                        vm.$store.dispatch('saveJwtToken', '');
                                        vm.$store.dispatch('saveCurrentUser', '');
                                        vm.$store.dispatch('saveCurrentRole', '');
                                        vm.$router.push('/landing');
                                    } catch (error) {
                                        console.error(error);
                                    }
                                }
                            })
                    },
                    reject: () => {
                    }
                });
            },
            toEdit() {
                this.$router.push('/user/edit');
            },
        },
        mounted(){
            let rol =this.$store.state.currentRole;
            if(rol.digitalTwin == 1 || rol.digitalTwin){
                this.digitalTwin = true;
            }
            if(rol.incidencias == 1 || rol.incidencias){
                this.incidencias = true;
            }
            if(rol.userDashboard == 1 || rol.userDashboard){
                this.adminPortal = true;
            }
        }
    }
</script>

<style scoped>
    .okCheck{
        opacity: 1!important;
        color:white;
        background: #00ff26;
    }
    .nokCheck{
        opacity: 1!important;
        color:white;
        background: #ff0024;
    }
        .avatar{
            width: 3em!important;
            height: 3em!important;
            font-size: 2em!important;
            background-color: #009affd4; 
            color: #ffffff
        }
    .disabledInput{
        opacity: 1!important;        
    }
    .main-container{
        display:flex;
        justify-content: center;
        align-items: center;
        height:100%;
    }
    .sub-container{
        background: white;
        color: black;
        display:flex;
        justify-content: center;
        height:100%;
        width: fit-content;
        padding: 1.5em 3.5em;
    }
    .activityhistorybtn {
        margin-top: 10px;
        background: lightgray;
        border: none;
        color: black;
    }

        .activityhistorybtn:hover {
            background: gray !important;
            border: none;
            color: black;
        }

    .profile-pic {
        margin-bottom: 3%;
    }    
</style>