<template>
  <DataView style="padding-top: 8px" :value=cleanUpTicket() layout='grid' :paginator=true :rows="15">
    <template #grid="slotProps">
      <div class="p-col-12 p-md-4 p-lg-3">
        <Card class="ticket">
          <template #title>
            {{ String(slotProps.data.token) }}
          </template>
          <template #content>

          </template>
        </Card>
      </div>
    </template>
    <template #empty>
      <div class="p-col-12">
        <Card class="ticket">
          <template #title>
            <div style="text-align: center">
              No tickets yet!
            </div>
          </template>
        </Card>
      </div>
    </template>
  </DataView>

  <Dialog v-model:visible="descriptionDialog" :header=this.descriptionName :modal=true :breakpoints="{'960px': '75vw', '640px': '100vw'}" :style="{width: '50vw'}">
    {{this.description}}
  </Dialog>
  
</template>

<script>
export default {
  name: "TicketFeed",
  props: {
    tickets: Array
  },
  data() {
    return {
      descriptionDialog: false,
      descriptionName: "",
      description: "",
    }
  },
  methods: {

    cleanUpTicket() {
      let temp = this.tickets
          .filter((value, index, array) => //remove any duplicate elements from array
              array.indexOf(array.find(findVal =>
                  findVal.id == value.id) //don't know why but this only works with == and not with ===
              ) === index
          );
      return temp.sort((a, b) => new Date(b.creation) - new Date(a.creation))
    },
    formatCreationDate(input) {
      let format = {
        year: 'numeric', month: 'numeric', day: 'numeric',
        hour: 'numeric', minute: 'numeric', second: 'numeric',
        hour12: false,
      };
      return new Intl.DateTimeFormat(['en-GB'], format).format(new Date(input))
    },
    updateDialogState(dialogId) {
      this.descriptionDialog = true
      this.description = this.tickets.find(act => act.id === dialogId).description
      this.descriptionName = this.tickets.find(act => act.id === dialogId).name
    }
  }
}
</script>

<style>
.p-card-title {
  text-align: left;
  font-weight: normal !important;
  font-size: 2rem;
}

.ticket {
  margin: 0.5em;
}

.p-card .p-card-content {
  padding: 0;
}

.expandDescription {
  color: #2196f3;
  font-weight: bold;
  width: max-content;
}

.expandDescription:hover {
  text-decoration: underline;
}

.likes {
  display: flex;
  justify-content: right;
  align-items: center;
}

.likes button {
  margin-left: 5px;
}
</style>