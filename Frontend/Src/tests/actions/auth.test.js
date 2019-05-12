import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';
import axios from '../../util/axios';
import MockAdapter from 'axios-mock-adapter';

import { signup, clearSignup, login, clearLogin } from '../../actions/auth';
import { SIGNUP_SUCCESS,
    SIGNUP_FAIL,
    CLEAR_SIGNUP,
    USER_LOGGED_IN,
    INVALID_LOGIN_CREDENTIALS,
    CLEAR_LOGIN
} from '../../constants';

const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);
const baseUrl = process.env.BASE_API_URL;
const mockAxios = new MockAdapter(axios);

describe('Auth-Actions Test suite', () => {
    let store;
    beforeEach(() => {
        store = mockStore({});
    });

    afterEach(() => {
        mockAxios.reset();
    });

    // This test should be calling axios with the right user data
    // and dispatching the SIGNUP_SUCCESS action with valid user
    it('Should get right response with valid data', () => {
        const user = {
            username: 'bensi94',
            password: 'testpass',
            name: 'Benedikt Oskarsson'
        };

        const responseObj = {
            username: user.username,
            name: user.name
        };

        mockAxios
            .onPost(`${baseUrl}/api/user/create/`)
            .reply(201, JSON.stringify(responseObj));

        // By returning the promise we let jest know that the promise
        // needs to be resolved  before going to the next one
        return store.dispatch(signup(user)).then(() => {
            expect(store.getActions()[0].type).toBe(SIGNUP_SUCCESS);
            expect(store.getActions()[0].payload).toEqual(responseObj);
            expect(JSON.parse(mockAxios.history.post[0].data)).toEqual(user);
        });
    });

    // This test should be calling axios with user data but
    // getting SIGNUP_FAIL action back with error data
    it('Should get error response on invalid data', () => {
        const user = {
            username: '',
            password: '',
            name: ''
        };

        const responseObj = {
            username: [
                "This field may not be blank."
            ],
            password: [
                "This field may not be blank."
            ],
            name: [
                "This field may not be blank."
            ]
        };

        mockAxios
            .onPost(`${baseUrl}/api/user/create/`)
            .reply(400, JSON.stringify(responseObj));

        // By returning the promise we let jest know that the promise
        // needs to be resolved  before going to the next one
        return store.dispatch(signup(user)).then(() => {
            expect(store.getActions()[0].type).toBe(SIGNUP_FAIL);
            expect(store.getActions()[0].payload).toEqual(responseObj);
            expect(JSON.parse(mockAxios.history.post[0].data)).toEqual(user);
        });
    });

    it('Should not be able to create the same user twice', () => {
        const user = {
            username: 'bensi94',
            password: 'testpass',
            name: 'Benedikt Oskarsson'
        };

        const responseObj = {
            username: [
                "user with this username already exists."
            ]
        };

        mockAxios
            .onPost(`${baseUrl}/api/user/create/`)
            .reply(400, JSON.stringify(responseObj));

        // By returning the promise we let jest know that the promise
        // needs to be resolved  before going to the next one
        return store.dispatch(signup(user)).then(() => {
            store.dispatch(signup(user));
        }).then(() => {
            expect(store.getActions()[0].type).toBe(SIGNUP_FAIL);
            expect(store.getActions()[0].payload).toEqual(responseObj);
            expect(JSON.parse(mockAxios.history.post[0].data)).toEqual(user);
            expect(JSON.parse(mockAxios.history.post[1].data)).toEqual(user);
        });
    });

    it('Should dispatch CLEAR_SIGNUP on clearSignup', () => {
        store.dispatch(clearSignup());
        expect(store.getActions()[0].type).toBe(CLEAR_SIGNUP);
    });

    it('Should get a token back on login', () => {
        const user = {
            username: 'bensi94',
            password: 'testpass'
        };

        const responseObj = {
            token: 'testtoken'
        };

        mockAxios
            .onPost(`${baseUrl}/api/user/token/`)
            .reply(200, JSON.stringify(responseObj));

        // By returning the promise we let jest know that the promise
        // needs to be resolved  before going to the next one
        return store.dispatch(login(user)).then(() => {
            expect(store.getActions()[0].type).toBe(USER_LOGGED_IN);
            expect(store.getActions()[0].payload).toEqual(responseObj);
            expect(JSON.parse(mockAxios.history.post[0].data)).toEqual(user);
            expect(mockAxios.axiosInstance.defaults.headers.common['Authorization']).toBe('Token testtoken');
        });
    });

    it('Should get unable to authenticate if invalid', () => {
        const user = {
            username: 'wronguser',
            password: 'wrongPassword'
        };

        const responseObj = {
            non_field_errors: [
                "Unable to authenticate with provided credentails"
            ]
        };

        mockAxios
            .onPost(`${baseUrl}/api/user/token/`)
            .reply(400, JSON.stringify(responseObj));

        // By returning the promise we let jest know that the promise
        // needs to be resolved  before going to the next one
        return store.dispatch(login(user)).then(() => {
            expect(store.getActions()[0].type).toBe(INVALID_LOGIN_CREDENTIALS);
            expect(JSON.parse(mockAxios.history.post[0].data)).toEqual(user);
        });
    });

    it('Should clear login on clear login', () => {
        store.dispatch(clearLogin());
        expect(store.getActions()[0].type).toBe(CLEAR_LOGIN);
        expect(mockAxios.axiosInstance.defaults.headers.common['Authorization']).toBe(undefined);
    });
});
