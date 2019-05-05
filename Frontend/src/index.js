// Dependencies
import React from 'react';
import ReactDOM from 'react-dom';
import 'element-theme-default';
import { BrowserRouter as Router } from 'react-router-dom';
import { Provider } from 'react-redux';

// Project files
import './styles/main.less';
import Header from './components/Header';
import store from './store';

const App = () => {
    return (
        <Provider store={store}>
            <Router>
                <Header />
            </Router>
        </Provider>
    );
};

ReactDOM.render(<App />, document.getElementById('root'));
