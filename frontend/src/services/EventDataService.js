/* eslint-disable */
import http from "../http-common";

class EventDataService {
  getAll() {
    return http.list('/events');
  }

  get(id) {
    return http.retrieve('/events/${id}');
  }

  create(data) {
    return http.create('/events', data);
  }

  update(id, data) {
    return http.update('/events/${id}', data);
  }

  delete(id) {
    return http.destroy('/events/${id}');
  }

  deleteAll() {
    return http.destroy('/events');
  }

}

export default new EventDataService();