<template>
	<div class="layout-topbar">
		<router-link to="/" class="layout-topbar-logo">
			<img alt="Logo" src="../assets/img/logowhite.png" />
			<span>WebApp MyParking</span>
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
				<router-link to="/notificaciones">
					<button class="p-link layout-topbar-button">
						<i class="pi pi-bell"></i>
						<span>Notificaciones</span>
					</button>
				</router-link>
			</li>
			<li>
				<router-link to="/profile">
					<button class="p-link layout-topbar-button">
						<i class="pi pi-user"></i>
						<span>Perfil</span>
					</button>
				</router-link>
			</li>
		</ul>
	</div>
</template>

<script>
export default {
    methods: {
        onMenuToggle(event) {
            this.$emit('menu-toggle', event);
        },
		onTopbarMenuToggle(event) {
            this.$emit('topbar-menu-toggle', event);
        },

    },
	computed: {
		darkTheme() {
			return this.$appState.darkTheme;
		}
	}
}
</script>