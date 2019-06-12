import { createStore, applyMiddleware } from 'redux';
import { routerMiddleware } from 'connected-react-router';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';
import dynamicMiddlewares from 'redux-dynamic-middlewares';

import rootReducer from '../reducers';
import history from '../util/history';

const initialState = {};
const middleware = [thunk, routerMiddleware(history), dynamicMiddlewares];

export const store = createStore(
    rootReducer(history),
    initialState,
    composeWithDevTools(applyMiddleware(...middleware))
);

export default store;
