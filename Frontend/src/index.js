// Dependencies
import React from 'react';
import ReactDOM from 'react-dom';
import 'element-theme-default';

// Project files
import './styles/main.less';
import Header from './components/Header';

const App = () => {
    return (
        <Header />
    );
};

ReactDOM.render(<App />, document.getElementById('root'));
