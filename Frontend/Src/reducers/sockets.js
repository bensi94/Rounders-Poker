import { SOCKET_CREATED } from '../constants';

export default (state = {}, action) => {
    switch (action.type) {
        case SOCKET_CREATED:
            return {
                ...state,
                [action.payload.table]: action.payload.socket
            };
        default: return state;
    }
};
