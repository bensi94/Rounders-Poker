// Dependencies
import React from 'react';
import { Menu } from 'element-react';
import { NavLink } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import { clearLogin } from '../actions/auth';
import { checkUser } from '../actions/user';


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
        if (this.props.isAuthenticated) {
            return (
                <Menu className="navBar" mode="horizontal" theme="dark">
                    <NavLink exact to="/table/1"
                        className="navlink"
                        activeClassName="active-navlink"
                        isActive={this.updateIsActive}
                    >
                        <Menu.Item index="1">
                            Rounders Poker
                        </Menu.Item>
                    </NavLink>
                    <NavLink exact to="/"
                        className="navlink"
                        activeClassName="active-navlink"
                        isActive={this.updateIsActive}
                        onClick={() => {
                            this.props.logOut();
                            this.props.checkUser();
                        }}
                    >
                        <Menu.Item className="right-item" index="2">
                            Log out
                        </Menu.Item>
                    </NavLink>
                </Menu>
            );
        } else {
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
}

Navbar.propTypes = {
    active: PropTypes.string.isRequired,
    isAuthenticated: PropTypes.bool.isRequired,
    logOut: PropTypes.func.isRequired,
    checkUser: PropTypes.func.isRequired
};

const mapStateToProps = (state) => {
    return {
        active: state.router.location.pathname,
        isAuthenticated: state.user.isAuthenticated
    };
};

const mapDispatchToProps = (dispatch) => ({
    logOut: () => dispatch(clearLogin()),
    checkUser: () => dispatch(checkUser())
});

export default connect(mapStateToProps, mapDispatchToProps)(Navbar);
