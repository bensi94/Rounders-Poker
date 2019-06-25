import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { createSocket } from '../actions/socket';
import DemoTable from '../../assets/demo2.svg';


class Game extends React.Component {
    constructor(props) {
        super(props);
    }

    componentDidMount() {
        this.props.createSocket(this.props.tableID, this.props.token);
    }

    render() {
        return (
            <>
                <h1> Game </h1>
                { this.props.players && Object.keys(this.props.players).map((key) => {
                    return <div key={key}>{key}</div>;
                })}
                <DemoTable className="demo-table" width={1000}/>
            </>
        );
    }
}

Game.propTypes = {
    createSocket: PropTypes.func.isRequired,
    token: PropTypes.string,
    players: PropTypes.objectOf(
        PropTypes.shape({
            stack: PropTypes.number,
            bet: PropTypes.number,
            status: PropTypes.string
        })
    ),
    tableID: PropTypes.string.isRequired
};

const mapStateToProps = (state) => {
    let tableID = state.router.location.pathname.substr(1);
    if (state.tables[tableID]) {
        return {
            players: state.tables[tableID].players,
            token: state.auth.token,
            tableID
        };
    } else {
        return {
            token: state.auth.token,
            tableID
        };
    }
};

const mapDispatchToProps = (dispatch) => ({
    createSocket: (table, token) => dispatch(createSocket(table, token))
});


export default connect(mapStateToProps, mapDispatchToProps)(Game);
