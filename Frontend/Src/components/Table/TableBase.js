import React from 'react';
import TableBaseSVG from '../../../assets/table-base.svg';
import ChipRack from './ChipRack';
import Player from './Player';
import Board from './Board';


class TableBase extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            tableSize: 1000
        };
    }

    render() {
        return (
            <div className="table-base-container">
                <TableBaseSVG width={`${this.state.tableSize}px`} height="100%" className="table-base-svg"/>
                <ChipRack tableSize={this.state.tableSize} />
                <Player tableSize={this.state.tableSize}
                    seatNumber={1}
                    stack={11}
                    bet={100}
                    name="bensi"
                    cards={['Kc', 'Kh']}
                    status="ACTIVE"
                />
                <Player
                    tableSize={this.state.tableSize}
                    seatNumber={2}
                    stack={999}
                    name="bensi"
                    status="INACTIVE"
                />
                <Player
                    tableSize={this.state.tableSize}
                    seatNumber={3}
                    stack={19387}
                    name="bensi"
                    status="FOLDED"
                />
                <Player
                    tableSize={this.state.tableSize}
                    seatNumber={4}
                    stack={432}
                    bet={1999}
                    name="bensi"
                    status="ACTIVE"
                />
                <Player
                    tableSize={this.state.tableSize}
                    seatNumber={5}
                    stack={23}
                    bet={1999}
                    name="bensi"
                    status="ACTIVE"
                />
                <Player
                    tableSize={this.state.tableSize}
                    seatNumber={6}
                    stack={99999}
                    bet={1999}
                    name="bensi"
                    status="ACTIVE"
                />
                <Player tableSize={this.state.tableSize}
                    seatNumber={7}
                    stack={124}
                    name="bensi"
                    status="INACTIVE"
                />
                <Player
                    tableSize={this.state.tableSize}
                    seatNumber={8}
                    stack={132}
                    name="bensi"
                    status="FOLDED"
                />
                <Player
                    tableSize={this.state.tableSize}
                    seatNumber={9}
                    stack={2342}
                    bet={1999}
                    name="bensi"
                    status="ACTIVE"
                />
                <Board tableSize={this.state.tableSize} board={['Ah', 'As', '9d', '6c', '7c']} pot={99999}/>
            </div>
        );
    }
}

export default TableBase;
