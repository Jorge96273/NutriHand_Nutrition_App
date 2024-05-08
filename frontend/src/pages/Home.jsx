import React from "react";
import { Card } from 'react-bootstrap';
import Carousel from "react-bootstrap/Carousel";
import { Link } from 'react-router-dom';
import '../styles/Home.css';


function Home() {
    return (
        <body className="body">
        <div className="home">
        <h1>Home</h1>
        <div className="carr">
        <Carousel>
            <Carousel.Item className="carousel-item">
                <h3 style={{color: 'gray'}}>Welcome to NutriHand</h3>
            </Carousel.Item>
            <Carousel.Item className="carousel-item">
                <h3 style={{color: 'gray'}}>Search Recipes?</h3>
            </Carousel.Item>
            <Carousel.Item className="carousel-item">
                <h3 style={{color: 'gray'}}>Search Foods?</h3>
            </Carousel.Item>
        </Carousel>
        </div>
        <nav>
            <Link to="../recipe/" className="link-button">Recipe</Link>
            <Link to="../food/" className="link-button">Food</Link>
            <Link to="../trolley/" className="link-button">Trolley</Link>
        </nav>
    </div>
    </body>
        
    );
}

export default Home