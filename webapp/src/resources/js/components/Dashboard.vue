<template>
	<div :class="containerClass" @click="onWrapperClick">
        <div>
            <AppTopBar @menu-toggle="onMenuToggle"/>
            <div class="layout-sidebar" @click="onSidebarClick">
                <AppMenu :model="menu" @menuitem-click="onMenuItemClick" />
            </div>
        </div>
        <div id="wrapper" class="layout-main-container">
            <div class="layout-main" >
                <slot>
                    This will only be displayed if there is no content
                    to be distributed.
                </slot>
            </div>
        </div>
	</div>
</template>

<script>
import AppTopBar from './AppTopbar.vue';
import AppMenu from './AppMenu.vue';

export default {
    name: "Dashboard",
    data() {
        return {
            layoutMode: 'static',
            staticMenuInactive: false,
            overlayMenuActive: false,
            mobileMenuActive: false,
        }
    },
    watch: {
        $route() {
            this.menuActive = false;
        }
    },
    methods: {
        onWrapperClick() {
            if (!this.menuClick) {
                this.overlayMenuActive = false;
                this.mobileMenuActive = false;
            }
            this.menuClick = false;
        },
        onMenuToggle() {
            this.menuClick = true;
            if (this.isDesktop()) {
                if (this.layoutMode === 'overlay') {
					if(this.mobileMenuActive === true) {
						this.overlayMenuActive = true;
					}
                    this.overlayMenuActive = !this.overlayMenuActive;
					this.mobileMenuActive = false;
                }
                else if (this.layoutMode === 'static') {
                    this.staticMenuInactive = !this.staticMenuInactive;
                }
            }
            else {
                this.mobileMenuActive = !this.mobileMenuActive;
            }
            event.preventDefault();
        },
        onSidebarClick() {
            this.menuClick = true;
        },
        onMenuItemClick(event) {
            if (event.item && !event.item.items) {
                this.overlayMenuActive = false;
                this.mobileMenuActive = false;
            }
        },
		onLayoutChange(layoutMode) {
			this.layoutMode = layoutMode;
		},
        addClass(element, className) {
            if (element.classList)
                element.classList.add(className);
            else
                element.className += ' ' + className;
        },
        removeClass(element, className) {
            if (element.classList)
                element.classList.remove(className);
            else
                element.className = element.className.replace(new RegExp('(^|\\b)' + className.split(' ').join('|') + '(\\b|$)', 'gi'), ' ');
        },
        isDesktop() {
            return window.innerWidth >= 992;
        },
        isSidebarVisible() {
            if (this.isDesktop()) {
                if (this.layoutMode === 'static')
                    return !this.staticMenuInactive;
                else if (this.layoutMode === 'overlay')
                    return this.overlayMenuActive;
            }
            return true;
        },
    },
    computed: {
        containerClass() {
            return ['layout-wrapper', {
                'layout-overlay': this.layoutMode === 'overlay',
                'layout-static': this.layoutMode === 'static',
                'layout-static-sidebar-inactive': this.staticMenuInactive && this.layoutMode === 'static',
                'layout-overlay-sidebar-active': this.overlayMenuActive && this.layoutMode === 'overlay',
                'layout-mobile-sidebar-active': this.mobileMenuActive,
				'p-input-filled': this.$primevue.config.inputStyle === 'filled',
				'p-ripple-disabled': this.$primevue.config.ripple === false
            }];
        },
    },
    beforeCreate() {
        this.menu = [
                {
                    label: 'Home', icon: 'pi pi-fw pi-home',
                    items: [{
                        label: 'Dashboard', icon: 'pi pi-fw pi-chart-bar', to: '/'
                    }]
                },
				{
					label: 'Área del Usuario', icon: 'pi pi-fw pi-sitemap',
					items: [
						{label: 'Vehiculos', icon: 'pi pi-fw pi-car', to: '/vehiculos'},
                        {label: 'Tickets', icon: 'pi pi-fw pi-ticket', to: '/tickets'},
                        {label: 'Incidencias', icon: 'pi pi-fw pi-exclamation-triangle', to: '/incidencias'},
					]
				}
            ];

         this.rolUsuario= this.$store.state.currentRole;
         if(this.rolUsuario["incidencias"] || this.rolUsuario["userDashboard"]){
            let adminDashboard = {label: 'Área del Administrador', icon: 'pi pi-fw pi-sitemap'};
            adminDashboard["items"] = [];
            if(this.rolUsuario["incidencias"]){
                adminDashboard["items"].push({label: 'Admin Incidencias', icon: 'pi pi-fw pi-check-square', to: '/admin/incidencias'});
            }
            if(this.rolUsuario["userDashboard"]){
                adminDashboard["items"].push({label: 'Admin Dashboard', icon: 'pi pi-fw pi-user-plus', to: '/admin/dashboard'});
            }
            this.menu.push(adminDashboard);
        } 
    },
    beforeUpdate() {


        if (this.mobileMenuActive)
            this.addClass(document.body, 'body-overflow-hidden');
        else
            this.removeClass(document.body, 'body-overflow-hidden');
    },
    components: {
        'AppTopBar': AppTopBar,
        'AppMenu': AppMenu,
    }
}
</script>
