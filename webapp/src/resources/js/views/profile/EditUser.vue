<template>
    <div class="user p-grid p-fluid center">
        <div class="p-field p-col-12 p-md-6">
            <span class="p-float-label">
                <InputText id="username" type="text" v-model="currentUser.username" />
                <label for="username">Username</label>
            </span>
        </div>
        <div class="p-field p-col-12 p-md-6">
            <span class="p-float-label">
                <InputText id="nombre" type="text" v-model="currentUser.nombre" />
                <label for="nombre">Nombre</label>
            </span>
        </div>
        <div class="p-field p-col-12 p-md-6">
            <span class="p-float-label">
                <InputText id="email" type="text" v-model="currentUser.email" />
                <label for="email">Email</label>
            </span>
        </div>
        <div class="p-field p-col-12 p-md-6">
            <form>
                <span class="p-float-label">
                    <Password :feedback="false" id="password" type="password"/>
                    <label for="password">Contraseña</label>
                </span>
                <span class="p-float-label">
                    <Password :feedback="false" id="confirmpassword" type="password"/>
                    <label for="confirmpassword">Confirmar Contraseña</label>
                </span>
            </form>
        </div>
        <span class="p-buttonset p-col-12 p-md-4 center">
            <Button class="p-button-outlined" @click="toUser()" label="Back" icon="pi pi-user" iconpos="left" />
            <Button @click="saveUser()" label="Save" icon="pi pi-save" iconPos="left" />
        </span>
    </div>
</template>

<script>
    export default {
        data() {
            // define view data
            return {
                currentUser: this.$store.state.currentUser,
                token: this.$store.state.jwtToken
            }
        },
        methods: {
            // save the modified user profile to store and database
            saveUser() {
                var data = {
                    Id: this.currentUser.id,
                    Role: this.currentRole.nombre,
                    DisplayName: this.currentUser.nombre,
                    UserName: this.currentUser.username,
                    Email: this.currentUser.email,
                    Created: this.currentUser.created_at,
                };

                var postParam = {
                    headers: {
                        "Content-Type": "application/json",
                        'Authorization': 'Bearer ' + this.token,
                    },
                    body: JSON.stringify(data),
                    method: "PUT",
                };

                var vm = this;
                fetch("/api/users", postParam)
                    .then(function (response) {
                        if (response.ok) {
                            // dispatch the modified user data to the store
                            vm.$store.dispatch('saveCurrentUser', vm.currentUser);
                            vm.$router.push('/user');
                        }
                    })
                    .catch((error) => console.log(error));
            },
            toUser() {
                this.$router.push('/user');
            }
        }
    }
</script>

<style scoped>
    .center {
        margin: auto;
        padding: 10px;
    }

    .user {
        margin-top: 2%;
    }
</style>