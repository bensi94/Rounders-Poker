import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';
import axios from '../../util/axios';
import MockAdapter from 'axios-mock-adapter';
import Cookies from 'js-cookie';

import { checkUser } from '../../actions/user';
import {
    SET_AUTHENTICATED_USER,
    SET_AUTHENTICATION_ERROR,
    SET_UNAUTHENTICATED_USER
} from '../../constants';

const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);
const baseUrl = process.env.BASE_API_URL;
const mockAxios = new MockAdapter(axios);


describe('User-Actions Test suite', () => {
    let store;
    beforeEach(() => {
        store = mockStore({});
    });

    afterEach(() => {
        mockAxios.reset();
    });

    it('Should get valid response on checkUser ', () => {
        const responseObj = {
            username: 'bensi94',
            name: 'Benedikt Oskarsson'
        };

        mockAxios
            .onGet(`${baseUrl}/api/user/me/`)
            .reply(200, JSON.stringify(responseObj));

        Cookies.get = jest.fn(() => 'testcookie');

        // By returning the promise we let jest know that the promise
        // needs to be resolved  before going to the next one
        return store.dispatch(checkUser()).then(() => {
            expect(store.getActions()[0].type).toBe(SET_AUTHENTICATED_USER);
            expect(JSON.parse(mockAxios.handlers.get[0][4])).toMatchObject(responseObj);
        });
    });

    it('Should give error on invalid token', () => {
        const responseObj = {
            detail: 'Invalid token.'
        };

        mockAxios
            .onGet(`${baseUrl}/api/user/me/`)
            .reply(401, JSON.stringify(responseObj));

        Cookies.get = jest.fn(() => 'testcookie');

        return store.dispatch(checkUser()).then(() => {
            expect(store.getActions()[0].type).toBe(SET_AUTHENTICATION_ERROR);
            expect(JSON.parse(mockAxios.handlers.get[0][4])).toMatchObject(responseObj);
        });
    });

    it('Should give unauthorized on no token', () => {
        Cookies.get = jest.fn(() => '');
        store.dispatch(checkUser());
        expect(store.getActions()[0].type).toBe(SET_UNAUTHENTICATED_USER);
    });
});
