import React from 'react';
import PropTypes from 'prop-types';
import { Loading, Alert } from "element-react";
import { connect } from 'react-redux';
import { createSocket } from '../actions/socket';
import TableBase from './Table/TableBase';


class Game extends React.Component {
    constructor(props) {
        super(props);
    }

    componentDidMount() {
        this.props.createSocket(this.props.tableID, this.props.token);
    }

    render() {
        if (this.props.error) {
            return (
                <Alert title={this.props.error.type}
                    type="error"
                    showIcon
                />
            );
        } else if (this.props.waiting) {
            return (
                <Loading text="Loading Table" />
            );
        }
        return (
            <>
                <h1> Game </h1>
                { this.props.players && Object.keys(this.props.players).map((key) => {
                    return <div key={key}>Player: {key}</div>;
                })}
                { this.props.observers && this.props.observers.map((observer) => {
                    return <div key={observer}>Observer: {observer}</div>;
                })}
                <div className="game-full">
                    <TableBase />
                </div>
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
    observers: PropTypes.arrayOf(PropTypes.string),
    tableID: PropTypes.string.isRequired,
    error: PropTypes.shape({
        type: PropTypes.string,
        error: PropTypes.shape({
            type: PropTypes.string
        })
    }),
    waiting: PropTypes.bool
};

const mapStateToProps = (state, { match }) => {
    let tableID = match.params.tableID;
    if (state.tables[tableID]) {
        let error = state.tables[tableID].error;
        return {
            players: state.tables[tableID].players,
            observers: state.tables[tableID].observers,
            token: state.auth.token,
            tableID,
            error
        };
    } else {
        return {
            token: state.auth.token,
            waiting: true,
            tableID
        };
    }
};

const mapDispatchToProps = (dispatch) => ({
    createSocket: (table, token) => dispatch(createSocket(table, token))
});


export default connect(mapStateToProps, mapDispatchToProps)(Game);
