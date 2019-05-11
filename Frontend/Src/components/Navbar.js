// Dependencies
import React from 'react';
import { Menu } from 'element-react';
import { NavLink } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';


export class Navbar extends React.Component {
    constructor(props) {
        super(props);
        this.updateIsActive = this.updateIsActive.bind(this);
    }

    updateIsActive(match) {
        if (match && match.url === this.props.active) {
            return true;
        }
        return false;
    }

    render() {
        return (
            <Menu className="navBar" mode="horizontal" theme="dark">
                <NavLink exact to="/"
                    className="navlink"
                    activeClassName="active-navlink"
                    isActive={this.updateIsActive}
                >
                    <Menu.Item index="1">
                        Rounders Poker
                    </Menu.Item>
                </NavLink>
                <NavLink exact to="/login"
                    className="navlink"
                    activeClassName="active-navlink"
                    isActive={this.updateIsActive}
                >
                    <Menu.Item className="right-item" index="2">
                        Login
                    </Menu.Item>
                </NavLink>
                <NavLink exact to="/signup"
                    className="navlink"
                    activeClassName="active-navlink"
                    isActive={this.updateIsActive}
                >
                    <Menu.Item className="right-item" index="3">
                        Sign up
                    </Menu.Item>
                </NavLink>
            </Menu>
        );
    }
}

Navbar.propTypes = {
    active: PropTypes.string.isRequired
};

const mapStateToProps = (state) => {
    return {
        active: state.router.location.pathname
    };
};

export default connect(mapStateToProps)(Navbar);
