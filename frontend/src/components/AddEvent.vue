<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <div class="form-group">
        <label for="event_title">Title</label>
        <input
          type="text"
          class="form-control"
          id="event_title"
          v-model="event.event_title"
          name="event_title"
        />
      </div>

      <div class="form-group">
        <label for="event_description">Description</label>
        <input
          type="text"
          class="form-control"
          id="event_description"
          v-model="event.event_description"
          name="event_description"
        />
      </div>

      <div class="form-group">
        <label for="event_date">Date</label>
        <input
          type="datetime-local"
          class="form-control"
          id="event_date"
          v-model="event.event_date"
          name="event_date"
        />
      </div>

      <button @click="saveEvent" class="btn btn-success">Submit</button>
    </div>

    <div v-else>
      <h4>Event created</h4>
      <button class="btn btn-success" @click="newEvent">Add</button>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import EventDataService from "../services/EventDataService";

export default {
  name: "create-event",
  data() {
    return {
      event: {
        id: null,
        title: "",
        description: "",
      },
    };
  },
  methods: {
    saveEvent() {
      var data = {
        title: this.event.event_title,
        description: this.event.description
      };

      EventDataService.create(data)
        .then(response => {
          this.event.id = response.data.id;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
    
    newEvent() {
      this.event = {};
    }
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>