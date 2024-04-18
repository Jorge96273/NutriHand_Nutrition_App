import React, { useState, useEffect } from "react";
import Form from "../components/Form"
import axios from 'axios';
import Row from "react-bootstrap/Row"

const NutrientSearch=()=> {
    const[recipeList, setRecipeList]=useState([]);
    const[searchTerm, setSearchTerm]=useState('')


    
    useEffect(() => {
        const getRecipe = async (nutrient) => {
            console.log('getRecipe');
            try{
                const response = await axios.get(`http://127.0.0.1:8000/api/v1/recipe/search_nutrient/Iron/`);
                console.log(response.data)
                setRecipeList(response.data)
            }
            catch(err){
              console.log(err.message)
            }
        };
        getRecipe();
    }, []);

        const handleClick = () => {
            console.log("hello")
        }
// Parenthesis envoke the function of handleClick. handleClick()
    return (
        <Row>
        <h2>Recipe</h2>
        <div>
        <input
            type="text"
            placeholder="Nutrient..."
        />
        <button onClick={handleClick} >Search</button>
        </div>
        <ul>
            {recipeList.map((recipe,index)=>
                <li key={index}>
                    <strong>{recipe.Title}</strong>
                    <img src={recipe.image} alt="  Image description" />
                    <p>Calories: {recipe.calories}</p>
                    <p>Protein: {recipe.protein}</p>
                    <p>Fat: {recipe.fat}</p>
                    <p>Carbs: {recipe.carbs}</p>
                    <p>Iron: {recipe.iron}</p>
                </li>
            )}
        </ul>
        
        </Row>
    )
}

export default NutrientSearch

// <button onClick = {()=> {}}