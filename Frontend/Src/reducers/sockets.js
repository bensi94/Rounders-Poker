import {
    WEBSOCKET_CONNECT,
    WEBSOCKET_OPEN
} from '@giantmachines/redux-websocket';

export default (state = {}, action) => {
    let prefix = action.type.split('::')[0];
    switch (action.type) {
        case `${prefix}::${WEBSOCKET_CONNECT}`:
            return {
                ...state,
                [prefix]: {
                    url: action.payload.url
                }
            };
        case `${prefix}::${WEBSOCKET_OPEN}`:
            return {
                [prefix]: {
                    ...state[prefix],
                    open: true
                }
            };
        default: return state;
    }
};
