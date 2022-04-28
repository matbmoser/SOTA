<template>
	<div class="layout-menu-container">
		<AppSubmenu :items="model" class="layout-menu" :root="true" @menuitem-click="onMenuItemClick" @keydown="onKeyDown" />
		<a href="https://www.primefaces.org/primeblocks-vue" class="block mt-3">
			<img alt="primeblocks" src="../assets/img/logowhite.png" class="w-full" />
		</a>
	</div>
</template>

<script>
import AppSubmenu from './AppSubmenu';

export default {
	props: {
		model: Array
	},
    methods: {
        onMenuItemClick(event) {
            this.$emit('menuitem-click', event);
        },
		onKeyDown(event) {
			const nodeElement = event.target;
			if (event.code === 'Enter' || event.code === 'Space') {
				nodeElement.click();
				event.preventDefault();
			}
		},

    },
	computed: {
		darkTheme() {
			return this.$appState.darkTheme;
		}
	},
	components: {
		'AppSubmenu': AppSubmenu
	}
}
</script>