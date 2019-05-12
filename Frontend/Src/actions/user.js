import {
    SET_AUTHENTICATED_USER,
    SET_AUTHENTICATION_ERROR,
    SET_UNAUTHENTICATED_USER,
    COOKIE_TOKEN_NAME
} from '../constants';
import axios, { setAuthorizationToken } from '../util/axios';
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
                })
                .catch(err => {
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
