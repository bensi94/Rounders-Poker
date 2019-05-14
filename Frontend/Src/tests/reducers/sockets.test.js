import socketsReducer from '../../reducers/sockets';
import { SOCKET_CREATED, PLAYER_LIST } from '../../constants';
import { SocketIO as io } from 'mock-socket';
import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';

const table = 'testTable';
const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);

describe('Socket-Reducers Test suite', () => {
    let store;
    const mockToken = 'Token testToken';

    beforeEach(() => {
        store = mockStore({});
    });

    it('Should put socket on a table in the redux store', () => {
        const socket = io(`${process.env.BASE_WS_URL}/${table}`, {
            extraHeaders: {
                Authorization: mockToken
            }
        });

        socket.on('player_list', (list) => {
            store.dispatch({
                type: PLAYER_LIST,
                payload: {
                    table,
                    players: JSON.parse(list)
                }
            });
        });

        let action = {
            type: SOCKET_CREATED,
            payload: {
                table,
                socket
            }
        };

        const state = socketsReducer({}, action);
        expect(state).toEqual({
            [table]: socket
        });
    });

    it('Should add second socket to the store when its created', () => {
        const socket1 = io(`${process.env.BASE_WS_URL}/${table}`, {
            extraHeaders: {
                Authorization: mockToken
            }
        });

        const testTable2 = 'testTable2';

        const socket2 = io(`${process.env.BASE_WS_URL}/testTable2`, {
            extraHeaders: {
                Authorization: mockToken
            }
        });

        let action = {
            type: SOCKET_CREATED,
            payload: {
                table: testTable2,
                socket: socket2
            }
        };

        const state = socketsReducer({
            [table]: socket1
        }, action);

        expect(state).toEqual({
            [table]: socket1,
            [testTable2]: socket2
        });
    });
});
