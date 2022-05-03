<template>

    <div class="activity">
        <div class="p-grid p-jc-center">
            <div class="p-col-10 p-offset-9">
                <Button label="New activity"
                        icon="pi pi-check"
                        @click="OpenEditDialog">
                </Button>
            </div>
        </div>
        <div class="p-grid p-jc-center">
            <div class="p-col-10">
                <!-- DataTable -->
                <DataTable :value="activity"
                           :scrollable="true"
                           scrollHeight="flex">
                    <Column field="name"
                            header="Name"
                            style="min-width: 150px"></Column>
                    <Column field="description"
                            header="Description"
                            style="min-width: 150px"></Column>
                    <Column field="typeNavigation.name"
                            header="Activity"
                            style="min-width: 100px"></Column>
                    <Column field="amount"
                            header="Amount"
                            style="min-width: 100px"></Column>
                    <Column field="typeNavigation.unit"
                            header="Unit"
                            style="min-width: 100px"></Column>
                    <Column field="points"
                            header="Points"
                            style="min-width: 100px"></Column>
                    <Column field="creation"
                            header="Activity creation"
                            style="min-width: 200px"></Column>
                </DataTable>
            </div>
        </div>

        <!-- Dialog -->
        <Dialog header="Add activity"
                v-model:visible="dialogDisplay"
                style="min-width: 20%" :breakpoints="{'960px': '75vw'}" :style="{width: '50vw'}" :modal="true">
            <div class="p-fluid" style="min-height: 200px">
                <div class="p-field" style="margin-top: 20px">
                    <span class="p-float-label">
                        <InputText id="activityNameInputText" type="text" v-model="activityName" />
                        <label>Activity Name</label>
                    </span>
                </div>
                <div class="p-field" style="margin-top: 20px">
                    <span class="p-float-label">
                        <Dropdown v-model="activityTypeValue" :options="activityTypes" optionLabel="name" emptyMessage="No activity types could be found in the database" />
                        <label>Activity type</label>
                    </span>
                </div>
                <div class="p-field" style="margin-top: 20px">
                    <span class="p-float-label">
                        <InputText id="activityDescriptionInputText" type="text" v-model="activityDescription" />
                        <label>Activity Description</label>
                    </span>
                </div>
                <div class="p-field" style="margin-top: 20px">
                    <span class="p-float-label">
                        <InputText id="activityAmountInputText" type="number" v-model="activityAmount" />
                        <label>Activity Amount</label>
                    </span>
                </div>
            </div>
                <template #footer>
                    <Button class="p-button-text"
                            label="Save changes"
                            icon="pi pi-check"
                            @click="SaveActivity(this.permissionsValue)">
                    </Button>
                </template>
</Dialog>
    </div>
</template>


<script>
    export default {
        data() {
            // define view data
			return {
                activity: [],
                activityTypes: [],
                activityTypeValue: null,
                dialogDisplay: false,
                activityId: null,
                activityName: null,
                activityDescription: null,
                activityType: null,
				activityPoints: null,
                activityAmount: null,
				token: this.$store.state.jwtToken,
				currentUser: this.$store.state.currentUser
            };
        },
        mounted() {
            // fetch API endpoint
            this.FetchActivity();
            this.FetchActivityTypes();
        },

        methods: {

			FetchActivityTypes() {
				var parameters = {
                    headers: {
						"Content-Type": "application/json",
						'Authorization': 'Bearer ' + this.token
					},
					method: "GET"
				};

				fetch("/api/activity/types", parameters)
					.then((r) => r.json())
					.then((val) => {
						this.activityTypes = val;
					});
            },

            //Load 
            FetchActivity() {
				var parameters = {
                    headers: {
						"Content-Type": "application/json",
						'Authorization': 'Bearer ' + this.token
					},
					method: "GET"
				};
                fetch("/api/vehiculos/" + this.$store.state.currentUser.id, parameters)
                    .then((r) => r.json())
                    .then((val) => {
						this.activity = val;
                    });
            },

            //Load the DataTable data in the Fields
			OpenEditDialog(activity) {
				this.activityId = activity.id;
				this.activityName = activity.name;
				this.activityDescription = activity.description;
                this.activityType = activity.type;
                this.activityAmount = activity.amount;
                this.dialogDisplay = true;
            },

            //Save the modified or created activityType
			SaveActivity() {
                var data = {
					Name: this.activityName,
                    Description: this.activityDescription,
					Type: this.activityTypeValue.id,
                    Amount: this.activityAmount,
					User: this.$store.state.currentUser.id,
                };

                var postParam = {
                    headers: {
                        "Content-Type": "application/json",
						'Authorization': 'Bearer ' + this.token
                    },
                    body: JSON.stringify(data),
                    method: "PATCH",
                };

                fetch("/api/activity", postParam)
                    .then(function (response) {
                        if (response.status == 200) {
							location.reload();
                        }
                    })
                    .catch((error) => console.log(error));

                this.dialogDisplay = false;
            },
        },
    };
</script>

<style>
    .p-button.p-component {
        margin: 0 5px 0 5px;
    }
</style>
