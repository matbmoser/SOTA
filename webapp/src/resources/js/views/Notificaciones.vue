<template>
<div>
  <div class="main">
  <div class="d-flex row justify-content-center">
  <div class="container-fluid">
    <h1 class="h1 mb-4 mt-4">Mis Notificaciones</h1>
    <Panel class="p-shadow-4" header="5 Last Registered Users">
          <template #icons>
                <p>Total Users:<span class='bg-primary' style='padding:10px;margin-top:20px;'>{{numUsers}} Users</span></p>
          </template>
          <DataTable :value="users" responsiveLayout="stack">
            <Column field="id" header="id"></Column>
            <Column field="nombre" header="Nombre"></Column>
            <Column field="email" header="Email"></Column>
            <Column field="documento" header="documento"></Column>
            <Column field="username" header="Username"></Column>
            <Column field="created_at" header="Joined At"></Column>
          </DataTable>
    </Panel>
    </div>
  </div>
</div>
</div>
</template>
<script>

    import axios from "axios";
    export default {
        data() {
            return {
                /**
                 * Number of Users Registered
                 * */
                numUsers: 0,
                users: null,
                basicData: {
                    labels: null,
                    datasets: [
                        {
                            label: 'Registered Users',
                            data: null,
                            fill: false,
                            borderColor: '#1bcf33'
                        }
                    ]
                }
            }
        },
        methods: {
            /**
             * Updates the users object with a JSON list of 5 last users
             * and filters and transform this information to the 7 last days of user
             * flow in the app to show in the chart.
             * @see forceUpdate()
             */
            fetchUsers() {
                axios
                    .get('/api/user', {
                        headers: {
                            Authorization: 'Bearer ' + this.token,
                        }
                    })
                    .then(response => {
                        const usr = response.data;
                        let lastDates = '01234567'.split('').map(function (n) {
                            var d = new Date();
                            d.setDate(d.getDate() - n);

                            return (function (day, month, year) {
                                return [day, month, year].join('/');
                            })(d.getDate(), d.getMonth() + 1, d.getFullYear());
                        }).sort();
                        let numDates = [0, 0, 0, 0, 0, 0, 0]
                        this.basicData.labels = '01234567'.split('').map(function (n) {
                            var d = new Date();
                            d.setDate(d.getDate() - n);

                            return (function (day, month) {
                                return [day < 10 ? '0' + day : day, month < 10 ? '0' + month : month].join('/');
                            })(d.getDate(), d.getMonth() + 1);
                        }).sort();

                        this.users = usr.filter(function (el, index) {
                            return index >= usr.length - 5;
                        });

                        lastDates.forEach(function (d, i) {
                            let dt = d.split("/");
                            let usrs = usr.filter(function (el) {
                                let myDate = new Date(el["created"]);
                                let date = myDate.getDate() + "/" + (myDate.getMonth() + 1) + "/" + myDate.getFullYear();
                                let date2 = dt[0] + "/" + dt[1] + "/" + dt[2];
                                return date < date2;
                            });
                            numDates[i] = usrs.length;
                        });

                        this.basicData.datasets[0].data = numDates;
                    })
            },
            /**
             * Updates the number of users with the lenght of a JSON list of all users from the back-end.
             * After this function is called use the forceUpdate() function to update the table.
             * uses API endpoint GET /api/user/
             *
             * @see forceUpdate()
             */
            fetchNumUsers() {
                fetch('/api/user', {
                    headers: {
                        Authorization: 'Bearer ' + this.token,
                    }
                })
                    .then(r => r.json())
                    .then(val => {
                        this.numUsers = val.length;
                    })
            }
        },
        mounted() {
            this.fetchUsers();
            this.fetchNumUsers();
        }
    }
</script>

<style scoped>
    .p-panel {
        box-shadow: 0 .5rem 1rem rgba(0,0,0,.15) !important;
        margin: 50px 0px;
    }

    .p-panel .p-panel-header {
        border: 1px solid #f7f7f7;
        padding: 1rem 1.25rem;
        background: #f7f7f7;
        color: #212529;
        border-top-right-radius: 4px;
        border-top-left-radius: 4px;
    }

    table {
        font-family: 'Open Sans', sans-serif;
        width: 750px;
        border-collapse: collapse;
        margin: 10px 10px 0 10px;
    }

    .t.row {
        margin: 0 !important;
    }

    table .p-datatable-thead tr th {
        text-transform: uppercase !important;
        text-align: left !important;
        background: #5600ff !important;
        color: #FFF !important;
    }

    table td:last-child {
        border-right: none;
    }

    table tbody tr:nth-child(2n) td {
        background: #e4d6ff;
    }
</style>

