// Dependencies
import React from 'react';
import { Menu } from 'element-react';
import { Link } from 'react-router-dom';


const Navbar = () => {
    return (
        <Menu className="navBar" mode="horizontal" theme="dark">
            <Menu.Item index="1">
                <Link to="/">
                    Rounders Poker
                </Link>
            </Menu.Item>
            <Menu.Item className="right-item" index="2">
                <Link to="/login">
                    Log In
                </Link>
            </Menu.Item>
            <Menu.Item className="right-item" index="3">
                <Link to="/signup">
                    Sign up
                </Link>
            </Menu.Item>
        </Menu>
    );
};


export default Navbar;
