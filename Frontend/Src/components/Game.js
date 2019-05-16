import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import SocketIOClient from 'socket.io-client';

SocketIOClient('bla');

// import store from '../store';
// import { initSocket } from '../actions/socket';

// Temp const should be replaced when we have multiple tables
const CURRENT_TABLE = 'game';

class Game extends React.Component {
    constructor(props) {
        super(props);
    }

    componentDidMount() {
        // this.props.initSocket(CURRENT_TABLE, this.props.tokenString, store)
    }

    render() {
        return <h1> Game </h1>;
    }
}

Game.propTypes = {
    initSocket: PropTypes.func.isRequired,
    tokenString: PropTypes.string.isRequired,
    players: PropTypes.arrayOf(PropTypes.shape({
        username: PropTypes.string
    }))
};

const mapStateToProps = (state) => {
    return {
        players: state.tables[CURRENT_TABLE].players,
        tokenString: `Token ${state.auth.token}`
    };
};

const mapDispatchToProps = (dispatch) => ({
    // initSocket: (table, tokenString, store) =>
    //     dispatch(initSocket(table, tokenString, store))
});


export default connect(mapStateToProps, mapDispatchToProps)(Game);
