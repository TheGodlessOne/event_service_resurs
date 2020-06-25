<template>
  <div id="app">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <div class="navbar-nav mr-auto">
        <li class="nav-item">
          <a href="/events" class="nav-link">Events</a>
        </li>
        <li class="nav-item">
          <a href="/add" class="nav-link">Add</a>
        </li>
      </div>
    </nav>

    <div class="container mt-3">
      <router-view />
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import AddEvent from './components/AddEvent'
import EventList from './components/EventList'
import EventDetail from './components/EventDetail'

export default {
  name: 'App',
  components: {
    'add-event': AddEvent,
    'event-list': EventList,
    'event-detail': EventDetail
  }
}
</script>
