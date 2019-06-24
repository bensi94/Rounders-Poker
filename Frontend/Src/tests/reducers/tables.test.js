import tablesReducer from '../../reducers/tables';
import { WEBSOCKET_MESSAGE } from '@giantmachines/redux-websocket';

describe('Tables-Reducers Test suite', () => {
    it('Should change the message to the store state', () => {
        const prefix = 'GAME';

        const message = {
            players: {
                bensi94: {
                    stack: 6,
                    bet: 0,
                    status: 'ACTIVE'
                }
            }
        };

        const action = {
            type: prefix + '::' + WEBSOCKET_MESSAGE,
            payload: {
                message: JSON.stringify(message)
            }
        };
        const state = tablesReducer({}, action);

        const responseObj = {
            [prefix]: message
        };

        expect(state).toEqual(responseObj);
    });
});
