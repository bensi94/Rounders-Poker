import userReducer from '../../reducers/user';

import {
    SET_AUTHENTICATED_USER,
    SET_AUTHENTICATION_ERROR,
    SET_UNAUTHENTICATED_USER
} from '../../constants';

describe('User-Reducer Test suite', () => {
    it('Should set user to full user object on valid ', () => {
        const action = {
            type: SET_AUTHENTICATED_USER,
            payload: {
                username: 'bensi94',
                name: 'Benedikt Oskarsson'
            }
        };

        const response = {
            username: 'bensi94',
            name: 'Benedikt Oskarsson',
            isAuthenticated: true
        };

        const state = userReducer({}, action);

        expect(state).toEqual(response);
    });

    it('Should set user to error state on auth error', () => {
        const action = {
            type: SET_AUTHENTICATION_ERROR,
            payload: {
                detail: 'Invalid token.'
            }
        };

        const response = {
            error: {
                detail: 'Invalid token.'
            }
        };

        const state = userReducer({}, action);

        expect(state).toEqual(response);
    });

    it('Should set to isAuthenticated false on unauthenticated ', () => {
        const action = {
            type: SET_UNAUTHENTICATED_USER
        };

        const response = {
            isAuthenticated: false
        };

        const state = userReducer({}, action);

        expect(state).toEqual(response);
    });
});
