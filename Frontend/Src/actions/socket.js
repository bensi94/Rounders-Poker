import reduxWebsocket, { connect } from '@giantmachines/redux-websocket';
import { addMiddleware } from 'redux-dynamic-middlewares';

export const createSocket = (table, token) => {
    let url = `${process.env.BASE_WS_URL}/ws/${table}/?Token=${token}`;
    addMiddleware(
        reduxWebsocket({
            prefix: table
        })
    );

    return (dispatch) => {
        dispatch(connect(url, table));
    };
};
