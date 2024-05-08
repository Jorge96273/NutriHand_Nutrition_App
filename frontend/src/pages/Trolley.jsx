import React, { useState, useEffect } from "react";
import axios from 'axios';
import '../styles/Recipe.css'

const TrolleyItems = () => {
    const [trolleyList, setTrolleyList] = useState([]);
    

    const getRecipe = async () => {
        console.log('getRecipe');
        try {
            let token = localStorage.getItem("token")
            const response = await axios.get(`http://127.0.0.1:8000/api/v1/trolley/`,{
                headers:{
                    'Authorization': `Token ${token}`
                }
            });

            setTrolleyList(response.data);
            console.log(response.data)

        } catch (err) {
            console.log(err.message);
        }
    };

    useEffect(() => {
        if (trolleyList) {
            getRecipe();
            console.log(trolleyList)

        }
    }, []);


    return (
        <div className="recipe-container">
            <h2>Trolley</h2>
            
            <ul className="recipe-list">
                {trolleyList.map((item, index) =>
                    <li key={index} className="recipe-item">
                        <p>{item}</p>
                    </li>

                )}
            </ul>
        </div>
    );
};


export default TrolleyItems