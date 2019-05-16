import io from '../../node_modules/socket.io-client/dist/socket.io.slim';

import { SOCKET_CREATED } from '../constants';
import { playerList } from './tables';

export const initSocket = (table, tokenString, store) => {
    const socket = io(`${process.env.BASE_WS_URL}/${table}`, {
        extraHeaders: {
            Authorization: tokenString
        }
    });

    socket.on('player_list', (list) => {
        store.dispatch(playerList(list, table));
    });

    return {
        type: SOCKET_CREATED,
        payload: {
            table,
            socket
        }
    };
};
