import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
import { Link } from "react-router-dom";
import { logOut } from "../utilities";

function NavBar({ user, setUser }) {
    return (
        <Navbar expand="lg" className="bg-body-tertiary">
            <Container fluid>
                <Navbar.Brand as={Link} to="/">
                    NutriHand
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="navbarScroll" />
                <Navbar.Collapse id="navbarScroll">
                    <Nav
                        className="me-auto my-2 my-lg-0"
                        style={{ color: 'blue', textDecoration: 'none', fontSize: '16px', padding: '5px 10px', border: '1px solid blue', borderRadius: '5px' }}
                        navbarScroll
                    >
                        
                            <Nav.Link as={Link} to={"/register/"}>
                                Register
                            </Nav.Link>
                            <>
                                <Nav.Link as={Link} to="/login/">
                                    Login
                                </Nav.Link>
                                <Button variant="tertiary" onClick={() => [logOut(), setUser(null)]}>
                                    Log Out
                                </Button>
                            </>
                    </Nav>
                    <Form className="d-flex">
                        <Form.Control
                            type="search"
                            placeholder="Search"
                            className="me-2"
                            aria-label="Search"
                        />
                        <Button variant="outline-success">Search</Button>
                    </Form>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default NavBar;