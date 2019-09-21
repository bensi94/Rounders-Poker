// Dependencies
import React from 'react';
import { Route, Switch } from 'react-router';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { Loading } from 'element-react';


// Project files
import FrontPage from './FrontPage';
import Login from './Login';
import Signup from './Signup';
import Navbar from './Navbar';
import Game from './Game';
import PrivateRoute from '../routers/PrivateRoute';
import PublicRoute from '../routers/PublicRoute';
import { checkUser } from '../actions/user';


export class Header extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        let page;
        if (this.props.isAuthenticated === undefined ||
            (this.props.isAuthenticated && !this.props.token)) {
            page = <Loading fullscreen/>;
            this.props.checkUser();
        } else {
            page = (
                <React.Fragment>
                    <Navbar />
                    <Switch>
                        <Route exact path="/" component={FrontPage} />
                        <PublicRoute exact path="/login" component={Login} />
                        <PublicRoute exact path="/signup" component={Signup} />
                        <PrivateRoute exact path="/table/:tableID" component={Game} />
                        <Route component={FrontPage} />
                    </Switch>
                </React.Fragment>
            );
        }
        return (
            { ...page }
        );
    }
}

Header.propTypes = {
    username: PropTypes.string,
    name: PropTypes.string,
    isAuthenticated: PropTypes.bool,
    token: PropTypes.string,
    error: PropTypes.shape({
        detail: PropTypes.string
    }),
    checkUser: PropTypes.func.isRequired
};

const mapStateToProps = (state) => {
    return {
        username: state.user.username,
        name: state.user.name,
        isAuthenticated: state.user.isAuthenticated,
        token: state.auth.token,
        error: state.user.error
    };
};

const mapDispatchToProps = (dispatch) => ({
    checkUser: () => dispatch(checkUser())
});

export default connect(mapStateToProps, mapDispatchToProps)(Header);
