import React from 'react';
import PropTypes from 'prop-types';

import Stack from './Stack';

class Player extends React.Component {
    constructor(props) {
        super(props);
        let stateObj = {};

        switch (this.props.seatNumber) {
            case 1:
                stateObj = {
                    rectLeft: '70%',
                    rectTop: '-4%',
                    stackLeft: 80,
                    stackTop: 13
                };
                break;
            case 2:
                stateObj = {
                    rectLeft: '86%',
                    rectTop: '18%',
                    stackLeft: 90,
                    stackTop: 36
                };
                break;
            case 3:
                stateObj = {
                    rectLeft: '90%',
                    rectTop: '57%',
                    stackLeft: 86,
                    stackTop: 72
                };
                break;
            case 4:
                stateObj = {
                    rectLeft: '68%',
                    rectTop: '87%',
                    stackLeft: 71,
                    stackTop: 82
                };
                break;
            case 5:
                stateObj = {
                    rectLeft: '42%',
                    rectTop: '87%',
                    stackLeft: 50,
                    stackTop: 82
                };
                break;
            case 6:
                stateObj = {
                    rectLeft: '16%',
                    rectTop: '87%',
                    stackLeft: 30,
                    stackTop: 82
                };
                break;
            case 7:
                stateObj = {
                    rectLeft: '-6%',
                    rectTop: '57%',
                    stackLeft: 18,
                    stackTop: 72
                };
                break;
            case 8:
                stateObj = {
                    rectLeft: '-2%',
                    rectTop: '18%',
                    stackLeft: 13,
                    stackTop: 36
                };
                break;
            case 9:
                stateObj = {
                    rectLeft: '14%',
                    rectTop: '-4%',
                    stackLeft: 23.5,
                    stackTop: 13
                };
            default:
                break;
        }

        this.state = {
            ...stateObj,
            widthPercent: '16%'
        };
    }


    render() {
        return (
            <>
                <div style={{ width: this.state.widthPercent, left: this.state.rectLeft, top: this.state.rectTop }}
                    className="player-rect"
                >
                    <svg id = "92f50c61-a635-413f-87df-d274975daa0e" viewBox="0 0 150 75">
                        <title>player-rect</title>
                        <g id="5f2ad952-a9de-49e6-aadd-7f71fef5b04b" data-name="Seat 1">
                            <rect width="150" height="75" rx="5" ry="5" className="player-rect-bg"/>
                            <text transform="translate(75 56.62)"className="player-react-stack-text">
                                ${ this.props.stack }
                            </text>
                            <text transform="translate(75 21.96)" className="player-react-title-text">
                                { this.props.name }
                            </text>
                        </g>
                    </svg>
                </div>
                {this.props.bet > 0 ?
                    <Stack
                        tableSize={this.props.tableSize}
                        stackAmount={this.props.bet}
                        left={this.state.stackLeft}
                        top={this.state.stackTop}
                    /> : undefined
                }
            </>
        );
    }
}

Player.defaultProps = {
    bet: 0
};

Player.propTypes = {
    tableSize: PropTypes.number.isRequired,
    stack: PropTypes.number.isRequired,
    bet: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
    seatNumber: PropTypes.oneOf([1, 2, 3, 4, 5, 6, 7, 8, 9])

};

export default Player;
