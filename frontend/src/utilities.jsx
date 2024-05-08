import axios from "axios";

export const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL, 
});

export const logIn = async (username, password, register, route) => {
    
    console.log("LOGIN URL ", username, password)
    let response = await api.post(route, {
        username: username,
        password: password,
    });
    if (response.status === 200 || response.status === 201) {
        let token = response.data.token;
        console.log("CREATED TOKEN AFTER LOGIN", token)
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


export const addRecipeToCart = async (recipeName) => {
    let token = localStorage.getItem("token");
    if (token) {
        api.defaults.headers.common["Authorization"] = `Token ${token}`;
        let response = await api.post("api/v1/recipe/", {"recipe": recipeName})
        console.log(response)
    } else {
        return null;
    }

}


export const removeRecipeFromCart = async (recipeName) => {
    console.log("first")
    let token = localStorage.getItem("token");
    if (token) {
        console.log("second")
        console.log(typeof recipeName)
        api.defaults.headers.common["Authorization"] = `Token ${token}`;
        let response = await api.delete(`api/v1/recipe/${recipeName}/`)
        console.log(response)
    } else {
        console.log("third")
        return null;
    }
}


export const addFoodToCart = async (foodName) => {
    console.log("first")
    let token = localStorage.getItem("token");
    if (token) {
        console.log("second")
        api.defaults.headers.common["Authorization"] = `Token ${token}`;
        let response = await api.post("api/v1/food/", { "food": foodName })
        console.log(response)
    } else {
        console.log("third")
        return null;
    }

}


export const removeFoodFromCart = async (foodName) => {
    console.log("first")
    console.log(foodName)
    let token = localStorage.getItem("token");
    if (token) {
        console.log(foodName)
        console.log(typeof foodName)
        api.defaults.headers.common["Authorization"] = `Token ${token}`;
        console.log("BRUH")
        let response = await api.delete(`api/v1/food/${foodName}/`)
        console.log("BBBB")
        console.log(response)
    } else {
        console.log("third")
        return null;
    }
}







// export const getAllTasks = async () => {
//     let response = await api.get("tasks/");
//     if (response.status) {
//         return response.data;
//     }
//     return [];
// };