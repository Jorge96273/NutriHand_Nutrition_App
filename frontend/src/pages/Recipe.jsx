
import React, { useState, useEffect } from "react";
import Form from "../components/Form"
import axios from 'axios';
import Row from "react-bootstrap/Row"
import { Link } from 'react-router-dom';
import '../styles/Recipe.css'
import { addRecipeToCart, removeRecipeFromCart } from '../utilities'

const NutrientSearch=()=> {
    const[recipeList, setRecipeList]=useState([]);
    const[nutrient, setNutrient]=useState('')
    const [searchTerm, setSearchTerm] = useState('')
    const [btnStates, setBtnStates] = useState({});



    const handleInputChange = (e) => {
        setSearchTerm(e.target.value);
    }


    const getRecipe = async () => {
        console.log('getRecipe');
        try {
            const response = await axios.get(`http://127.0.0.1:8000/api/v1/recipe/search_nutrient/${nutrient}/`);
            setRecipeList(response.data);
            

        } catch (err) {
            console.log(err.message);
        }
    };

    useEffect(() => {
        if (nutrient) {
            getRecipe();
        }
    }, [nutrient]);
        

    const handleSubmit = (e) => {
        e.preventDefault();
        setNutrient(searchTerm);
        
    };


    const toggleButtonState = (id, recipeName) => {
        console.log("recipe ID, recipe Name ", id, recipeName)
        console.log("button state ", btnStates[id])
        if (btnStates[id] === undefined || btnStates[id] === 'Cart?') {
            addRecipeToCart(recipeName)
        } else if (btnStates[id] === 'Added!') {
            removeRecipeFromCart(recipeName)
        }

        setBtnStates(prevState => ({
            ...prevState,
            [id]: prevState[id] === 'Added!' ? 'Cart?' : 'Added!'
        }));
        
         
    };

    return (
        <div className="recipe-container">
            <h2>Seach Nutrient</h2>
            <div className="recipe-search">
                <form onSubmit={handleSubmit}>

                    <input
                        type="text"
                        placeholder="Nutrient"
                        value={searchTerm}
                        onChange={handleInputChange}
                        className="search-input"
                    />

                    <button type="submit">Search</button>

                </form>
            </div>
            <ul className="recipe-list">
                {recipeList.map((recipe, index) =>
                    <li key={index} className="recipe-item">
                        <Link to={`/recipe/${recipe}`} className="recipe-title"><strong>{recipe.Title}</strong></Link>
                        <img src={recipe.image} alt={recipe.Title + " image"} className="recipe-image" />
                        <p className="recipe-calories">Calories: {recipe.calories}</p>
                        <p>Protein: {recipe.protein}</p>
                        <p>Fat: {recipe.fat}</p>
                        <p>Carbs: {recipe.carbs}</p>
                        <p>Iron: {recipe.iron}</p>
                        <p>ID: {recipe.id}</p>
                        <button onClick={() => toggleButtonState(recipe.id, recipe.Title)}>
                        {btnStates[recipe.id] || 'Cart?'}</button>
                    </li>
                    
                )}
            </ul>
        </div>
    );
};


export default NutrientSearch
