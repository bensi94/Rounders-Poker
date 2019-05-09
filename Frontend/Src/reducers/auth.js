import { SIGNUP_SUCCESS, SIGNUP_FAIL } from '../constants';

const initialState = {
    signupSucess: {},
    singupFail: {}
};

export default (state = initialState, action) => {
    switch (action.type) {
        case SIGNUP_SUCCESS: return action.payload;
        case SIGNUP_FAIL: return action.payload;
        default: return state;
    }
};
