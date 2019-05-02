import React from 'react';
import { Menu } from 'element-react';

const Header = () => {
    return (
        <Menu className="navBar" mode="horizontal" theme="dark">
            <Menu.Item index="1">Rounders Poker</Menu.Item>
            <Menu.Item className="right-item" index="2">Log In</Menu.Item>
            <Menu.Item className="right-item" index="3">Sign up</Menu.Item>
        </Menu>
    );
};

export default Header;
