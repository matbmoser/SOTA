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
    meta: { requiresAuth: true, adminAuth: true, userAuth: true }
  },
  {
    path: "/admin/dashboard",
    name: "AdminDashboard",
    component: AdminDashboard,
    meta: { requiresAuth: true, adminAuth: true, userAuth: true }
  },
  {
    path: "/admin/incidencias",
    name: "AdminIncidencias",
    component: AdminIncidencias,
    meta: { requiresAuth: true, adminAuth: true, userAuth: true }
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
    meta: { requiresAuth: true, adminAuth: true, userAuth: true }
  },
  {
    path: "/incidencias",
    name: "Incidencias",
    component: Incidencias,
    meta: { requiresAuth: true, adminAuth: true, userAuth: true }
  },
  {
    path: "/tickets",
    name: "Tickets",
    component: Tickets,
    meta: { requiresAuth: true, adminAuth: true, userAuth: true }
  },
  {
    path: "/notificaciones",
    name: "Notificaciones",
    component: Notificaciones,
    meta: { requiresAuth: true, adminAuth: true, userAuth: true }
  },
  {
    path: "/profile/:name",
    name: "Profile",
    component: Profile,
    props: true,
    meta: { requiresAuth: true, adminAuth: true, userAuth: true }
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
  let jwtToken = store.state.jwtToken;
  let role = store.state.currentRole;
  // Check if the meta has a authentication tag
  if (to.meta.requiresAuth) {
      if (jwtToken === '') {
          // Send to the login page when the jwtToken is empty
          next('/login');
      }
      else if (to.meta.userAuth) {
          if (role === 'Usuario') {
              // Send to the next page when the user has the user role
              next();
          }
          else {
              // Send to the home page
              next('/');
          }
      }
      else if (to.meta.adminAuth) {
          if (role === 'Administrador') {
              // Send to the next page when the user has the admin role
              next();
          }
          else {
              // Send to the home page
              next('/');
          }
      }
      // Send to the next page, when a authentication tag is not required
  }
  else {
      next();
  }
});
export default router;
//# sourceMappingURL=index.js.map