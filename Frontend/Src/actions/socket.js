import io from 'socket.io-client';

import { SOCKET_CREATED, PLAYER_LIST } from '../constants';

export const initSocket = (table, tokenString, store) => {
    const socket = io(`${process.env.BASE_WS_URL}/${table}`, {
        extraHeaders: {
            Authorization: tokenString
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

    return {
        type: SOCKET_CREATED,
        payload: {
            table,
            socket
        }
    };
};
