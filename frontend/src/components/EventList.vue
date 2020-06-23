<template>
  <div class="list row">
    <div class="col-md-8">
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Search by title"
          v-model="event_title"/>
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" type="button"
            @click="searchTitle"
          >
            Search
          </button>
        </div>
      </div>
    </div>
    <div class="col-md-6">
      <h4>Events List</h4>
      <ul class="list-group">
        <li class="list-group-item"
          :class="{ active: index == currentIndex }"
          v-for="(event, index) in events"
          :key="index"
          @click="setActiveEvent(event, index)"
        >
          {{ event.event_title }}
        </li>
      </ul>

      <button class="m-3 btn btn-sm btn-danger" @click="removeAllEvents">
        Remove All
      </button>
    </div>
    <div class="col-md-6">
      <div v-if="currentEvent">
        <h4>Event</h4>
        <div>
          <label><strong>Title:</strong></label> {{ currentEvent.event_title }}
        </div>
        <div>
          <label><strong>Description:</strong></label> {{ currentEvent.event_description }}
        </div>

        <a class="badge badge-warning"
          :href="'/events/' + currentEvent.id"
        >
          Edit
        </a>
      </div>
      <div v-else>
        <br />
        <p>Please click on a event...</p>
      </div>
    </div>
  </div>
</template>

<script>
import EventDataService from "../services/EventDataService";

export default {
  name: "events-list",
  data() {
    return {
      events: [],
      currentEvent: null,
      currentIndex: -1,
      event_title: ""
    };
  },
  methods: {
    retrieveEvents() {
      EventDataService.getAll()
        .then(response => {
          this.events = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },

    refreshList() {
      this.retrieveEvents();
      this.currentEvent = null;
      this.currentIndex = -1;
    },

    setActiveEvent(event, index) {
      this.currentEvent = event;
      this.currentIndex = index;
    },

    removeAllEvents() {
      EventDataService.deleteAll()
        .then(response => {
          console.log(response.data);
          this.refreshList();
        })
        .catch(e => {
          console.log(e);
        });
    },
    
    searchTitle() {
      EventDataService.findByTitle(this.title)
        .then(response => {
          this.events = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.retrieveevents();
  }
};
</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>