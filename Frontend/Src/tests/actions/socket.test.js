import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';
import { Server } from 'mock-socket';

import { initSocket } from '../../actions/socket';
import { SOCKET_CREATED, PLAYER_LIST } from '../../constants';

const testTable = 'testTable';
const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);
const mockServer = new Server(`${process.env.BASE_WS_URL}/${testTable}`);

describe('Socket-actions Test suite', () => {
    let store;
    const mockToken = 'Token testToken';

    beforeEach(() => {
        store = mockStore({});
    });

    it('Should init socket correctly', () => {
        store.dispatch(initSocket(testTable, mockToken, store));
        expect(store.getActions()[0].type).toBe(SOCKET_CREATED);
        expect(store.getActions()[0].payload.table).toEqual(testTable);
    });

    it('Should dispatch player_list on player_list event', () => {
        const emitObj = [{
            username: 'bensi94'
        }];
        store.dispatch(initSocket(testTable, mockToken, store));

        mockServer.emit('player_list', JSON.stringify(emitObj));

        expect(store.getActions()[1].type).toBe(PLAYER_LIST);
        expect(store.getActions()[1].payload).toEqual(emitObj);
    });
});
