import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { createSocket } from '../actions/socket';

// Temp const should be replaced when we have multiple tables
const CURRENT_TABLE = 'game';

class Game extends React.Component {
    constructor(props) {
        super(props);
    }

    componentDidMount() {
        this.props.createSocket(CURRENT_TABLE);
    }

    render() {
        return <h1> Game </h1>;
    }
}

Game.propTypes = {
    createSocket: PropTypes.func.isRequired,
    tokenString: PropTypes.string.isRequired,
    players: PropTypes.arrayOf(PropTypes.shape({
        username: PropTypes.string
    }))
};

const mapStateToProps = (state) => {
    if (state.tables[CURRENT_TABLE]) {
        return {
            players: state.tables[CURRENT_TABLE].players,
            tokenString: `Token ${state.auth.token}`
        };
    } else {
        return {
            tokenString: `Token ${state.auth.token}`
        };
    }
};

const mapDispatchToProps = (dispatch) => ({
    createSocket: (table) => dispatch(createSocket(table))
});


export default connect(mapStateToProps, mapDispatchToProps)(Game);
