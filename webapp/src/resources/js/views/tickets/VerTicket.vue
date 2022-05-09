<template>
<div class="flex h-100 justify-content-center align-items-center">
    <router-link to="/tickets"><Button style="position:fixed; bottom: 10px; left:10px;" icon="pi pi-arrow-left" /></router-link>
        <Card class="sub-container">
        <template #title>
            <div class="flex justify-content-left align-items-top w-full h-full">
                <Avatar class="avatar w-full h-full" :label="ticket.idPlaza" size="xlarge" shape="square" />
            </div>
        </template>
        <template #content>
            <div class="user p-grid p-fluid">
                <div class="p-field p-col-12 p-md-6">
                    Matricula:
                    <span class="p-float-label">
                        <InputText class="disabledInput" id="email" type="text" v-model="ticket.matricula" disabled/>
                    </span>
                </div>
                <div class="p-field p-col-12 p-md-6">
                    Hora de entrada:
                    <span class="p-float-label">
                        <InputText class="disabledInput" id="email" type="text" v-model="ticket.entrada" disabled/>
                    </span>
                </div>
                <div class="p-field p-col-12 p-md-6">
                    Hora de salida:
                    <span class="p-float-label">
                        <InputText class="disabledInput" id="email" type="text" v-model="ticket.salida" disabled/>
                    </span>
                </div>
                <div class="p-field p-col-12 p-md-6">
                    Validez:
                    <span class="p-float-label">
                        <Button :class="(ticket.valido==true ? 'p-button-success p-button-filled' : 'p-button-danger p-button-filled')" :label="(ticket.valido==true ? 'VALIDO' : 'NOVALIDO')" id="email" type="text"/>
                    </span>
            </div>
            </div>
            <div class="p-field p-col-12 p-md-6 mt-5">
                <QRCode
                    :style="getStyle"
                    :text="getPath"
                    size="250">
                </QRCode>
            </div>
        </template>
        <template #footer>
            <span class="p-buttonset p-col-12 p-md-4 center">
                <Button class="w-full p-button-danger p-button-filled" @click="addIncidencia()" :style="getStyle" icon="pi pi-exclamation-triangle" label="Abrir Incidencia" />
            </span>
        </template>
        </Card>
        <LoadingToast position="center"  group='load'/>
        <ErrorToast position="center" group='err'/>
            <!-- Dialog -->
        <Dialog header="Añadir Incidencia"
                v-model:visible="dialogDisplay"
                 :breakpoints="{'960px': '75vw'}" :style="{width: '30vw'}" :modal="true">
                <form autocomplete="off">
                <div class="p-fluid">
                    <div class="p-field" style="margin-top: 30px">
                        <span class="p-float-label">
                            <InputText id="activityNameInputText" type="text" v-model="titulo" required/>
                            <label>Titulo</label>
                        </span>
                    </div>
                    <div class="p-field" style="margin-top: 30px">
                        <span class="p-float-label">
                            <Textarea v-model="descripcion" rows="5" cols="30" required/>
                            <label>Descripción</label>
                        </span>
                    </div>
                    <div class="p-field" style="margin-top: 30px">
                        <label>Gravedad</label>
                        <Rating v-model="gravedad" :stars="5" :cancel="false" required/>
                    </div>
                    <div class="p-field" style="margin-top: 30px">
                        <span class="p-float-label">
                            <FileUpload name="demo[]" url="./upload.php" v-model="imagen" @upload="onUpload" :fileLimit="1" :multiple="false" accept="image/*" :maxFileSize="1000000" required>
                                <template #empty>
                                    <p>Sube la foto de la incidencia aqui</p>
                                </template>
                            </FileUpload>
                            <label>Foto Incidencia</label>
                        </span>
                    </div>
                </div>
                </form>
                <template #footer>
                    <div class="flex justify-content-center">
                    <Button type="submit"
                            class="p-buttom-primary"
                            :icon="iconComputed" 
                            :label="labelComputed" 
                            @click="SaveIncidencia()">
                    </Button>
                    </div>
                </template>
          </Dialog>
        </div>
</template>

