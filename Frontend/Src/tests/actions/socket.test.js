import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';
import { WebSocket } from 'mock-socket';
import { createSocket } from '../../actions/socket';
import { WEBSOCKET_CONNECT } from '@giantmachines/redux-websocket';
import dynamicMiddlewares from 'redux-dynamic-middlewares';

const testTable = 'TEST_TABLE';
const middlewares = [thunk, dynamicMiddlewares];
const mockStore = configureMockStore(middlewares);
//const mockServer = new Server(`${process.env.BASE_WS_URL}/${testTable}`);

describe('Socket-actions Test suite', () => {
    let store;
    global.WebSocket = WebSocket;

    beforeEach(() => {
        store = mockStore({});
    });

    it('Should create and open socket correctly', () => {
        const mockToken = 'mockToken';
        let url = `${process.env.BASE_WS_URL}/ws/${testTable}/?Token=${mockToken}`;
        store.dispatch(createSocket(testTable, mockToken));
        expect(store.getActions()[0].type).toBe(`${testTable}::${WEBSOCKET_CONNECT}`);
        expect(store.getActions()[0].payload.url).toEqual(url);
    });
});
