// Dependencies
import React from 'react';
import { Switch, Route } from 'react-router-dom';


// Project files
import FrontPage from './FrontPage';
import Login from './Login';
import Signup from './Signup';
import Navbar from './Navbar';


const Header = () => {
    return (
        <React.Fragment>
            <Navbar />
            <Switch>
                <Route exact path="/" component={FrontPage} />
                <Route exact path="/login" component={Login} />
                <Route exact path="/signup" component={Signup} />
                <Route component={FrontPage} />
            </Switch>
        </React.Fragment>
    );
};

export default Header;
