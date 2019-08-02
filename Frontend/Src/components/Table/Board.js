import React from 'react';
import PropTypes from 'prop-types';

import Card from './Card';
import Stack from './Stack';

class Board extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        let cards = [];

        this.props.board.forEach(cardString => {
            cards.push(<Card key={cardString} card={cardString} />);
        });
        return (
            <div className="board-wrapper">
                {cards}
                <Stack tableSize={this.props.tableSize}
                    // If the there is nothing in the pot (pot is undefined), the pot is 0
                    stackAmount={(this.props.pot ? this.props.pot : 0)}
                    left={50}
                    top={90}
                />
            </div>
        );
    }
}

Board.propTypes = {
    board: PropTypes.arrayOf(PropTypes.string),
    tableSize: PropTypes.number.isRequired,
    pot: PropTypes.number
};

export default Board;
