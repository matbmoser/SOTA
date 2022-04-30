<template>
  <div class="p-grid nested-grid p-jc-center">
    
    <div class="p-col-10">
      <ScrollPanel style="width: 100%; height: 400px">
        <DataView layout="list" :value=notifications >
          <template #header>
            <div class="table-header">
              General
            </div>
          </template>
          <template #list="slotProps">
            <div class="p-col-12" :style=getBackgroundColour(slotProps.data.isRead) >
              <div class="p-grid">
                <div class="p-col-10 box" style="text-align:left">
                  {{ slotProps.data.title }}
                </div>
                <div class="p-col-2">
                  <Button @click="deleteNotification(slotProps.data.id, $event)" icon="pi pi-times" class="p-button-rounded p-button-plain p-button-text"/></div>
              </div>
            </div>
          </template>
        </DataView>
      </ScrollPanel>
    </div>
    <div class="p-col-10">
      <ScrollPanel style="width: 100%; height: 400px">
        <DataView layout="list" :value=joinRequests >
          <template #header>
            <div class="table-header">
              Groups
             </div>
          </template>
          <template #list="slotProps">
            <div class="p-col-12" :style=getBackgroundColour(false) >
              <div class="p-grid">
                <div class="p-col-10 box" style="text-align:left">
                  {{ slotProps.data.title }}
                </div>
                <div class="p-col-2" v-if="this.$store.state.currentUser.id == slotProps.data.group.ownerId">
                  <Button @click="acceptJoinRequest(slotProps.data.id, slotProps.data.group.id, $event)" icon="pi pi-check" class="p-button-rounded p-button-plain p-button-text"/>
                  <Button @click="rejectJoinRequest(slotProps.data.id, slotProps.data.group.id, $event)" icon="pi pi-times" class="p-button-rounded p-button-plain p-button-text"/>
                </div>
              </div>
            </div>
          </template>
        </DataView>
      </ScrollPanel>
    </div>
  </div>
</template>

<script>
export default {
  name: "NotificationPage",
  data() {
    return {
      notifications: [],
      joinRequests: [],
      getParam: {
        headers: {
          "Content-Type": "application/json",
          'Authorization': 'Bearer ' + this.$store.state.jwtToken
        },
        method: "GET"
      }
    }
  },
  beforeMount() {
    this.getNotification();
  },
  methods: {
    getBackgroundColour(isRead) {
      return isRead ? 'background-color: white': 'background-color: #e6e6e6';
    },
    getNotification() {
      fetch("/api/users/notificaciones", this.getParam)
          .then(r => {
            if (r.ok) return r.json();
            else return null;
          })
          .then(val => this.notifications = val)
          .catch(reason => console.log(reason));
    },
    deleteNotification(notId, event) {
      this.$confirm.require({
        target: event.currentTarget,
        message: 'Do you want to delete this record?',
        header: 'Delete Confirmation',
        icon: 'pi pi-info-circle',
        acceptClass: 'p-button-danger',
        accept: () => {
          let deleteParams = this.getParam
          deleteParams.method = "DELETE"
          fetch('/api/notifications/' + notId, deleteParams)
              .then(res => {
                if(!res.ok) throw new Error(res);
                else this.$router.go();
              })
              .catch(reason => console.log(reason))
        },
        reject: () => { }
      });
    },
    acceptJoinRequest(userId, groupId, event) {
      this.$confirm.require({
        target: event.currentTarget,
        message: 'Are you sure you want to accept this user to the group?',
        header: 'Accept request',
        icon: 'pi pi-info-circle',
        accept: () => {
          let postParams = this.getParam
            postParams.method = "POST"
            fetch(`/api/groups/${groupId}/requests/accept/${userId}`, postParams)
              .then(res => {
                  if (!res.ok) throw new Error(res);
                  else this.$router.go();
              })
              .catch(reason => console.log(reason))
        },
        reject: () => { }
      });
    },
      rejectJoinRequest(userId, groupId, event) {
      this.$confirm.require({
        target: event.currentTarget,
        message: 'Are you sure you want to reject this user from the group?',
        header: 'Accept request',
        icon: 'pi pi-info-circle',
        acceptClass: 'p-button-danger',
        accept: () => {
          let deleteParam = this.getParam
          deleteParam.method = "DELETE"
           fetch(`/api/groups/${groupId}/requests/deny/${userId}`, deleteParam)
              .then(res => {
                if(!res.ok) throw new Error(res);
                else this.$router.go();
              })
              .catch(reason => console.log(reason))
        },
        reject: () => { }
      });
    }
  }
}
</script>

<style>
.p-scrollpanel-wrapper {
  border-right: 9px solid var(--surface-b);
}

.p-scrollpanel-bar {
  background-color: var(--primary-color) !important;
  opacity: 1;
  transition: background-color .2s;
}

.p-scrollpanel-bar:hover {
  background-color: #007ad9 !important;
}
</style>