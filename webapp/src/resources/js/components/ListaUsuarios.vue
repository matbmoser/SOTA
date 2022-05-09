<template>
  <div class="leaderboard">
    <div class="p-grid p-jc-center">
      <div class="p-col-12">
        <DataTable :value="Usuarios" responsiveLayout="stack" :scrollable="true" scrollHeight="800px" :sortOrder="1" sortField="created_at">
          <template #loading>
            Cargando Usuarios, por favor espere...
          </template>

          <!--Header-->
          <template #header>
            <div class="p-d-flex p-jc-between p-ai-center">
              <h3 class="p-m-0">{{ header }}</h3>
            </div>
          </template>

          <!--Body-->
          <Column field="nombre" header="Nombre" />
          <Column field="apellido1" header="Apellido" />
          <Column field="username" header="Username" />
          <Column field="email" header="Email" />
          <Column field="rol" header="Rol" />
          <Column field="created_at" header="Creado en" />
            <Column v-if="edit" class="actionButtons" style="display:flex; justify-content: center;">
                <template #body="slotProps">
                    <Button @click="changeRol(slotProps.data)" icon="pi pi-pencil" label="Editar Rol" class="mr-2 p-button-primary p-button-filled p-button-squared "></Button>
                    <Button @click="borrarUsuario($event, slotProps.data.id)" icon="pi pi-times" class="p-button-danger p-button-filled p-button-squared "></Button>
                    <ConfirmPopup></ConfirmPopup>
                </template>
            </Column>
        </DataTable>
      </div>
    </div>
         <!-- Dialog -->
        <Dialog header="Cambiar Rol Usuario"
                v-model:visible="dialogDisplay"
                 :breakpoints="{'960px': '75vw'}" :style="{width: '30vw'}" :modal="true">
                <form autocomplete="off">
                <div class="p-fluid">
                    <div class="p-field" style="margin-top: 30px">
                        <span class="p-float-label">
                            <Dropdown v-model="rol" :options="roles" optionLabel="nombre" emptyMessage="No existen roles..." />
                            <label>Roles</label>
                        </span>
                    </div>
                </div>
                </form>
                <template #footer>
                    <div class="flex justify-content-center">
                    <Button class="p-buttom-primary"
                            :icon="iconComputed" 
                            :label="labelComputed" 
                            @click="ActualizarRol()">
                    </Button>
                    </div>
                </template>
          </Dialog>
  </div>
</template>

<script>
import axios from "axios";
import {ToastSeverity} from 'primevue/api';
export default {
  name: "ListaUsuarios",
  props: {
    Usuarios: Array,
    header: String,
    edit:Boolean,
    roles:Array
  },
  
computed: {
    labelComputed(){
        let label = ''

        if (this.loading) label = 'Actualizando Rol...'
        else label = 'Actualizar Rol'

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
      changeRol(data){
          this.dialogDisplay = true;
          this.user = data;
          console.log(data["rol"])
          this.rol=data["rol"];
      },
      ActualizarRol(){
           this.loading=true;
            var self = this;
             var packet = {
                    "id": this.user.id,
                    "idRol": this.currentUser.nombre,
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
       deleteUsuario(event, id) {
                this.$confirm.require({
                target: event.currentTarget,
                message: '¿Estás seguro que quieres borrar este usuario?',
                icon: 'pi pi-exclamation-triangle',
                acceptLabel: "Borrar",
                rejectLabel: "Cancelar",
                accept: () => {
                    //callback to execute when user confirms the action
                var self = this;
                this.loading = true;
                axios.delete('/api/user',{ 
                    headers: {
                            Authorization: 'Bearer ' + this.$store.state.jwtToken
                        },
                    data:{
                        "id": id
                    }})
                    .then(response => {
                        self.displayMessage(ToastSeverity.SUCCESS, "¡Usuario Borrado!", "El usuario ha sido borrado de la app...");
                        location.reload();
                        
                    }).catch(error =>{
                        if(error.response.data.message!=null){
                             self.displayMessage(ToastSeverity.ERROR, "¡Fallo al borrar el Usuario!", "Intente enviar otra vez... Error: ["+error.response.data.message+"]");
                            return;
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
                                self.displayMessage(ToastSeverity.ERROR, "¡Fallo al borrar el Usuario!", "Intente enviar otra vez... Error: ["+err+"]");
                                return;
                            }
                        }
                        self.displayMessage(ToastSeverity.ERROR, "¡Fallo al borrar el Usuario!", "Intente enviar otra vez...");
                    });
                                },
                reject: () => {}
            });
       },
        displayMessage(severity, summary, message) {
            this.loading = false;
            this.$toast.add({severity:severity, summary: summary, group:'err', detail: message});
        }
    
    //Load the DataTable data in the Fields
  },data() {
      return {
          loading: false,
          user : null,
          dialogDisplay : false,
          rol:null
      }
   }, 
}
</script>

<style scoped>

    .speedial{
        position: fixed!important;
        bottom: 20px!important;
        right: 20px!important;
    }
</style>
<style lang="scss" scoped>
  ::v-deep(.user-item) {
    background: lightgreen!important;
  }
::v-deep(.speeddial-linear-demo) {
    .p-speeddial-direction-up {
        left: calc(50% - 2rem);
        bottom: 0;
        bottom: 0;
    }

    .p-speeddial-direction-down {
        left: calc(50% - 2rem);
        top: 0;
    }

    .p-speeddial-direction-left {
        right: 0;
        top: calc(50% - 2rem);
    }

    .p-speeddial-direction-right {
        left: 0;
        top: calc(50% - 2rem);
    }
}

::v-deep(.speeddial-circle-demo) {
    .p-speeddial-circle {
        top: calc(50% - 2rem);
        left: calc(50% - 2rem);
    }

    .p-speeddial-semi-circle {
        &.p-speeddial-direction-up {
            left: calc(50% - 2rem);
            bottom: 0;
        }

        &.p-speeddial-direction-down {
            left: calc(50% - 2rem);
            top: 0;
        }

        &.p-speeddial-direction-left {
            right: 0;
            top: calc(50% - 2rem);
        }

        &.p-speeddial-direction-right {
            left: 0;
            top: calc(50% - 2rem);
        }
    }

    .p-speeddial-quarter-circle {
        &.p-speeddial-direction-up-left {
            right: 0;
            bottom: 0;
        }

        &.p-speeddial-direction-up-right {
            left: 0;
            bottom: 0;
        }

        &.p-speeddial-direction-down-left {
            right: 0;
            top: 0;
        }

        &.p-speeddial-direction-down-right {
            left: 0;
            top: 0;
        }
    }
}

::v-deep(.speeddial-tooltip-demo) {
    .p-speeddial-direction-up {
        &.speeddial-left {
            left: 0;
            bottom: 0;
        }

        &.speeddial-right {
            right: 0;
            bottom: 0;
        }
    }
}

::v-deep(.speeddial-delay-demo) {
    .p-speeddial-direction-up {
        left: calc(50% - 2rem);
        bottom: 0;
    }
}

::v-deep(.speeddial-mask-demo) {
    .p-speeddial-direction-up {
        right: 0;
        bottom: 0;
    }
}
</style>
