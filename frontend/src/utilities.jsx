import axios from "axios";

export const api = axios.create({
    baseURL: import.meta.env.VITE_BASE_URL,
});

export const logIn = async (email, password, register) => {
    let response = await api.post(`users/${register ? "signup" : "login"}/`, {
        email: email,
        password: password,
    });
    if (response.status === 200 || response.status === 201) {
        let token = response.data.token;
        api.defaults.headers.common["Authorization"] = `Token ${token}`;
        localStorage.setItem("token", token);
        return response.data.user;
    } else {
        alert("Log In failed");
    }
};

export const logOut = async () => {
    let response = await api.post("users/logout/");
    if (response.status === 204) {
        localStorage.removeItem("token");
        delete api.defaults.headers.common["Authorization"];
        return null;
    }
    alert("log out failed");
};



export const getInfo = async () => {
    let token = localStorage.getItem("token");
    if (token) {
        api.defaults.headers.common["Authorization"] = `Token ${token}`;
        let response = await api.get("users/");
        return response.data.email;
    } else {
        return null;
    }
};
















// export const getAllTasks = async () => {
//     let response = await api.get("tasks/");
//     if (response.status) {
//         return response.data;
//     }
//     return [];
// };