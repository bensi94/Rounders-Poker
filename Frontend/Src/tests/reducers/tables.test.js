import tablesReducer from '../../reducers/tables';
import { PLAYER_LIST } from '../../constants';

const table = 'testTable';

describe('Tables-Reducers Test suite', () => {
    it('Should add created player to the correct table', () => {
        const list = [{
            username: 'bensi94'
        }];

        const action = {
            type: PLAYER_LIST,
            payload: {
                table,
                players: list
            }
        };
        const state = tablesReducer({}, action);

        const responseObj = {
            [table]: {
                players: list
            }
        };

        expect(state).toEqual(responseObj);
    });

    it('Should add a second table to the list', () => {
        const list = [{
            username: 'bensi94'
        }];

        const testTable2 = 'testTable2';

        const action = {
            type: PLAYER_LIST,
            payload: {
                table: testTable2,
                players: list
            }
        };
        const state = tablesReducer({
            [table]: {
                players: list
            }
        }, action);

        const responseObj = {
            [table]: {
                players: list
            },
            [testTable2]: {
                players: list
            }
        };

        expect(state).toEqual(responseObj);
    });

    it('Should add player to a list on current table', () => {
        const oldList = [{
            username: 'bensi94'
        }];

        const newList = [
            {
                username: 'bensi94'
            },
            {
                username: 'thorir'
            }
        ];

        const action = {
            type: PLAYER_LIST,
            payload: {
                table,
                players: newList
            }
        };

        const state = tablesReducer({
            [table]: {
                players: oldList
            }
        }, action);

        const responseObj = {
            [table]: {
                players: newList
            }
        };

        expect(state).toEqual(responseObj);
    });
});
