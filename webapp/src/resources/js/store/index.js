import { createStore } from 'vuex';
import createPersistedState from "vuex-persistedstate";
import axios from "axios";
import router from '../route/index.js';
export default createStore({
    state: {
        // Data that is accesible through the entire application, is stored in the localstorage
        jwtToken: '',
        currentUser: {},
        currentRole: {}
    },
    mutations: {
        // The only way to change data in a store state value is using a mutation method
        saveJwtToken(state, jwtToken) {
            state.jwtToken = jwtToken;
        },
        saveCurrentUser(state, currentUser) {
            state.currentUser = currentUser;
        },
        saveCurrentRole(state, currentRole) {
            state.currentRole = currentRole;
        },
        deleteJwtToken(state) {
            state.jwtToken = '';
        },
        deleteCurrentUser(state) {
            state.currentUser = {};
        },
        deleteCurrentRol(state) {
            state.currentRole = {};
        },
        deleteStore(state){
            state.jwtToken = '';
            state.currentUser = {};
            state.currentRole = {};
        }
    },
    actions: {
        updateProfile ({ commit, state }) {
        
        axios.get("/api/auth/check",{
            headers: { 
            'Authorization': 'Bearer ' + state.jwtToken,
            }
            }).then(response => {
                
            }).catch(e=>{
                commit("deleteStore");
                router.push("/login").catch(() => {});
            });
        },
        // Actions commit the mutation method
        saveJwtToken(context, jwtToken) {
            context.commit('saveJwtToken', jwtToken);
        },
        deleteJwtToken(context) {
            context.commit('saveJwtToken');
        },
        saveCurrentUser(context, currentUser) {
            context.commit('saveCurrentUser', currentUser);
        },
        deleteCurrentUser(context) {
            context.commit('saveCurrentUser');
        },
        saveCurrentRole(context, currentRole) {
            context.commit('saveCurrentRole', currentRole);
        },
        deleteCurrentRol(context) {
            context.commit('deleteCurrentRol');
        },
        deleteStore(context) {
            context.commit('deleteStore');
        },
    },
    modules: {},
    plugins: [createPersistedState()],
});
