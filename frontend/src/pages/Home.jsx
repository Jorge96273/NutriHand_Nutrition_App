import React from "react";
import { Card } from 'react-bootstrap';
import Carousel from "react-bootstrap/Carousel";
// import foodpicone from "../assets/foodpicone.jpeg";
// import foodpic2 from "../assets/foodpicone.jpeg";
import { useNavigate } from "react-router-dom";
import { Link } from 'react-router-dom';

function Home() {
    const navigate = useNavigate();
    return (
        <body className="home">
        <h1>Home</h1>
            <div>
                <Carousel>
                    <Carousel.Item>
                        <foodpicone text="First slide"/>
                            <h3>Welcome to NutriHand</h3>
                    </Carousel.Item>
                    <Carousel.Item>
                        <foodpic2 text="Second slide" />
                            <h3>Search Recipes?</h3>
                    </Carousel.Item>
                    <Carousel.Item>
                            <h3>Search Foods?</h3>
                    </Carousel.Item>
                </Carousel>
            </div>
            <div>
                <Link to="../recipeandfood/" style={{ color: 'blue', textDecoration: 'none', marginRight: '10px', fontSize: '16px', padding: '0px 10px', border: '1px solid blue', borderRadius: '5px' }}>Recipe</Link>
            </div>
            <div>
                <Link to="../food/" style={{ color: 'blue', textDecoration: 'none', marginRight: '10px', fontSize: '16px', padding: '0px 10px', border: '1px solid blue', borderRadius: '5px' }}>food</Link>
            </div>
        </body>
        
    );
}

export default Home