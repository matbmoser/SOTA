<template>
  <div class="leaderboard">
    <div class="p-grid p-jc-center">
      <div class="p-col-12">
        <DataTable :value="Incidencias" responsiveLayout="stack" :scrollable="true" scrollHeight="800px" :sortOrder="1" sortField="created_at">
          <template #loading>
            Cargando Incidencias, por favor espere...
          </template>

          <!--Header-->
          <template #header>
            <div class="p-d-flex p-jc-between p-ai-center">
              <h3 class="p-m-0">{{ header }}</h3>
            </div>
          </template>

          <!--Body-->
          <Column field="gravedad" header="Gravedad" />
          <Column field="titulo" header="Titulo" />
          <Column field="descripcion" header="Descripción" />
          <Column field="fechaCierre" header="Fecha Cierre" />
          <Column field="resulta" header="Estado" />
          <Column field="notaCierre" header="Nota Cierre" />
          <Column field="created_at" header="Creado en" />
            <Column v-if="edit" class="actionButtons" style="display:flex; justify-content: center;">
                <template #body="slotProps">
                    <Button @click="closeIncidencia(slotProps.data.id)" icon="pi pi-check" class="p-button-success p-button-filled p-button-squared "></Button>
                    <ConfirmPopup></ConfirmPopup>
                </template>
            </Column>
        </DataTable>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {ToastSeverity} from 'primevue/api';
export default {
  name: "ListaIncidecnias",
  props: {
    Incidencias: Array,
    header: String,
    edit:Boolean
  },
  methods:{
        displayMessage(severity, summary, message) {
            this.loading = false;
            this.$toast.add({severity:severity, summary: summary, group:'err', detail: message});
        }
    //Load the DataTable data in the Fields
  },data() {
      return {
          loading: false,
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
