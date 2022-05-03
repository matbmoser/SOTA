<template>
  <div class="leaderboard">
    <div class="p-grid p-jc-center">
      <div class="p-col-12">
        <DataTable :value="Vehiculos" responsiveLayout="stack" :scrollable="true" scrollHeight="800px" :sortOrder="1" sortField="created_at">
          <template #loading>
            Cargando Vehiculos, por favor espere...
          </template>

          <!--Header-->
          <template #header>
            <div class="p-d-flex p-jc-between p-ai-center">
              <h3 class="p-m-0">{{ header }}</h3>
            </div>
          </template>

          <!--Body-->
          <Column field="matricula" header="Matricula" />
          <Column field="segmento" header="Segmento" />
          <Column field="clasificacion" header="Tamaño" />
          <Column field="numAparcamientos" header="Aparcamientos" />
          <Column field="ultimoAparcamiento" header="Ultimo Aparcamiento" />
          <Column field="created_at" header="Creado en" />
            <Column class="actionButtons" style="display:flex; justify-content: center;">
                <template #body="slotProps">
                    <Button @click="deleteVehiculo($event, slotProps.data.id)" icon="pi pi-times" class="p-button-danger p-button-filled p-button-squared "></Button>
                    <ConfirmPopup></ConfirmPopup>
                </template>
            </Column>

        </DataTable>
      </div>
      <div class="w-full grid justify-content-end">
          <SpeedDial :model="items" style="position: fixed;
    bottom: 20px;
    right: 20px;" :radius="120" direction="up-left" type="quarter-circle" />
      </div>
    </div>
            <!-- Dialog -->
        <Dialog header="Añadir Vehiculo"
                v-model:visible="dialogDisplay"
                 :breakpoints="{'960px': '75vw'}" :style="{width: '30vw'}" :modal="true">
                <form autocomplete="off">
                <div class="p-fluid">
                    <div class="p-field" style="margin-top: 30px">
                        <span class="p-float-label">
                            <InputText id="activityNameInputText" type="text" v-model="matricula" />
                            <label>Matricula</label>
                        </span>
                    </div>
                    <div class="p-field" style="margin-top: 30px">
                        <span class="p-float-label">
                            <Dropdown v-model="tipoVehiculo" :options="TipoVehiculos" optionLabel="tipo" emptyMessage="No existen tipos de vehiculos" />
                            <label>Tipo de Vehiculo</label>
                        </span>
                    </div>
                </div>
                </form>
                <template #footer>
                    <div class="flex justify-content-center">
                    <Button class="p-buttom-primary"
                            :icon="iconComputed" 
                            :label="labelComputed" 
                            @click="SaveVehicle()">
                    </Button>
                    </div>
                </template>
          </Dialog>
  </div>
</template>

