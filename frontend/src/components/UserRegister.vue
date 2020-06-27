<template>
  <div class="submit-form">
    <div>
      <div class="form-group">
        <label for="username">Username</label>
        <input
          type="text"
          class="form-control"
          id="username"
          v-model="user.username"
          name="username"
        />
      </div>

      <div class="form-group">
        <label for="email">Email</label>
        <input
          type="email"
          class="form-control"
          id="email"
          v-model="user.email"
          name="email"
        />
      </div>

      <div class="form-group">
        <label for="password">Password</label>
        <input
          type="password"
          class="form-control"
          id="password"
          v-model="user.password"
          name="password"
        />
      </div>

      <button @click="registerUser" class="btn btn-success">Register</button>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import UserDataService from "../services/UserDataService";

export default {
  name: "register-user",
  data() {
    return {
      user: {
        email: '',
        username: '',
        password: '',
      },
    };
  },
  methods: {
    registerUser () { 
      this.dispatch('loginUser', {
        email: this.email,
        username: this.username,
        password: this.password,
      })
          .then(() => {
            this.wrongCred = false
            this.$router.push({ name: 'login' })
          })
      }
    }
}
</script>