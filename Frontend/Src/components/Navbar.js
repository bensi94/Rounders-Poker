// Dependencies
import React from 'react';
import { Menu } from 'element-react';
import { NavLink } from 'react-router-dom';


class Navbar extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Menu className="navBar" mode="horizontal" theme="dark">
                <NavLink exact to="/" className="navlink" activeClassName="active-navlink">
                    <Menu.Item index="1">
                        Rounders Poker
                    </Menu.Item>
                </NavLink>
                <NavLink exact to="/login" className="navlink" activeClassName="active-navlink">
                    <Menu.Item className="right-item" index="2">
                        Login
                    </Menu.Item>
                </NavLink>
                <NavLink exact to="/signup" className="navlink" activeClassName="active-navlink">
                    <Menu.Item className="right-item" index="3">
                        Sign up
                    </Menu.Item>
                </NavLink>
            </Menu>
        );
    }
}


export default Navbar;
