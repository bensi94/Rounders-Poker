import axios from '../util/axios';
import { SIGNUP_SUCCESS, SIGNUP_FAIL } from '../constants';

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