<script>
import axios from "axios";
import SpeedDial from 'primevue/speeddial';
import {ToastSeverity} from 'primevue/api';
export default {
  name: "ListaVehiculos",
  props: {
    Vehiculos: Array,
    TipoVehiculos: Array,
    header: String
  },
  components:{
    "SpeedDial":SpeedDial
  },
  computed: {
        labelComputed(){
            let label = ''

            if (this.loading) label = 'Añadiendo Vehiculo...'
            else label = 'Añadir Vehiculo'

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
        //Used to show the edit dialog
            showEditDialog(user) {
                //Save the user to be used in the saveUserRoles method
                this.vehicle = vehicle;
                this.dialogDisplay = true;
            },
            //Used to hide the edit Dialog
            hideEditDialog() {
                this.dialogDisplay = false;
            },
            displayMessage(severity, summary, message) {
                this.loading = false;
                this.$toast.add({severity:severity, summary: summary, group:'err', detail: message});
            },
            deleteVehiculo(event, id) {
                this.$confirm.require({
                target: event.currentTarget,
                message: '¿Estás seguro que quieres borrar este vehiculo?',
                icon: 'pi pi-exclamation-triangle',
                acceptLabel: "Borrar",
                rejectLabel: "Cancelar",
                accept: () => {
                    //callback to execute when user confirms the action
                var self = this;
                this.loading = true;
                axios.delete('/api/vehiculo/user/'+this.$store.state.currentUser.id, {
                        "id": id,
                        "idUsuario": this.$store.state.currentUser.id
                    },
                    {
                        headers: {
                            Authorization: 'Bearer ' + this.$store.state.jwtToken,
                        }
                    })
                    .then(response => {
                        self.displayMessage(ToastSeverity.SUCCESS, "¡Vehiculo Borrado!", "El vehiculo ha sido borrado de tu lista...");
                        location.reload();
                        
                    }).catch(error =>{
                        if(error.response.data.message!=null){
                             self.displayMessage(ToastSeverity.ERROR, "¡Fallo al borrar el Vehiculo!", "Intente enviar otra vez... Error: ["+error.response.data.message+"]");
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
                                self.displayMessage(ToastSeverity.ERROR, "¡Fallo al borrar el Vehiculo!", "Intente enviar otra vez... Error: ["+err+"]");
                            }else{
                                self.displayMessage(ToastSeverity.ERROR, "¡Fallo al borrar el Vehiculo!", "Intente enviar otra vez...");
                            }
                        }
                    });
                                },
                reject: () => {}
            }); 

        },
		SaveVehicle() { 
                var self = this;
                this.loading = true;
                axios.put('/api/vehiculo/user/'+this.$store.state.currentUser.id, {
                        "matricula":this.matricula,
                        "idTipoVehiculo": this.tipoVehiculo.id,
                        "idUsuario": this.$store.state.currentUser.id
                    },
                    {
                        headers: {
                            Authorization: 'Bearer ' + this.$store.state.jwtToken,
                        }
                    })
                    .then(response => {
                        this.dialogDisplay = false;
                        self.displayMessage(ToastSeverity.SUCCESS, "¡Vehículo Añadido!", "El vehiculo ha sido añadido en tu lista...");
                        location.reload();
                        
                    }).catch(error =>{
                         if(error.response.data.message!=null){
                             self.displayMessage(ToastSeverity.ERROR, "¡Fallo al añadir vehículo!", "Intente enviar otra vez... Error: ["+error.response.data.message+"]");
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
                                self.displayMessage(ToastSeverity.ERROR, "¡Fallo al añadir vehículo!", "Intente enviar otra vez... Error: ["+err+"]");
                            }else{
                                self.displayMessage(ToastSeverity.ERROR, "¡Fallo al añadir vehículo!", "Intente enviar otra vez...");
                            }
                        }
                      
                    });
                

            },
    //Load the DataTable data in the Fields
  },data() {
      return {
          matricula: null,
          tipoVehiculo: null,
          dialogDisplay: false,
          editDialog: false,
          vehicleTypeValue: null,
          loading: false,
          items: [
              {
                  label: 'Add',
                  icon: 'pi pi-plus',
                  command: () => {
                      this.dialogDisplay = true;
                  }
              },
              {
                  label: 'Update',
                  icon: 'pi pi-refresh',
                  command: () => {
                      this.$toast.add({ severity: 'success', summary: 'Update', detail: 'Data Updated' });
                  }
              },
              {
                  label: 'Delete',
                  icon: 'pi pi-trash',
                  command: () => {
                      this.$toast.add({ severity: 'error', summary: 'Delete', detail: 'Data Deleted' });
                  }
              },
              {
                  label: 'Upload',
                  icon: 'pi pi-upload',
                  command: () => {
                      this.$router.push('fileupload');
                  }
              },
              {
                  label: 'Vue Website',
                  icon: 'pi pi-external-link',
                  command: () => {
                      window.location.href = 'https://vuejs.org/'
                  }
              }
          ]
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
