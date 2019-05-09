import authReducer from '../../reducers/auth';
import { SIGNUP_SUCCESS, SIGNUP_FAIL } from '../../constants';

describe('Auth-Reducers Test suite', () => {
    it('Should add signed up user to store', () => {
        const payload = {
            username: 'bensi94',
            name: 'Benedikt Oskarsson'
        };

        const action = {
            type: SIGNUP_SUCCESS,
            payload: payload
        };

        const state = authReducer({}, action);
        expect(state).toMatchObject(payload);
    });

    it('Should give correct error object if user exists', () => {
        const payload = {
            username: [
                "user with this username already exists."
            ]
        };

        const action = {
            type: SIGNUP_FAIL,
            payload: payload
        };

        const state = authReducer({}, action);
        expect(state).toMatchObject(payload);
    });
});