import axios from 'axios';
import { SIGNUP_SUCCESS, SIGNUP_FAIL } from '../constants';

const baseUrl = process.env.BASE_API_URL;

const config = {
    headers: {
        "Content-Type": "application/json"
    }
};

export const signup = (user) => {
    const body = JSON.stringify(user);
    return (dispatch) => {
        return axios.post(`${baseUrl}/api/user/create`, body, config)
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
