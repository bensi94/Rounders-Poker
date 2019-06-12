import reduxWebsocket, { connect } from '@giantmachines/redux-websocket';
import { addMiddleware } from 'redux-dynamic-middlewares';

export const createSocket = (table) => {
    let url = `${process.env.BASE_WS_URL}/ws/${table}`;
    addMiddleware(
        reduxWebsocket({
            prefix: table
        })
    );

    return (dispatch) => {
        dispatch(connect(url, table));
    };
};
