import { createWebHistory, createRouter } from "vue-router";
import Home from "./views/Home.vue";
import Profile from "./views/Profile.vue";
import AdminDashboard from "./views/AdminDashboard.vue";
import AdminIncidencias from "./views/AdminIncidencias.vue";
import Notificaciones from "./views/Notificaciones.vue";
import Incidencias from "./views/Incidencias.vue";
import Tickets from "./views/Tickets.vue";
import Vehiculos from "./views/Vehiculos.vue";
import NotFound from "./views/NotFound.vue";
import Login from "./views/Login.vue";
import Register from "./views/Register.vue";
export const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/admin/dashboard",
    name: "AdminDashboard",
    component: AdminDashboard,
  },
  {
    path: "/admin/incidencias",
    name: "AdminIncidencias",
    component: AdminIncidencias,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/vehiculos",
    name: "Vehiculos",
    component: Vehiculos,
  },
  {
    path: "/incidencias",
    name: "Incidencias",
    component: Incidencias,
  },
  {
    path: "/tickets",
    name: "Tickets",
    component: Tickets,
  },
  {
    path: "/notificaciones",
    name: "Notificaciones",
    component: Notificaciones,
  },
  {
    path: "/profile/:name",
    name: "Profile",
    component: Profile,
    props: true,
  },
  {
  path: "/:catchAll(.*)",
  component: NotFound,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;