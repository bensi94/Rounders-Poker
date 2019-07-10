import React from 'react';
import PropTypes from 'prop-types';


class Player extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            widthRatio: 0.17
        };
    }

    render() {
        let style = {
            left: `${this.props.left}%`,
            top: `${this.props.top}%`,
            width: `${this.props.tableSize * this.state.widthRatio}px`
        };

        return (
            <div style={style} className="player-rect">
                <svg id = "92f50c61-a635-413f-87df-d274975daa0e" viewBox="0 0 150 75">
                    <title>player-rect</title>
                    <g id="5f2ad952-a9de-49e6-aadd-7f71fef5b04b" data-name="Seat 1">
                        <rect width="150" height="75" rx="5" ry="5" className="player-rect-bg"/>
                        <text transform="translate(22.7 56.62)"className="player-react-stack-text">
                            ${ this.props.stack }
                        </text>
                        <text transform="translate(40.03 21.96)" className="player-react-title-text">
                            { this.props.name }
                        </text>
                    </g>
                </svg>
            </div>
        );
    }
}

Player.propTypes = {
    tableSize: PropTypes.number.isRequired,
    left: PropTypes.number.isRequired,
    top: PropTypes.number.isRequired,
    stack: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired

};

export default Player;
