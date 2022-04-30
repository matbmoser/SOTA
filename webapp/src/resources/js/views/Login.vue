<template>
    <div id="mainContainer" class="gradient-custom flex align-items-center justify-content-center">
            <div class="form-demo">
            <Dialog v-model:visible="showMessage" :breakpoints="{ '960px': '80vw' }" :style="{ width: '30vw' }" position="top">
                <div class="flex align-items-center flex-column pt-6 px-3">
                    <i class="pi pi-check-circle" :style="{fontSize: '5rem', color: 'var(--green-500)' }"></i>
                    <h5>Registration Successful!</h5>
                    <p :style="{lineHeight: 1.5, textIndent: '1rem'}">
                        Your account is registered under name <b>{{state.email}}</b> ; it'll be valid next 30 days without activation. Please check <b>{{state.email}}</b> and {{state.email}} for activation instructions.
                    </p>
                </div>
                <template #footer>
                    <div class="flex justify-content-center">
                        <Button label="OK" @click="toggleDialog" class="p-button-text" />
                    </div>
                </template>
            </Dialog>
                <div class="main-card justify-content-center">
                    <div class="card">
                        <div class="text-center mb-5">
                            <img src="../media/img/logowhite.png" alt="Image" class="loginlogo mb-3">
                            <div class="text-900 text-3xl font-medium mb-3 loginTitle">WebApp MyParking</div>
                        </div>
                        <form @submit.prevent="handleSubmit(!v$.$invalid)" class="p-fluid" autocomplete="off">
                            <div class="field mt-4">
                                <div class="p-float-label p-input-icon-right">
                                    <i class="pi pi-envelope" />
                                    <InputText id="email" v-model="v$.email.$model" :class="{'p-invalid':v$.email.$invalid && submitted}" aria-describedby="email-error"/>
                                    <label for="email" :class="{'p-error':v$.email.$invalid && submitted}">Email*</label>
                                </div>
                                <span v-if="v$.email.$error && submitted">
                                    <span id="email-error" v-for="(error, index) of v$.email.$errors" :key="index">
                                    <small class="p-error">{{error.$message}}</small>
                                    </span>
                                </span>
                                <small v-else-if="(v$.email.$invalid && submitted) || v$.email.$pending.$response" class="p-error">{{v$.email.required.$message.replace('Value', 'Email')}}</small>
                            </div>
                            <div class="field mt-4">
                                <div class="p-float-label">
                                    <Password id="password" v-model="v$.password.$model" :feedback="false" :class="{'p-invalid':v$.password.$invalid && submitted}" toggleMask>
          
          
                                    </Password>
                                    <label for="password" :class="{'p-error':v$.password.$invalid && submitted}">Password*</label>
                                </div>
                                <small v-if="(v$.password.$invalid && submitted) || v$.password.$pending.$response" class="p-error">{{v$.password.required.$message.replace('Value', 'Password')}}</small>
                            </div>
                        
                            <div class="field-checkbox">
                                <Checkbox id="remember" name="remember" value="Accept" v-model="v$.remember.$model" :class="{'p-invalid':v$.remember.$invalid && submitted}" />
                                <label for="remember" :class="{'p-error': v$.remember.$invalid && submitted}">Remember me</label>
                            </div>
                            <Button type="submit" label="Login" class="mt-2 submitButton" />
                        </form>
                    </div>
                </div>
            </div>
    </div>
</template>
<script>
import {ToastSeverity} from 'primevue/api';
import { reactive, ref, onMounted } from 'vue';
import { email, required } from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import { useStore } from 'vuex'
import router from '../route/index.js'
import axios from "axios";
export default {
    name: "Login",
    data() {
        return {
            user: null,
            authorization: null
        }
    },
    setup() {
        const store = useStore();

        const state = reactive({
            email: '',
            password: '',
            remember: null
        });

        const rules = {
            email: { required, email },
            password: { required },
            remember: { }
        };

        const submitted = ref(false);
        const showMessage = ref(false);

        const v$ = useVuelidate(rules, state);

        const handleSubmit = (isFormValid) => {
            submitted.value = true;

            if (!isFormValid) {
                return;
            }
            let emitObj = JSON.parse(JSON.stringify(this.additionalInfo));
            this.$emit('login', emitObj)

            axios
            .post("/api/auth/login",{
                "email": state.email,
                "password": state.password
            })
            .then(function (response) {
                saveUser(response.data.user,response.headers.authorization);
            });
        }
        const saveUser = (user, token) => {
            store.commit('saveCurrentUser',user);
            store.commit('saveJwtToken', token);
            
            axios
            .get("/api/rol/"+user.idRol,{
                headers:{
                    Authorization: 'Bearer ' + token,
                }
            })
            .then(function (response) {
                saveUserRol(response.data.rol);
            }); 
        }
        const saveUserRol = (rol) =>{
            store.commit('saveCurrentRole', rol);
            router.push("/");
        }
        const toggleDialog = () => {
            
            showMessage.value = !showMessage.value;

            if(!showMessage.value) {
                resetForm();
            }
        }

        const resetForm = () => {
            state.email = '';
            state.password = '';
            submitted.value = false;
        }

        return { state, v$, handleSubmit, toggleDialog, saveUserRol, saveUser, submitted, showMessage}
    },
    methods:{
        
    },
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
    margin-bottom: 1rem;
    width: 25em;
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
    height:100%;
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