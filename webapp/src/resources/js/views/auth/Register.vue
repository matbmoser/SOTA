<template>
    <div id="mainContainer" class="gradient-custom flex align-items-center justify-content-center">
            <div class="form-demo">
                <div class="main-card justify-content-center">
                    <div class="card">
                        <div class="text-center mb-5">
                            <img src="../..//media/img/logowhite.png" alt="Image" class="loginlogo mb-3">
                            <div class="text-900 text-3xl font-medium mb-3 loginTitle">UFV MyParking</div>
                        </div>
                        <form @submit.prevent="handleSubmit(!v$.$invalid)" class="p-fluid" autocomplete="off">
                                                        <div class="field grid formgrid">
                                <div class="col-12 mb-2 lg:col-6 lg:mb-0">
                                    <div class="p-float-label p-input-icon-right">
                                        <i class="pi pi-envelope" />
                                        <InputText @keydown.space.prevent id="email" v-model="v$.email.$model" :class="{'p-invalid':v$.email.$invalid && submitted}" aria-describedby="email-error"/>
                                        <label for="email" :class="{'p-error':v$.email.$invalid && submitted}">Email*</label>
                                    </div>
                                    <span v-if="v$.email.$error && submitted">
                                        <span id="email-error" v-for="(error, index) of v$.email.$errors" :key="index">
                                        <small class="p-error">{{error.$message}}</small>
                                        </span>
                                    </span>
                                    <small v-else-if="(v$.email.$invalid && submitted) || v$.email.$pending.$response" class="p-error">{{v$.email.required.$message.replace('Value', 'Email')}}</small>
                                </div>
                                <div class="col-12 mb-2 lg:col-6 lg:mb-0">
                                    <div class="p-float-label">
                                        <Calendar id="fechaNacimiento" v-model="v$.fechaNacimiento.$model" :class="{'p-invalid':v$.fechaNacimiento.$invalid && submitted}" toggleMask :showIcon="true" />
                                        <label for="fechaNacimiento">Fecha de Nacimiento</label>
                                    </div>
                                    <small v-if="(v$.fechaNacimiento.$invalid && submitted) || v$.fechaNacimiento.$pending.$response" class="p-error">{{v$.fechaNacimiento.required.$message.replace('Value', 'Fecha de Nacimiento')}}</small>
                                </div>
                            </div>
                            <div class="field grid formgrid mt-4">
                                <div class="col-12 mb-2 lg:col-6 lg:mb-0">
                                    <div class="p-float-label">
                                    <Password id="password" v-model="v$.password.$model" :class="{'p-invalid':v$.password.$invalid && submitted}" toggleMask>
                                        <template #header>
                                            <h6>Elige una contraseña</h6>
                                        </template>
                                        <template #footer="sp">
                                            {{sp.level}}
                                            <Divider />
                                            <p class="mt-2">Consejos</p>
                                            <ul class="pl-2 ml-2 mt-0" style="line-height: 1.5">
                                                <li>Al menos un caracter en minuscula</li>
                                                <li>Al menos un caracter en mayuscula</li>
                                                <li>Al menos un caracter numerico</li>
                                                <li>Como mínimo 8 caracteres</li>
                                            </ul>
                                        </template>
                                    </Password>
                                    <label for="password" :class="{'p-error':v$.password.$invalid && submitted}">Password*</label>
                                    </div>
                                    <small v-if="(v$.password.$invalid && submitted) || v$.password.$pending.$response" class="p-error">{{v$.password.required.$message.replace('Value', 'Password')}}</small>
                                </div>
                            <div class="col-12 mb-2 lg:col-6 lg:mb-0" >
                                <div class="p-float-label">
                                    <Password id="confirmar" v-model="v$.confirmar.$model" :feedback="false" :class="{'p-invalid':v$.confirmar.$invalid && submitted}" toggleMask>
                                    </Password>
                                    <label for="confirmar" :class="{'p-error':v$.confirmar.$invalid && submitted}">Confirmar Password</label>
                                </div>
                                <small v-if="(v$.confirmar.$invalid && submitted) || v$.confirmar.$pending.$response" class="p-error">{{v$.confirmar.required.$message.replace('Value', 'Confirmar Password')}}</small>
                            </div>
                            </div>
                            <div class="field grid formgrid mt-4">
                                <div class="col-12 mb-2 lg:col-6 lg:mb-0">
                                    <div class="p-float-label">
                                        <InputText id="nombre" v-model="v$.nombre.$model" :class="{'p-invalid':v$.nombre.$invalid && submitted}" />
                                        <label for="nombre" :class="{'p-error':v$.nombre.$invalid && submitted}">Nombre*</label>
                                    </div>
                                    <small v-if="(v$.nombre.$invalid && submitted) || v$.nombre.$pending.$response" class="p-error">{{v$.nombre.required.$message.replace('Value', 'Nombre')}}</small>
                                </div>
                                <div class="col-12 mb-2 lg:col-6 lg:mb-0">
                                    <div class="p-float-label">
                                        <InputText id="apellido1" v-model="v$.apellido1.$model" :class="{'p-invalid':v$.apellido1.$invalid && submitted}" />
                                        <label for="apellido1" :class="{'p-error':v$.apellido1.$invalid && submitted}">Apellido 1*</label>
                                    </div>
                                    <small v-if="(v$.apellido1.$invalid && submitted) || v$.apellido1.$pending.$response" class="p-error">{{v$.apellido1.required.$message.replace('Value', 'Apellido1')}}</small>
                                </div>
                            </div>
                            <div class="field grid formgrid mt-4">
                                <div class="col-12 mb-2 lg:col-6 lg:mb-0">
                                    <div class="p-float-label">
                                        <InputText id="apellido2" v-model="apellido2" />
                                        <label for="apellido2">Apellido 2</label>
                                    </div>
                                </div>
                                <div class="col-12 mb-2 lg:col-6 lg:mb-0">
                                    <div class="p-float-label p-input-icon-left">
                                            <i class="pi pi-user" />
                                            <InputText id="username" @keydown.space.prevent v-model="v$.username.$model" :class="{'p-invalid':v$.username.$invalid && submitted}" />
                                            <label for="username" :class="{'p-error':v$.username.$invalid && submitted}">Username*</label>
                                    </div>
                                <small v-if="(v$.username.$invalid && submitted) || v$.username.$pending.$response" class="p-error">{{v$.username.required.$message.replace('Value', 'Username')}}</small>
                                </div>
                            </div>
                            <div class="field grid formgrid mt-4">
                                <div class="col-12 mb-2 lg:col-6 lg:mb-0">
                                    <div class="p-float-label">
                                        <InputText id="documento" v-model="v$.documento.$model" :class="{'p-invalid':v$.documento.$invalid && submitted}" />
                                        <label for="documento" :class="{'p-error':v$.documento.$invalid && submitted}">DNI/NIE/Pasaporte*</label>
                                    </div>
                                      <small v-if="(v$.documento.$invalid && submitted) || v$.documento.$pending.$response" class="p-error">{{v$.documento.required.$message.replace('Value', 'Documento')}}</small>
                                </div>
                                <div class="col-12 mb-2 lg:col-6 lg:mb-0">
                                    <div class="p-float-label">
                                        <InputText id="telefono" :class="{'p-invalid':v$.telefono.$invalid && submitted}" v-model="v$.telefono.$model"/>
                                        <label for="telefono" :class="{'p-error':v$.telefono.$invalid && submitted}" >Teléfono*</label>
                                    </div>
                                     <small v-if="(v$.telefono.$invalid && submitted) || v$.telefono.$pending.$response" class="p-error">{{v$.telefono.required.$message.replace('Value', 'Teléfono')}}</small>
                                </div>
                            </div>
                            <div class="field-checkbox grid formgrid mt-4">
                                <div class="col-12 mb-2 lg:col-12 lg:mb-0">
                                    <Checkbox id="accept" name="accept" value="Accept" v-model="v$.accept.$model" :class="{'p-invalid':v$.accept.$invalid && submitted}" />
                                    <label for="accept" :class="{'p-error': v$.accept.$invalid && submitted}"> Acepto la <a icon="pi pi-external-link" @click="openPrivacyModal">política de privacidad</a></label>
                                </div>
                            </div>
                            <Button type="submit" :icon="iconComputed" :label="labelComputed" class="mt-2 submitButton" />
                    
                        </form>
                <p class="mt-3">¿Ya estás registrado? <router-link to="/login"><a>Log in</a></router-link></p>
            </div>
            <Dialog header="Política de Privacidad" v-model:visible="privacyModal" :breakpoints="{'960px': '75vw'}" :style="{width: '50vw'}" :modal="true">
                <p>
                    <Privacidad/>
                </p>
                <template #footer>
                    <Button label="Acepto" icon="pi pi-check" @click="closePrivacyModal" autofocus />
                </template>
            </Dialog>
            <ErrorToast position="top-center"/>
        </div>
    </div>
