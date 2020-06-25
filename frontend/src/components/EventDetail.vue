<template>
  <div v-if="currentEvent" class="edit-form">
    <h4>Event</h4>
    <form>
      <div class="form-group">
        <label for="event_title">Title</label>
        <input type="text" class="form-control" id="event_title"
          v-model="currentEvent.event_title"
        />
      </div>
      <div class="form-group">
        <label for="event_description">Description</label>
        <input type="text" class="form-control" id="event_description"
          v-model="currentEvent.event_description"
        />
      </div>
      <div class="form-group">
        <label for="event_date">Date</label>
        <input type="datetime-local" class="form-control" id="event_date"
          v-model="currentEvent.event_date"
        />
      </div>
    </form>

    <button class="badge badge-danger mr-2"
      @click="deleteEvent"
    >
      Delete
    </button>

    <button type="submit" class="badge badge-success"
      @click="updateEvent"
    >
      Update
    </button>
    <p>{{ message }}</p>
  </div>

  <div v-else>
    <br />
    <p>Please click on a event...</p>
  </div>
</template>

<script>
/* eslint-disable */
import EventDataService from "../services/EventDataService";

export default {
  name: "event",
  data() {
    return {
      currentEvent: null,
      message: ''
    };
  },
  methods: {
    getEvent(id) {
      EventDataService.get(id)
        .then(response => {
          this.currentEvent = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },

    updateEvent() {
      EventDataService.update(this.currentEvent.id, this.currentEvent)
        .then(response => {
          console.log(response.data);
          this.message = 'The event was updated successfully!';
        })
        .catch(e => {
          console.log(e);
        });
    },

    deleteEvent() {
      EventDataService.delete(this.currentEvent.id)
        .then(response => {
          console.log(response.data);
          this.$router.push({ name: "events" });
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.message = '';
    this.getEvent(this.$route.params.id);
  }
};
</script>

<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>