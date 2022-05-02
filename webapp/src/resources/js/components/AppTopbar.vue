<template>
	<div class="layout-topbar">
		<router-link to="/" class="layout-topbar-logo">
			<img alt="Logo" src="../media/img/logowhite.png" />
			<span>UFV MyParking</span>
		</router-link>
		<button class="p-link layout-menu-button layout-topbar-button" @click="onMenuToggle">
			<i class="pi pi-bars"></i>
		</button>

		<button class="p-link layout-topbar-menu-button layout-topbar-button"
			v-styleclass="{ selector: '@next', enterClass: 'hidden', enterActiveClass: 'scalein', 
			leaveToClass: 'hidden', leaveActiveClass: 'fadeout', hideOnOutsideClick: true}">
			<i class="pi pi-ellipsis-v"></i>
		</button>
		<ul class="layout-topbar-menu hidden lg:flex origin-top">
			<li>
				<button @click="logout" class="p-link layout-topbar-button">
					<i class="pi pi-sign-out"></i>
					<span>Logout</span>
				</button>
			</li>
			<li>
				<router-link to="/profile">
					<button class="p-link layout-topbar-button">
						<i class="pi pi-user"></i>
						<span>Perfil</span>
					</button>
				</router-link>
			</li>
			<li>
				<router-link to="/notificaciones">
					<button class="p-link layout-topbar-button">
						<i class="pi pi-bell"></i>
						<span>Notificaciones</span>
					</button>
				</router-link>
			</li>
		</ul>
	</div>
</template>

<script>
import axios from "axios";
export default {
    methods: {
        onMenuToggle(event) {
            this.$emit('menu-toggle', event);
        },
		onTopbarMenuToggle(event) {
            this.$emit('topbar-menu-toggle', event);
        },
		logout(event){
			
			var self = this;
			var jwtToken = this.$store.state.jwtToken
			this.$store.dispatch('deleteStore');
			this.$router.push("/login").catch(() => {});
			axios.post("/api/auth/logout",
				{
   					key: "value"
				}, 
				{
                headers:{
                    Authorization: 'Bearer ' + jwtToken,
                }
            })
		}
    },
	computed: {
		darkTheme() {
			return this.$appState.darkTheme;
		}
	}
}
</script>