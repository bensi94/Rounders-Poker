import authReducer from '../../reducers/auth';
import {
    SIGNUP_SUCCESS,
    SIGNUP_FAIL,
    CLEAR_SIGNUP,
    USER_LOGGED_IN,
    INVALID_LOGIN_CREDENTIALS
} from '../../constants';

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
                'user with this username already exists.'
            ]
        };

        const response = {
            error: {
                username: 'user with this username already exists.'
            }
        };

        const action = {
            type: SIGNUP_FAIL,
            payload: payload
        };

        const state = authReducer({}, action);
        expect(state).toMatchObject(response);
    });

    it('Should clear return cleared on CLEAR_SIGNUP', () => {
        const action = {
            type: CLEAR_SIGNUP
        };
        const state = authReducer({}, action);
        expect(state).toMatchObject({});
    });

    it('Should add token on login', () => {
        const payload = {
            token: 'testtoken'
        };
        const action = {
            type: USER_LOGGED_IN,
            payload: payload
        };

        const state = authReducer({}, action);
        expect(state).toMatchObject(payload);
    });

    it('Should return error and message on invalid credentials', () => {
        const action = {
            type: INVALID_LOGIN_CREDENTIALS
        };

        const response = {
            error: 'Could not log in with provided user credentials'
        };

        const state = authReducer({}, action);
        expect(state).toMatchObject(response);
    });
});
