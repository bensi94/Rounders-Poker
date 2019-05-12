import { combineReducers } from 'redux';
import { connectRouter } from 'connected-react-router';


import auth from './auth';
import user from './user';

export default (history) => combineReducers({
    router: connectRouter(history),
    auth,
    user
});
