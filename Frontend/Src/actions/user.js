import {
    SET_AUTHENTICATED_USER,
    SET_AUTHENTICATION_ERROR,
    SET_UNAUTHENTICATED_USER,
    USER_LOGGED_IN,
    COOKIE_TOKEN_NAME
} from '../constants';
import axios, { setAuthorizationToken, clearAuthorizationToken } from '../util/axios';
import Cookies from 'js-cookie';

export const checkUser = () => {
    const token = Cookies.get(COOKIE_TOKEN_NAME);
    if (token) {
        setAuthorizationToken(token);
        return (dispatch) => {
            return axios.get('/api/user/me/')
                .then(res => {
                    dispatch({
                        type: SET_AUTHENTICATED_USER,
                        payload: res.data
                    });
                    dispatch({
                        type: USER_LOGGED_IN,
                        payload: {
                            token
                        }
                    });
                })
                .catch(err => {
                    clearAuthorizationToken();
                    Cookies.remove(COOKIE_TOKEN_NAME);
                    dispatch({
                        type: SET_AUTHENTICATION_ERROR,
                        payload: err.response.data
                    });
                });
        };
    } else {
        return {
            type: SET_UNAUTHENTICATED_USER
        };
    }
};
