import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { createSocket } from '../actions/socket';

// Temp const should be replaced when we have multiple tables
const CURRENT_TABLE = 'GAME';

class Game extends React.Component {
    constructor(props) {
        super(props);
    }

    componentDidMount() {
        this.props.createSocket(CURRENT_TABLE, this.props.token);
    }

    render() {
        return <h1> Game </h1>;
    }
}

Game.propTypes = {
    createSocket: PropTypes.func.isRequired,
    token: PropTypes.string,
    players: PropTypes.arrayOf(PropTypes.shape({
        username: PropTypes.string
    }))
};

const mapStateToProps = (state) => {
    if (state.tables[CURRENT_TABLE]) {
        return {
            players: state.tables[CURRENT_TABLE].players,
            token: state.auth.token
        };
    } else {
        return {
            token: state.auth.token
        };
    }
};

const mapDispatchToProps = (dispatch) => ({
    createSocket: (table, token) => dispatch(createSocket(table, token))
});


export default connect(mapStateToProps, mapDispatchToProps)(Game);
