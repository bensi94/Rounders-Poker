import React from 'react';
import TableBaseSVG from '../../../assets/table-base.svg';
import Stack from './Stack';
import ChipRack from './ChipRack';
import Player from './Player';


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
                <TableBaseSVG width={`${this.state.tableSize}px`} height="100%" />
                <ChipRack tableSize={this.state.tableSize} />
                <Stack
                    tableSize={this.state.tableSize}
                    stackAmount={24839}
                    left={50}
                    top={50}
                />
                <Stack
                    tableSize={this.state.tableSize}
                    stackAmount={487}
                    left={30}
                    top={30}
                />
                <Player tableSize={this.state.tableSize} left={10} top={10} stack={1000} name="bensi"/>
            </div>
        );
    }
}

export default TableBase;
