import { createBrowserRouter } from "react-router-dom";
import App from "./App.jsx";
import Login from "./pages/Login"
import Register from "./pages/Register"
import Home from "./pages/Home.jsx"
import NotFound from "./pages/NotFound"
import Recipe from "./pages/Recipe.jsx"
import Food from "./pages/Food.jsx"
import Trolley from "./pages/Trolley.jsx"
import SavedRecipes from "./components/SavedRecipes.jsx"
import ProtectedRoute from "./components/ProtectedRoute"
import { getInfo } from "./utilities.jsx";

function Logout() {
    localStorage.clear()
    return <Navigate to="/login" />
}

function RegisterAndLogout() {
    localStorage.clear()
    return <Register />
}

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [
            {
                index: true,
                element: <Home />,
            },
            {
                path: "home/",
                element: <Home /> ,
            },
            {
                path: "login/",
                element: <Login />
            },
            {
                path: "logout/",
                element: <ProtectedRoute element= {<Logout />}/>,
            },
            {
                path: "register/",
                element: <RegisterAndLogout />
            },
            {
                path: "trolley/",
                element: <Trolley />
            },
            {
                path: "recipe/",
                element: <Recipe />
            },
            {
                path: "savedrecipes/:nutrient",
                element: <SavedRecipes />
            },
            {
                path: "food/",
                element: <Food />
            },
            {
                path: "*",
                element: <NotFound />
            }

        ],
    },
]);

export default router;