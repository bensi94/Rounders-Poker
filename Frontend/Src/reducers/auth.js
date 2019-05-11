import {
    SIGNUP_SUCCESS,
    SIGNUP_FAIL,
    CLEAR_SIGNUP,
    USER_LOGGED_IN,
    INVALID_LOGIN_CREDENTIALS,
    CLEAR_LOGIN
} from '../constants';

export default (state = {}, action) => {
    switch (action.type) {
        case SIGNUP_SUCCESS: return action.payload;
        case SIGNUP_FAIL:
            // Getting the errors that exist
            const username = action.payload.username ?
                action.payload.username.join(' ') : undefined;
            const name = action.payload.name ?
                action.payload.name.join(' ') : undefined;
            const password = action.payload.password ?
                action.payload.password.join(' ') : undefined;

            return { error: {
                username,
                name,
                password
            } };
        case CLEAR_SIGNUP: return {};
        case USER_LOGGED_IN: return action.payload;
        case INVALID_LOGIN_CREDENTIALS:
            return {
                error: 'Could not log in with provided user credentials'
            };
        case CLEAR_LOGIN: return {};
        default: return state;
    }
};
