import { PLAYER_LIST } from '../constants';

export default (state = {}, action) => {
    switch (action.type) {
        case PLAYER_LIST:
            return {
                ...state,
                [action.payload.table]: {
                    players: action.payload.players
                }
            };
        default:
            return state;
    }
};