</div>
        
</template>

<script>
import { email, required, minLength } from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import Privacidad from "../../components/Privacidad.vue";
import {ToastSeverity} from 'primevue/api';
import ErrorToast from "../../components/toasts/ErrorToast.vue";
import axios from "axios";
export default {
    setup: () => ({ v$: useVuelidate() }),
    data() {
        return {
            nombre: '',
            apellido1: '',
            apellido2: '',
            username: '',
            email: '',
            password: '',
            telefono: '',
            documento: '',
            confirmar: '',
            fechaNacimiento: null,
            accept: null,
            submitted: false,
            showMessage: false,
            loading: false,
            privacyModal: false,
            position: "center"
        }
    },
    computed: {
        labelComputed(){
        let label = ''

        if (this.loading) label = 'Loading...'
        else label = 'Sign in'

        return label
        },
        iconComputed(){
            let icon = ''

            if (this.loading) icon = 'pi pi-spin pi-spinner'
            else icon = ''

            return icon
        }
    },
    validations() {
        return {
            nombre: {
                required
            },
            apellido1: {
                required
            },
            username: {
                required
            },
            email: {
                required,
                email
            },
            password: {
                required, minLength: minLength(8)
            },
            confirmar: {
                required
            },
            documento: {
                required
            },
            telefono: {
                required
            },
            accept: {
                required
            },
            fechaNacimiento: {
                required
            },
        }
    },
    methods: {
        openPrivacyModal () {
            this.privacyModal = true;
        },
        closePrivacyModal (){
            this.privacyModal = false;
        },
        resetForm() {
            this.nombre= '',
            this.apellido1=  '',
            this.apellido2= '',
            this.username=  '',
            this.email=  '',
            this.password=  '',
            this.telefono=  '',
            this.documento=  '',
            this.fechaNacimiento=  null,
            this.accept=  null,
            this.submitted=  false,
            this.confirmar= ''
        },
        
        saveUser(user, token){
            var self = this
            this.$store.dispatch('saveCurrentUser', user);
            this.$store.dispatch('saveJwtToken', token);
            axios
            .get("/api/rol/"+user.idRol,{
                headers:{
                    Authorization: 'Bearer ' + token,
                }
            })
            .then(function (response) {
                self.saveUserRol(response.data.rol);
            }); 
        },
        saveUserRol(rol){
            this.$store.dispatch('saveCurrentRole', rol);
            this.$router.push("/").catch(() => {});
        },
        setLoading() {
            this.loading = true;
        },
        displayErrorMessage(error) {
            this.loading = false;
            this.$toast.add({severity:ToastSeverity.ERROR, summary: 'Register Failed!', detail: error, life: 5000});
        },
        handleSubmit(isFormValid) {
            this.submitted = true;

            if (!isFormValid) {
                return;
            }
            this.setLoading();
            var self = this
            var packet = {
                    "nombre": this.nombre,
                    "apellido1": this.apellido1,
                    "username": this.username,
                    "email": this.email,
                    "password": this.password,
                    "documento": this.documento,
                    "fechaNacimiento": this.fechaNacimiento,
                    "password_confirmation": this.confirmar,
                    "telefono": this.telefono
            }
            if(this.apellido2!=null){
                packet["apellido2"] = this.apellido2;
            }
            axios
            .post("/api/auth/register",packet)
            .then(function (response) {
                self.saveUser(response.data.user,response.headers.authorization);
            }).catch(error =>{
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
        }
    },
    components:{
        "Privacidad": Privacidad,
        "ErrorToast": ErrorToast
    }
    
}
</script>


<style scoped>
.submitButton {
    width: 100%;
    /* color: aqua; */
    background: white;
     border: none;
}
.submitButton:enabled:hover {
    width: 100%;
    /* color: aqua; */
    background: rgb(187 187 187 / 22%)!important;
    border: none;
    color:#ffffff;
    transition: all .25s ease;
}
.field {
    margin: 4px;
    /* height: 3em; */
}
.card {
    background-color: #1f3c5930;
    padding: 1.5rem;
    color: var(--surface-900);
    margin-bottom: 1rem;
    border-radius: 12px;
    box-shadow: 0px 3px 5px rgb(0 0 0 / 2%), 0px 0px 2px rgb(0 0 0 / 5%), 0px 1px 4px rgb(0 0 0 / 8%) !important;
}

#mainContainer{
    width: 100%;
}
.pi-eye {
    transform:scale(1.6);
    margin-right: 1rem;
}
.pi-eye-slash {
    transform:scale(1.6);
    margin-right: 1rem;
}
@import url('https://fonts.googleapis.com/css2?family=Kanit:ital,wght@1,300&family=Sarpanch:wght@400;900&display=swap');
.gradient-custom {
    /* fallback for old browsers */
    background: #6a11cb;
    
    /* Chrome 10-25, Safari 5.1-6 */
    /*background: -webkit-linear-gradient(to right, rgba(106, 17, 203, 1), rgba(37, 117, 252, 1));
    */
    
    /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
    background: linear-gradient(360deg, #621bc9, #00c6ff);
    
    height: 100%!important;
    
}

.main-card{
    padding: 1.5em 3em!important;
    width: 100%;
}
.button_custom {
    background:white!important;
}
.alertMessage{
    position: fixed!important;
    top:1px!important; 
    left: 50% !important;
    transform: translateX(-50%)!important;
}


.fieldsForm{
    background: #212529!important;
    color: white!important;
}

.loginlogo{
    height: 10em;
}
.loginTitle{
    font-family: "Kanit";
}
</style>