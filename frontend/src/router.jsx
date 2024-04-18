import { createBrowserRouter } from "react-router-dom";
import App from "./App.jsx";
import Login from "./pages/Login"
import Register from "./pages/Register"
import Home from "./pages/Home.jsx"
import NotFound from "./pages/NotFound"
import RecipeandFood from "./pages/RecipeandFood.jsx"
import Food from "./pages/Food.jsx"
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
        // loader: getInfo,
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
                element: <Logout />
            },
            {
                path: "register/",
                element: <RegisterAndLogout />
            },
            {
                path: "recipeandfood/",
                element: <RecipeandFood />
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