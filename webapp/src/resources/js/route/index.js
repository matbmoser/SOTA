import { createWebHistory, createRouter } from "vue-router";
import Home from "../views/Home.vue";
import Profile from "../views/Profile.vue";
import store from '../store/index.js';
import AdminDashboard from "../views/AdminDashboard.vue";
import AdminIncidencias from "../views/AdminIncidencias.vue";
import Notificaciones from "../views/Notificaciones.vue";
import Incidencias from "../views/Incidencias.vue";
import Tickets from "../views/Tickets.vue";
import Vehiculos from "../views/Vehiculos.vue";
import NotFound from "../views/NotFound.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";

export const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: { requiresAuth: true }
  },
  {
    path: "/admin/dashboard",
    name: "AdminDashboard",
    component: AdminDashboard,
    meta: { requiresAuth: true, userDashboard: true}
  },
  {
    path: "/admin/incidencias",
    name: "AdminIncidencias",
    component: AdminIncidencias,
    meta: { requiresAuth: true, incidencias: true }
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: {
      requiresAuth: false,
      hideNavigation: true 
    }
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
    meta: {
      requiresAuth: false,
      hideNavigation: true 
    }
  },
  {
    path: "/vehiculos",
    name: "Vehiculos",
    component: Vehiculos,
    meta: { requiresAuth: true}
  },
  {
    path: "/incidencias",
    name: "Incidencias",
    component: Incidencias,
    meta: { requiresAuth: true }
  },
  {
    path: "/tickets",
    name: "Tickets",
    component: Tickets,
    meta: { requiresAuth: true}
  },
  {
    path: "/notificaciones",
    name: "Notificaciones",
    component: Notificaciones,
    meta: { requiresAuth: true }
  },
  {
    path: "/profile/:name",
    name: "Profile",
    component: Profile,
    props: true,
    meta: { requiresAuth: true }
  },
  {
  path: "/:catchAll(.*)",
  component: NotFound,
  meta: {
    requiresAuth: true
  }
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  var rol = {};
  var jwtToken = '';
  if (to.meta.requiresAuth) {
    jwtToken = store.state.jwtToken;
    if (jwtToken === '') {
        // Send to the login page when the jwtToken is empty
        next('/login');
        return;
    }
    store.dispatch('updateProfile');
    rol = store.state.currentRole;
    }
    if (to.meta.incidencias && rol.incidencias==true) {
      next();
      return;
    } else if (to.meta.incidencias && rol.incidencias==false) {
      next("/");
      return;
    }
  
    if (to.meta.userDashboard && rol.userDashboard==true) {
      next();
      return;
    } else if (to.meta.userDashboard && rol.userDashboard==false){
      next("/");
      return;
    }
  
    if (jwtToken != '') {
      // Send to the login page when the jwtToken is empty
      if(to.name === 'Login' || to.name === 'Register')
      {
          next("/");
          return;
      }
    }
    next();
});
export default router;