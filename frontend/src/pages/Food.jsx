import React, { useState, useEffect } from "react";
import Form from "../components/Form"
import axios from 'axios';
import Row from "react-bootstrap/Row"

const FoodSearch = () => {
    const [foodList, setFoodList] = useState([]);

    useEffect(() => {
        const getFood = async (food) => {
            console.log('getFood');
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/v1/food/search_food/apple/`);
                console.log(response.data)
                setFoodList(response.data)
            }
            catch (err) {
                console.log(err.message)
            }
        };
        getFood();
    }, []);



    return (
        <Row>
            <h2>Food</h2>
            <ul>
                {foodList.map((food, index) =>
                    <li key={index}>
                        <strong>{food.name}</strong>
                        <p>Calories: {food.caloric}</p>
                        <p>Protein: {food.protein}</p>
                        <p>Fat: {food.fat}</p>
                        </li>
                )}
            </ul>

        </Row>
    )
}

export default FoodSearch

// {
//     "dishes": [
//         {
//             "id": "2410",
//             "name": "Apple",
//             "caloric": "52",
//             "type": "x",
//             "fat": "0.17",
//             "carbon": "13.8",
//             "protein": "0.26",
//             "category_id": "500"
//         },