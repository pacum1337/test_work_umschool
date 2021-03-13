import Vue from "vue";
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        username: '',
        token: '',
        domen: 'http://127.0.0.1:8000/',
        profile: {
            full_name: "",
            status: ''
        }
    },
    mutations: {
        setToken: (state, {auth_token}) => {
            state.token = auth_token
            sessionStorage.token = auth_token
        },
        setUsername: (state, payload) => {
            state.username = payload
            sessionStorage.username = payload
        },
        setProfile: (state, {full_name, status}) => {
            state.profile.full_name = full_name
            state.profile.status = status
            sessionStorage.full_name = full_name
            sessionStorage.status = status
        },
        logOut: (state) => {
            state.username = ""
            sessionStorage.username = ""

            state.token = ""
            sessionStorage.token = ""

            state.profile = {
                full_name: '',
                status: ''
            }
            sessionStorage.full_name = ''
            sessionStorage.status = ''
        }
    },
    actions: {},
    getters: {
        getToken: (state) => {
            if (sessionStorage.token) {
                state.token = sessionStorage.getItem('token')
            }
            if (state.token === undefined) {
                state.token = ""
            }
            return state.token
        },
        getProfile: (state) => {
            if (sessionStorage.profile) {
                state.profile.full_name = sessionStorage.getItem('full_name')
                state.profile.status = sessionStorage.getItem('status')
            }
            if (state.profile === undefined) {
                state.profile = {
                    full_name: '',
                    status: ''
                }
            }
            return state.profile
        },
        getUsername: (state) => {
            if (sessionStorage.username) {
                state.username = sessionStorage.getItem('username')
            }
            return state.username
        },
        getDomen: (state) => {
            return state.domen
        }
    }
})
