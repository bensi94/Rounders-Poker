import {
    SET_AUTHENTICATED_USER,
    SET_AUTHENTICATION_ERROR,
    SET_UNAUTHENTICATED_USER
} from '../constants';

export default (state = {}, action) => {
    switch (action.type) {
        case SET_AUTHENTICATED_USER:
            return {
                ...action.payload,
                isAuthenticated: true
            };
        case SET_AUTHENTICATION_ERROR:
            return {
                error: {
                    ...action.payload
                }
            };
        case SET_UNAUTHENTICATED_USER:
            return {
                isAuthenticated: false
            };
        default: return state;
    }
};
