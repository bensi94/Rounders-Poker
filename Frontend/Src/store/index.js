import { createStore, applyMiddleware } from 'redux';
import { routerMiddleware } from 'connected-react-router';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';

import rootReducer from '../reducers';
import history from '../util/history';

const initialState = {};


const middleware = [thunk];

const store = createStore(
    rootReducer(history),
    initialState,
    composeWithDevTools(applyMiddleware(routerMiddleware(history), ...middleware))
);

export default store;
