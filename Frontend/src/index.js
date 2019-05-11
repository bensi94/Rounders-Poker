// Dependencies
import React from 'react';
import ReactDOM from 'react-dom';
import 'element-theme-default';
import { ConnectedRouter } from 'connected-react-router';
import { Provider } from 'react-redux';

// Project files
import './styles/main.less';
import Header from './components/Header';
import store from './store';
import history from './util/history';


const App = () => {
    return (
        <Provider store={store}>
            <ConnectedRouter history={history}>
                <Header />
            </ConnectedRouter>
        </Provider>
    );
};

ReactDOM.render(<App />, document.getElementById('root'));
