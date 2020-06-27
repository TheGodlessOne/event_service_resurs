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
        <label for="password">Password</label>
        <input
          type="password"
          class="form-control"
          id="password"
          v-model="user.password"
          name="password"
        />
      </div>

      <button @click="loginUser" class="btn btn-success">Login</button>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import UserDataService from "../services/UserDataService";

export default {
  name: "user-login",
  data() {
    return {
      user: {
        username: "",
        password: "",
        wrongCred: false
      },
    };
  },
  methods: {
    loginUser () { 
      this.dispatch('loginUser', {
        username: this.username,
        password: this.password
      })
          .then(() => {
            this.wrongCred = false
            this.push({ name: 'downloads' })
          })
        .catch(err => {
          console.log(err)
          this.wrongCred = true
        })
      }
    }
}
</script>