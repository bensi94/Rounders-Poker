import { SIGNUP_SUCCESS, SIGNUP_FAIL, CLEAR_SIGNUP } from '../constants';

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
        default: return state;
    }
};
