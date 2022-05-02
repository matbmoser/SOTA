<template>
    <div>
    <Dashboard>
        <Fieldset legend="Ocupación Zonas" class="flex justify-content-center align-content-center" toggleable="true">
             <div class="grid">
                <div v-for="(zona, index) in zonas" :key="index">
                    <div class="col-4 w-full">
                        <Card :id="setIdZona(zona.letra)">
                            <template #title>
                                <div class="flex justify-content-end">
                                    <p>{{ tipoPlazas[zona.idTipoPlaza] }}</p>
                                </div>
                                <div class="flex justify-content-between">
                                <span class="letraZona">{{ zona.letra }}</span>
                                </div>
                            </template>
                            <template #content>
                                <span class="numZona">{{ plazas[zona.id] }}/{{ zona.plazas }}</span>
                            </template>
                        </Card>
                    </div>
                </div>
            </div>
        </Fieldset>
        <Fieldset legend="Mapa" class="mt-3 flex justify-content-center" :collapsed="true" toggleable="true">
            <img src="../media/img/mapaparking.jpg" style="width:100%" alt="Mapa" preview/>
        </Fieldset>
    </Dashboard>
    <Toast position="middle-center"/>
    </div>
</template>

<script>
import axios from "axios";
import {ToastSeverity} from 'primevue/api';
import Dashboard from '../components/Dashboard.vue';
    export default {
        name: 'Home',
        data(){
            return {
                numUsers: 0,
                zonas: null,
                plazas: null,
                tipoPlazas: null,
                currentIdx: 0,
                loading: false
            }
        },
        components: {
            "Dashboard" : Dashboard
        },
        methods: {
            setIdZona(letra){
                return "Zona"+letra;
            },
            /**
             * Updates the number of users with the lenght of a JSON list of all users from the back-end.
             * After this function is called use the forceUpdate() function to update the table.
             * uses API endpoint GET /api/user/
             *
             * @see forceUpdate()
             */
            fetchAll() {
                axios
                    .get('/api/plazas/validas/zonas', {
                        headers: {
                            Authorization: 'Bearer ' + this.$store.state.jwtToken,
                        }
                    })
                    .then(response => {
                        this.loading = false;
                        this.zonas = response.data.zonas;
                        this.tipoPlazas = response.data.tipoPlazas;
                        this.plazas = response.data.plazas;
                    })
            },
            displayErrorMessage(error) {
                this.loading = false;
                this.$toast.add({severity:ToastSeverity.ERROR, summary: 'Login Failed!', detail:error, life: 3000});
            },
            startLoading() {
                this.loading = true;
                this.$toast.add({severity:ToastSeverity.INFO, summary: 'Loading Content', detail: "<ProgressSpinner />", life: 4000});
            },
        },
        mounted() {
            this.startLoading(),
            this.fetchAll()
        }
    }
</script>

<style scoped>
.numZona, .letraZona{
    font-size:4.5rem;
}
.letraZona{
    margin-right:10px
}

/** INICIO ZONAS APARCAMIENTO **/
#ZonaA{
    background-color: rgb(255 192 0);
}
#ZonaB{
    background-color: rgb(0 31 255);
}
#ZonaC{
    background-color: rgb(223 1 8);
}
#ZonaD{
    background-color: rgb(0 230 5);
}
#ZonaE{
    background-color: rgb(68 0 255);

}
#ZonaF{

    background-color: rgb(255 22 203);
}

#ZonaG{

    background-color: rgb(0 222 224);
}

#ZonaH{

    background-color: rgb(250 129 0);
}
#ZonaI{

    background-color: rgb(127 41 40);
}

</style>
