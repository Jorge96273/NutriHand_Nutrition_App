import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link, useParams } from 'react-router-dom';

const SavedRecipes = () => {
    const [recipes, setRecipes] = useState([]);


    const { nutrient } = useParams()


    useEffect(() => {
        const fetchRecipes = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/v1/recipe');
                setRecipes(response.data);
            } catch (error) {
                console.error('Error fetching saved recipes:', error);
            }
        };

        fetchRecipes();
    }, []);

    return (
        <div>
            <h1>Saved Recipes</h1>
            <ul>
                {recipes.map(recipe => (
                    <li key={recipe.id}>
                        <Link to={`/recipe/${recipe.id}`}>
                            <strong>{recipe.title}</strong>
                        </Link>
                        <p>{recipe.description}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default SavedRecipes;