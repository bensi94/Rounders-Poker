import { PLAYER_LIST } from '../constants';

export const playerList = (list, table) => {
    return {
        type: PLAYER_LIST,
        payload: {
            table,
            players: JSON.parse(list)
        }
    };
};
