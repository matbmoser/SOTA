<template>
	<div class="layout-footer">
		<img alt="Logo" src="../media/img/ufv.png" height="20" class="mr-2" />
		by
		<span class="font-medium ml-2">Mathias Brunkow Moser</span>
	</div>
</template>

<script>
	export default {
		name: "AppFooter",
		methods: {
		},
		computed: {
			darkTheme() {
				return this.$appState.darkTheme;
			}
		}
	}
</script>