import socketsReducer from '../../reducers/sockets';
import { WEBSOCKET_CONNECT, WEBSOCKET_OPEN } from '@giantmachines/redux-websocket';

describe('Socket-Reducers Test suite', () => {
    it('Should put url in redux store', () => {
        const table = 'TEST_TABLE';
        const url = `${process.env.BASE_WS_URL}/${table}`;
        const action = {
            type: `${table}::${WEBSOCKET_CONNECT}`,
            payload: {
                url
            }
        };

        const state = socketsReducer({}, action);
        expect(state).toEqual({
            [table]: {
                url
            }
        });
    });

    it('Should add second socket to the store when its created', () => {
        const table1 = 'TEST_TABLE';
        const table2 = 'TEST_TABLE2';

        const url = `${process.env.BASE_WS_URL}/${table1}`;
        const url2 = `${process.env.BASE_WS_URL}/${table2}`;

        const action = {
            type: `${table2}::${WEBSOCKET_CONNECT}`,
            payload: {
                url: url2,
                table: table2
            }
        };

        const state = socketsReducer({
            [table1]: {
                url,
                open: true
            }
        }, action);

        expect(state).toEqual({
            [table1]: {
                url,
                open: true
            },
            [table2]: {
                url: url2
            }
        });
    });

    it('Should set socket open when it opens', () => {
        const table = 'TEST_TABLE';
        const url = `${process.env.BASE_WS_URL}/${table}`;
        const action = {
            type: `${table}::${WEBSOCKET_OPEN}`
        };

        const state = socketsReducer({
            [table]: {
                url
            }
        }, action);

        expect(state).toEqual({
            [table]: {
                url,
                open: true
            }
        });
    });
});
