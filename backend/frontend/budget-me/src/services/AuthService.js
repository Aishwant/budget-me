import http from '@http-common';

class AuthService{
    register(payload){
        return http.post("/register", payload);
    }
}