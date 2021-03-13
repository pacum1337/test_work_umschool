<template>
  <div>
    <h1>Страница с чатом</h1>
    <div class="alert alert-danger" role="alert" v-if="error">
      {{ error }}
    </div>
    <div v-if="access !== 0">
      <div class="chat mb-5" v-for="data in chatData" :key="data.user + data.lesson">
        <h3 v-if="profile.status === 'student'">Чат по предмету {{ data.lesson.name }}</h3>
        <h3 v-else>Чат c {{ data.user.full_name }}</h3>
        <div class="chat-zone">
          <div class="message" v-for="message in data.messages" :key="message.id">
            <p>{{ message.message }}</p>
            <small>{{ message.who_wrote }}</small>
          </div>
        </div>
        <form @submit.prevent="sendMessage()">
          <div class="form-group mt-4">
            <label for="exampleFormControlTextarea1">Сообщение</label>
            <textarea v-model="message" class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
          </div>
          <button class="btn btn-info mt-2" type="submit">Отправить</button>
        </form>
      </div>
    </div>
    <div v-else>
      Доступ к выбраному предмету запрещен!
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      access: 0,
      slug: this.$route.params['slug'],
      error: '',
      chatData: {},
      message: ''
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
  methods: {
    loadData() {
      axios
          .get(
              this.$store.getters.getDomen + "api/v1/lessons/" + this.slug + "/",
              {
                headers: {
                  'Authorization': this.token
                }
              })
          .then(response => {
            this.access = response.data.access;
            this.chatData = response.data
          }, (error) => {
            console.log(error);
          });
      this.access = 0
    },
    async sendMessage() {
      if (this.message === ''){
        return
      }
      var data = {
        'message': this.message
      }
      var response = await fetch(
          this.$store.getters.getDomen + "api/v1/lessons/" + this.slug + "/",
          {
            method: 'post',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': this.token
            },
            body: JSON.stringify(data)
          });
      if (response.status === 204) {
        this.loadData()
        this.message = ''
      } //else {
      //
      // }

    }
  },
  mounted() {
    this.loadData()
  },
  watch: {
    $route(toR) {
      this.slug = toR.params['slug']
      this.loadData()
    }
  }
}
</script>

<style scoped>
.chat .chat-zone {
  width: 100%;
  height: 600px;
  border: 1px solid black;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  padding-top: 20px;
}

.chat .chat-zone .message {
  border: 1px solid gray;
  padding: 15px;
  margin: 20px;
  margin-top: 0;
  border-radius: 15px;
}

.chat .chat-zone .message small {
  font-size: 12px;
  color: gray;
}

.chat .chat-zone .message p {
  margin-bottom: 0;
}

.chat button {
  float: right;
}
</style>
