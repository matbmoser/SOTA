<template>
	<div id="app">
		
		<div class="app-container">
			<img alt="Vue logo" src="assets/primevue-logo.png">
			<HelloWorld msg="Vue + PrimeVue + Laravelmix App"/>
			<form @submit.prevent="greet">
				<InputText type="text" v-model="text"/>
				<Button type="submit" label="Submit"/>
				<h3>{{message}}</h3>
			</form>
		</div>

		<Toast/>
	</div>
</template>

<script>
	import HelloWorld from './components/HelloWorld.vue'
    import { useToast } from 'primevue/usetoast'
    import Button from 'primevue/button'
    import Toast from 'primevue/toast'
	export default {
		data() {
			return {
				message: null,
				text: null,
			}
		},
		created() {  
			this.fetchData();  
			this.timer = setInterval(this.fetchData, 5000);  
		},  
		methods: {
			greet() {
                this.$toast.add({severity: 'info', summary: 'Hello '  + this.text});
				this.message = 'Hello ' + this.text;
			},
			async fetchData() {  

			},  
			cancelAutoUpdate() {  
			clearInterval(this.timer);  
			},  
		}, 
		beforeDestroy() {  
			this.cancelAutoUpdate();  
		},  
		components: {
			HelloWorld
		}
		}
</script>

<style scoped>
	#app {
		font-family: 'Avenir', Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		color: #2c3e50;
		margin-top: 60px;
	}

	.app-container {
		text-align: center;
	}

	body #app .p-button {
		margin-left: .2em;
	}

	form {
		margin-top: 2em;
	}
</style>
