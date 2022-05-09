<template>
  <div class="leaderboard">
    <div class="p-grid p-jc-center">
      <div class="p-col-12">
        <DataTable :value="Tickets" responsiveLayout="stack" :scrollable="true" scrollHeight="800px" :sortOrder="1" sortField="idPlaza">
          <template #loading>
            Cargando Tickets, por favor espere...
          </template>

          <!--Header-->
          <template #header>
            <div class="p-d-flex p-jc-between p-ai-center">
              <h3 class="p-m-0">{{ header }}</h3>
            </div>
          </template>

          <!--Body-->
          <Column style="font-weight: 700; font-size:1.5em" class="flex justify-content-center" field="idPlaza" header="Número de Plaza" />
          <Column field="matricula" header="Matrícula" />
          <Column field="entrada" header="Entrada Parking" />
          <Column field="salida" header="Salida Parking" />
            <Column class="actionButtons2" style="display:flex; justify-content: center;">
                <template #body="slotProps">
                    <Button @click="seeTicket(slotProps.data)" icon="pi pi-ticket" label="Ver Ticket" class="p-button-primary p-button-filled p-button-squared "></Button>
                </template>
            </Column>
        </DataTable>
      </div>
    </div>
            <!-- Dialog -->
  </div>
</template>

<script>
import axios from "axios";
import {ToastSeverity} from 'primevue/api';
export default {
  name: "ListaTickets",
  props: {
    Tickets: Array,
    header: String
  },
  methods:{
        //Used to show the edit dialog
    seeTicket(ticket) {
        this.token = ticket.token;
        this.$router.push("/ticket/"+this.token);
    },
    //Used to hide the edit Dialog
    displayMessage(severity, summary, message) {
        this.loading = false;
        this.$toast.add({severity:severity, summary: summary, group:'err', detail: message});
    },

    //Load the DataTable data in the Fields
  }
  ,data() {
      return {
          ticket: null,
          loading: false,
          token: "", 
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
