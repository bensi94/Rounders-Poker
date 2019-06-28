import React from 'react';
import TableBaseSVG from '../../../assets/table-base.svg';
import Stack from './Stack';
import ChipRack from './ChipRack';


class TableBase extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            tableSize: 600
        };
    }

    render() {
        return (
            <div className="table-base-container">
                <TableBaseSVG width={`${this.state.tableSize}px`} height="100%" />
                <ChipRack tableSize={this.state.tableSize} />
                <Stack />
            </div>
        );
    }
}

export default TableBase;
