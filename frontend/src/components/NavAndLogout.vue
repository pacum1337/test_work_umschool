<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <router-link tag="li" class="nav-item" active-class="active" exact to="/">
          <a class="nav-link">Главная</a>
        </router-link>

        <router-link tag="li" class="nav-item" active-class="active" :to="'/' + lesson.slug + '/'" exact v-for="lesson in lessons" :key="lesson.slug">
          <a class="nav-link">{{ lesson.name }}</a>
        </router-link>
      </ul>
      <div class="ml-auto my-auto d-flex align-items-center">
        <p v-if="username && token !== ''" class="mb-0 mr-4">
          Здравствуйте {{ profile.full_name }}
        </p>
        <p v-else class="mb-0">Вы не авторизованы</p>
        <form v-if="token !== ''" @submit.prevent="logOut()">
          <button class="btn btn-info">Выход из профиля</button>
        </form>
      </div>
    </div>
  </nav>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return{
      lessons: []
    }
  },
  methods: {
    async logOut() {
      await fetch(this.$store.getters.getDomen + 'auth/token/logout/', {
        method: 'post',
        headers: {
          'Authorization': 'Token ' + this.token
        }
      });
      this.$store.commit('logOut')
    }
  },
  computed: {
    token() {
      return this.$store.getters.getToken
    },
    username() {
      return this.$store.getters.getUsername
    },
    profile() {
      return this.$store.getters.getProfile
    }
  },
  mounted() {
      axios
              .get(this.$store.getters.getDomen + "api/v1/lessons/")
              .then(response => {
                  this.lessons = response.data;
              })
              .catch(function(e){
                  this.error = e;
              });
  },
}
</script>

<style scoped>

</style>
