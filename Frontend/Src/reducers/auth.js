import { SIGNUP_SUCCESS, SIGNUP_FAIL } from '../constants';

export default (state = {}, action) => {
    switch (action.type) {
        case SIGNUP_SUCCESS: return action.payload;
        case SIGNUP_FAIL: return action.payload;
        default: return state;
    }
};
