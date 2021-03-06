/* eslint-disable */
import Vue from "vue"
import Router from "vue-router"

Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      alias: "/events",
      name: "events",
      component: () => import("./components/EventList")
    },
    {
      path: "/events/:id",
      name: "event-details",
      component: () => import("./components/EventDetail")
    },
    {
      path: "/add",
      name: "add",
      component: () => import("./components/AddEvent")
    },
    {
      path: "/login",
      name: "login",
      component: () => import("./components/UserLogin")
    },
    {
      path: "/register",
      name: "register",
      component: () => import("./components/UserRegister")
    },
  ]
});