import socketsReducer from '../../reducers/sockets';
import { SOCKET_CREATED } from '../../constants';
import { SocketIO as io } from 'mock-socket';

const table = 'testTable';


describe('Socket-Reducers Test suite', () => {
    const mockToken = 'Token testToken';

    it('Should put socket on a table in the redux store', () => {
        const socket = io(`${process.env.BASE_WS_URL}/${table}`, {
            extraHeaders: {
                Authorization: mockToken
            }
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
