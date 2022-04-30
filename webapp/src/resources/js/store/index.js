import { createStore } from 'vuex';
import createPersistedState from "vuex-persistedstate";

export default createStore({
    state: {
        // Data that is accesible through the entire application, is stored in the localstorage
        jwtToken: '',
        currentUser: {},
        currentRole: ''
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
    },
    actions: {
        // Actions commit the mutation method
        saveJwtToken(context, jwtToken) {
            context.commit('saveJwtToken', jwtToken);
        },
        saveCurrentUser(context, currentUser) {
            context.commit('saveCurrentUser', currentUser);
        },
        saveCurrentRole(context, currentRole) {
            context.commit('saveCurrentRole', currentRole);
        },
    },
    modules: {},
    plugins: [createPersistedState()],
});