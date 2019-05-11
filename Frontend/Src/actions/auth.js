import axios from '../util/axios';
import { SIGNUP_SUCCESS,
    SIGNUP_FAIL,
    CLEAR_SIGNUP,
    USER_LOGGED_IN,
    INVALID_LOGIN_CREDENTIALS,
    CLEAR_LOGIN
} from '../constants';

export const signup = (user) => {
    const body = JSON.stringify(user);
    return (dispatch) => {
        return axios.post('/api/user/create/', body)
            .then(res => {
                dispatch({
                    type: SIGNUP_SUCCESS,
                    payload: res.data
                });
            })
            .catch(err => {
                dispatch({
                    type: SIGNUP_FAIL,
                    payload: err.response.data
                });
            });
    };
};

export const clearSignup = () => {
    return {
        type: CLEAR_SIGNUP
    };
};

export const login = (user) => {
    const body = JSON.stringify(user);
    return (dispatch) => {
        return axios.post('/api/user/token/', body)
            .then(res => {
                dispatch({
                    type: USER_LOGGED_IN,
                    payload: res.data
                });
            })
            .catch(err => {
                const invalidLoginCredentials = {
                    non_field_errors: [
                        'Unable to authenticate with provided credentails'
                    ]
                };

                if (JSON.stringify(err.response.data) === JSON.stringify(invalidLoginCredentials)) {
                    dispatch({
                        type: INVALID_LOGIN_CREDENTIALS
                    });
                }
            });
    };
};

export const clearLogin = () => {
    return {
        type: CLEAR_LOGIN
    };
};
