/* eslint-disable */
import http from "../http-common";

class UserDataService {
    create(data) {
        return http.post('/users', data);
    }

    delete(id) {
        return http.delete('/users/${id}');
    }
}