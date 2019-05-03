// Dependencies
import React from 'react';
import { Menu } from 'element-react';
import { Link } from 'react-router-dom';


const Navbar = () => {
    return (
        <Menu className="navBar" mode="horizontal" theme="dark">
            <Link to="/" className="navlink">
                <Menu.Item index="1">
                    Rounders Poker
                </Menu.Item>
            </Link>
            <Link to="/login" className="navlink">
                <Menu.Item className="right-item" index="2">
                    Log In
                </Menu.Item>
            </Link>
            <Link to="/signup" className="navlink">
                <Menu.Item className="right-item" index="3">
                    Sign up
                </Menu.Item>
            </Link>
        </Menu>
    );
};


export default Navbar;
