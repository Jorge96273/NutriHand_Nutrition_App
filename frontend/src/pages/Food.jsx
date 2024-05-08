import React, { useState, useEffect } from "react";
import Form from "../components/Form"
import axios from 'axios';
import Row from "react-bootstrap/Row"
import { Link } from 'react-router-dom';
import '../styles/Food.css'
import { addRecipeToCart, removeRecipeFromCart } from '../utilities'
import { addFoodToCart, removeFoodFromCart } from '../utilities'


const NutrientSearch = () => {
    const [foodList, setFoodList] = useState([]);
    const [food, setFood] = useState('')
    const [searchTerm, setSearchTerm] = useState('')
    const [btnStates, setBtnStates] = useState({});



    const handleInputChange = (e) => {
        setSearchTerm(e.target.value);
    }


    const getFood = async () => {
        console.log('getFood');
        try {
            let token = localStorage.getItem("token")
            const response = await axios.get(`http://127.0.0.1:8000/api/v1/food/search_food/${food}/`, {
                headers: {
                    'Authorization': `Token ${token}`
                }
            });
            setFoodList(response.data);

            console.log('gotFood!')
        } catch (err) {
            console.log(err.message);
        }
    };

    useEffect(() => {
        if (food) {
            getFood();
        }
    }, [food]);


    const handleSubmit = (e) => {
        e.preventDefault();
        setFood(searchTerm);

    };


    const toggleButtonState = (id, foodName) => {
        console.log("recipe ID, recipe Name ", id, foodName)
        console.log("button state ", btnStates[id])
        if (btnStates[id] === undefined || btnStates[id] === 'Cart?') {
            addFoodToCart(foodName)
    removeFoodFromCart   } else if (btnStates[id] === 'Added!') {
            removeFoodFromCart(foodName)
        }

        setBtnStates(prevState => ({
            ...prevState,
            [id]: prevState[id] === 'Added!' ? 'Cart?' : 'Added!'
        }));
    };

    return (
        <div className="recipe-container">
            <h2>Seach Product</h2>
            <div className="recipe-search">
                <form onSubmit={handleSubmit}>

                    <input
                        type="text"
                        placeholder="Product"
                        value={searchTerm}
                        onChange={handleInputChange}
                        className="search-input"
                    />

                    <button type="submit">Search</button>

                </form>
            </div>
            <ul className="recipe-list">
                {foodList.map((food, index) =>
                    <li key={index} className="recipe-item">
                        <Link to={`/recipe/${food}`} className="recipe-title"><strong>{food.Title}</strong></Link>
                        <img src={food.image} alt={food.Title + " image"} className="recipe-image" />
                        <p>ID: {food.id}</p>
                        <button onClick={() => toggleButtonState(food.id, food.Title)}>
                            {btnStates[food.id] || 'Cart?'}</button>
                    </li>

                )}
            </ul>
        </div>
    );
};


export default NutrientSearch