import { WEBSOCKET_MESSAGE } from '@giantmachines/redux-websocket';

export default (state = {}, action) => {
    let prefix = action.type.split('::')[0];
    switch (action.type) {
        case `${prefix}::${WEBSOCKET_MESSAGE}`:
            return {
                [prefix]: JSON.parse(action.payload.message)
            };
        default:
            return state;
    }
};
