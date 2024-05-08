import { Navigate } from "react-router-dom";
import api from "../api";
import { useState, useEffect } from "react";

function ProtectedRoute({ children }) {
    const [isAuthorized, setIsAuthorized] = useState(null);

    useEffect(() => {
        checkSession().catch(() => setIsAuthorized(false));
    }, []);

    const checkSession = async () => {
        try {
            const res = await api.get("/api/check_session/");
            setIsAuthorized(res.status === 200);
        } catch (error) {
            console.log(error);
            setIsAuthorized(false);
        }
    };

    if (isAuthorized === null) {
        return <div>Loading...</div>;
    }

    return isAuthorized ? children : <Navigate to="/login" />;
}

export default ProtectedRoute;
