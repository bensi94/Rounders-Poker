// Dependencies
import React from 'react';
import ReactDOM from 'react-dom';
import 'element-theme-default';
import { BrowserRouter as Router } from 'react-router-dom';

// Project files
import './styles/main.less';
import Header from './components/Header';

const App = () => {
    return (
        <Router>
            <Header />
        </Router>
    );
};

ReactDOM.render(<App />, document.getElementById('root'));
