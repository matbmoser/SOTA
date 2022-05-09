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
                    <form autocomplete="off">
                    <div class="user p-grid p-fluid">
                        <div class="p-field p-col-12 p-md-6">
                            Username:
                            <span class="p-float-label">
                                <InputText class="disabledInput" id="email" type="text" v-model="currentUser.username"/>
                            </span>
                        </div>
                        <div class="p-field p-col-12 p-md-6">
                            Nombre:
                            <span class="p-float-label">
                                <InputText class="disabledInput" id="email" type="text" v-model="currentUser.nombre"/>
                            </span>
                        </div>
                        <div class="p-field p-col-12 p-md-6">
                            Email:
                            <span class="p-float-label">
                                <InputText class="disabledInput" id="email" type="text" v-model="currentUser.email"/>
                            </span>
                        </div>
                    <div class="p-field p-col-12 p-md-6">
                        Contraseña:
                            <Password v-model="password" :feedback="false" id="password" />
                    </div>
                    <div class="p-field p-col-12 p-md-6">
                        Confirmar Contraseña:
                        <Password v-model="confirmpassword" :feedback="false" id="confirmpassword"/>
                        </div>
                    </div>
                    </form>
                </template>
                <template #footer>
                    <span class="p-buttonset p-col-12 p-md-4 center">
                       <span class="p-buttonset p-col-12 p-md-4 center">
                        <Button class="p-button-outlined" @click="toUser()" label="Back" icon="pi pi-arrow-left" iconpos="left" />
                        <Button @click="saveUser()" :label="labelComputed" :icon="iconComputed" iconPos="left" />
                    </span>
                    </span>
                </template>
                </Card>
            </template>
        </Card>
        <LoadingToast position="center"  group='load'/>
        <ErrorToast position="center" group='err'/>
    </Dashboard>
</template>

<script>
    import ErrorToast from "../../components/toasts/ErrorToast.vue";
    import {ToastSeverity} from 'primevue/api';
    import axios from "axios";
    export default {
        data() {
            // define view data
            return {
                currentUser: this.$store.state.currentUser,
                token: this.$store.state.jwtToken,
                password: "",
                confirmpassword: "",
                loading: false
            }
        },
        computed:{
            labelComputed(){
                let label = ''

                if (this.loading) label = 'Actualizando Perfil...'
                else label = 'Actualizar Perfil'

                return label
            },
            iconComputed(){
                let icon = 'pi pi-save'

                if (this.loading) icon = 'pi pi-spin pi-spinner'
                else icon = 'pi pi-save'

                return icon
            }
        },
        components:{
            "ErrorToast":ErrorToast
        },
        methods: {
            displayToastMessage(severity, summary, message) {
                this.loading = false;
                this.$toast.add({severity:severity, summary: summary, group:'err', detail: message});
            },
            displayErrorMessage(error) {
                this.loading = false;
                this.$toast.add({severity:ToastSeverity.ERROR, summary: 'Register Failed!', detail: error, group:'err', life: 5000});
            },
            saveUser(){
            this.loading=true;
            var self = this;
             var packet = {
                    "id": this.currentUser.id,
                    "nombre": this.currentUser.nombre,
                    "username": this.currentUser.username,
                    "email": this.currentUser.email,
                    "password": this.password,
                    "password_confirmation": this.confirmpassword,
            }
            axios
            .patch("/api/user/"+this.currentUser.id,packet,{
                headers:{
                    "Authorization": "Bearer " + this.token
                }
            })
            .then(function (response) {
                self.loading=false;
                self.$store.dispatch('saveCurrentUser', response.data.user);
                self.$store.dispatch('saveJwtToken', response.headers.authorization);
                self.displayToastMessage(ToastSeverity.SUCCESS, "Perfil Actualizado!", "El perfil se encuentra actualizado...");
                location.reload();
            }).catch(error =>{
                self.displayToastMessage(ToastSeverity.ERROR, "¡Fallo al añadir Incidencia!", "Intente enviar otra vez... Error: ["+error+"]");
                this.loading = false;
                if(error.response.data.message!=null){
                    self.displayErrorMessage(error.response.data.message);
                }
                else{
                    if(error.response.data.errors != ''){
                        let content = error.response.data.errors;
                        let i = 0;
                        let contentArray = Object.keys(content);
                        let err = "";
                        while(i < contentArray.length){
                            err += '<strong>'+contentArray[i]+'</strong> '+content[contentArray[i]] +'<br>'
                            i++;
                        }
                        self.displayErrorMessage(err);
                    }else{
                    self.displayErrorMessage(error.response.data);
                    }
                }
            });
            },
            toUser() {
                this.$router.push('/profile');
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