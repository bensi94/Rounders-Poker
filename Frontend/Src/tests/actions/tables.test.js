import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';

import { playerList } from '../../actions/tables';
import { PLAYER_LIST } from '../../constants';

const testTable = 'testTable';
const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);

describe('Tables-actions Test suite', () => {
    let store;

    beforeEach(() => {
        store = mockStore({});
    });

    it('Should return a valid player list on PLAYER_LIST', () => {
        const list = [{
            username: 'bensi94'
        }];

        const responseObj = {
            table: testTable,
            players: list
        };

        store.dispatch(playerList(JSON.stringify(list), testTable));
        expect(store.getActions()[0].type).toBe(PLAYER_LIST);
        expect(store.getActions()[0].payload).toEqual(responseObj);
    });
});
