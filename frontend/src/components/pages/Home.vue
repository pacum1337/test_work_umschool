<template>
  <div>
    <h1>Главная</h1>
    <div class="alert alert-danger" role="alert" v-if="!hasUser">
      <div v-for="userMsg in serverMsg.username" :key="userMsg">
        {{ userMsg }}
      </div>
      <div v-for="userMsg in serverMsg.password" :key="userMsg">
        {{ userMsg }}
      </div>
      <div v-for="userMsg in serverMsg.non_field_errors" :key="userMsg">
        {{ userMsg }}
      </div>
    </div>
    <form @submit.prevent="logIn()">
      <div class="form-group">
        <label for="username">Имя пользователя</label>
        <input
            type="text"
            class="form-control"
            id="username"
            name="username"
            v-model="userData.username"
        >
      </div>
      <div class="form-group">
        <label for="password">Пароль</label>
        <input
            type="password"
            class="form-control"
            id="password"
            name="password"
            v-model="userData.password"
        >
      </div>
      <button
          type="submit"
          class="btn btn-primary"
      >Авторизация
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      userData: {
        username: '',
        password: ''
      },
      hasUser: true,
      serverMsg: '',
    }
  },
  methods: {
    async logIn() {
      var response = await fetch(this.$store.getters.getDomen + 'auth/token/login/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.userData)
      });
      if (response.status === 200) {
        this.hasUser = true
        this.$store.commit('setToken', await response.json())
        this.$store.commit('setUsername', this.userData.username)
        this.userData.username = ''
        this.userData.password = ''
        this.getProfile()
      } else {
        this.hasUser = false
        this.serverMsg = await response.json()
      }
    },
    getProfile() {
      axios
          .get(
              this.$store.getters.getDomen + "api/v1/profile/",
              {
                headers: {
                  'Authorization': this.token
                }
              })
          .then(response => {
            this.$store.commit('setProfile', response.data)
          })
          .catch(function (e) {
            this.error = e;
          });
    }
  },
  computed: {
    token() {
      return this.$store.getters.getToken
    },
    profile() {
      return this.$store.getters.getProfile
    }
  },
}
</script>

<style scoped>

</style>