<script>
    import Rating from 'primevue/rating';
    import { inject, toRefs } from "vue";
    import VueQRCodeComponent from 'vue-qrcode-component'
    import ErrorToast from "../../components/toasts/ErrorToast.vue";
    import LoadingToast from "../../components/toasts/LoadingToast.vue";
    import {ToastSeverity} from 'primevue/api';
    import axios from "axios";

    export default {
        props: ['token'],
        components:{
            "ErrorToast": ErrorToast,
            "LoadingToast": LoadingToast,
            "QRCode":VueQRCodeComponent,
            "Rating":Rating
        },
        data() {
            // define view data
            return {
                ticket:{},
                loading:false,
                exists: false,
                dialogDisplay: false,
                gravedad: 0,
                titulo:"",
                descripcion:"",
                imagen:""
            }
        },
        computed:{
            getPath(){
                    return window.location.href
            },
            getStyle(){
                if(!this.loading && this.exists){
                    return "display:block!important"
                }
                return "display:none!important"
            },
            labelComputed(){
                let label = ''

                if (this.loading) label = 'Enviando Incidencia...'
                else label = 'Enviar Incidencia'

                return label
            },
            iconComputed(){
                let icon = 'pi pi-check'

                if (this.loading) icon = 'pi pi-spin pi-spinner'
                else icon = 'pi pi-check'

                return icon
            }
        },
        methods:{
            addIncidencia(){
            this.jwtToken = this.$store.state.jwtToken;
            if(this.jwtToken == null || this.jwtToken == ""){
                this.displayToastMessage(ToastSeverity.ERROR, "¡Operación invalida!", "Debes estar logueado para añadir incidencias...");
                return;
            }
            if(!this.exists){
                this.displayToastMessage(ToastSeverity.ERROR, "¡Operación invalida!", "El ticket tiene que existir...");
                return;
            }
            this.dialogDisplay = true;
            },
            startLoading() {
                this.loading = true;
                this.$toast.add({severity:ToastSeverity.SUCCESS, summary:"Espere por favor...", group:'load', detail: "<h3>Comprobando validez...</h3>"});
            },
            displayToastMessage(severity, summary, message) {
                this.loading = false;
                this.$toast.add({severity:severity, summary: summary, group:'err', detail: message});
            },
            loadTicket(){
                axios
                    .get('/api/ticket/'+this.token)
                    .then(response => {
                        this.loading = false;
                        this.$toast.removeAllGroups();
                        this.exists=true;
                        this.ticket = response.data.ticket;
                    }).catch(error =>{
                        this.$toast.removeAllGroups();
                        this.displayToastMessage(ToastSeverity.ERROR, "No ha sido posible encontrar el ticket", "Está caducado o no existe....");
                    });
            },
            SaveIncidencia() {
                this.jwtToken = this.$store.state.jwtToken;
                if(this.jwtToken == null || this.jwtToken == ""){
                    this.displayToastMessage(ToastSeverity.ERROR, "¡Operación invalida!", "Debes estar logueado para añadir incidencias...");
                    return;
                }
                if(!this.exists){
                    this.displayToastMessage(ToastSeverity.ERROR, "¡Operación invalida!", "El ticket tiene que existir...");
                    return;
                }
                axios.put('/api/incidencia', {
                        "token": this.token,
                        "gravedad":this.gravedad,
                        "titulo": this.titulo,
                        "descripcion": this.descripcion,
                        "nombreArchivoFoto":this.foto
                    },{
                        header:{
                            "Authorization": "Bearer " +  this.jwtToken
                        }
                    }
                    )
                    .then(response => {
                        this.dialogDisplay = false;
                        this.displayToastMessage(ToastSeverity.SUCCESS, "Incidencia Añadida!", "La incidencia ha sido añadido en tu perfil...");
                        location.reload();
                        
                    }).catch(error =>{
                         if(error.response.data.message!=null){
                             self.displayToastMessage(ToastSeverity.ERROR, "¡Fallo al añadir Incidencia!", "Intente enviar otra vez... Error: ["+error.response.data.message+"]");
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
                                self.displayToastMessage(ToastSeverity.ERROR, "¡Fallo al añadir Incidencia!", "Intente enviar otra vez... Error: ["+err+"]");
                            }else{
                                self.displayToastMessage(ToastSeverity.ERROR, "¡Fallo al añadir Incidencia!", "Intente enviar otra vez...");
                            }
                        }
                      
                    });
            }
        },
        mounted() {
            this.loadTicket();
            this.startLoading();
        }
    }
</script>

<style scoped>

        .avatar{

                position: relative;
                /* position: sticky; */
                top: -38px;
                left: -67px;
                width: 200px!important;
                height: 200px!important;
                font-size: 5em!important;
                background-color: #00f3ffd4;
                border-radius: 0!important;
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