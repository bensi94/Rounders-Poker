import React from 'react';
import PropTypes from 'prop-types';

import BlackChip from '../../../assets/black-chip-vertical.svg';
import BlueChip from '../../../assets/blue-chip-vertical.svg';
import GreenChip from '../../../assets/green-chip-vertical.svg';
import PinkChip from '../../../assets/pink-chip-vertical.svg';
import RedChip from '../../../assets/red-chip-vertical.svg';

class ChipRack extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            maxChipCount: 19,
            left: 38.8,
            leftAdd: 3.28,
            topConstant: 4,
            topPercent: 0.6,
            widthConstant: 0.027,
            componentList: [
                'GreenChip',
                'RedChip',
                'BlueChip',
                'PinkChip',
                'BlackChip',
                'BlueChip',
                'RedChip'
            ],
            chipRack: undefined
        };
    }

    componentDidMount() {
        this.setState({
            chipRack: this.getChipRack()
        });
    }

    getChipComponent(component, style, keyString) {
        switch (component) {
            case 'GreenChip':
                return (<GreenChip
                    style={style}
                    className="vertical-chip"
                    width={this.props.tableSize * this.state.widthConstant}
                    key={keyString} />
                );
            case 'RedChip':
                return (<RedChip
                    style={style}
                    className="vertical-chip"
                    width={this.props.tableSize * this.state.widthConstant}
                    key={keyString} />
                );
            case 'BlueChip':
                return (<BlueChip
                    style={style}
                    className="vertical-chip"
                    width={this.props.tableSize * this.state.widthConstant}
                    key={keyString} />
                );
            case 'PinkChip':
                return (<PinkChip
                    style={style}
                    className="vertical-chip"
                    width={this.props.tableSize * this.state.widthConstant}
                    key={keyString} />
                );
            case 'BlackChip':
                return (<BlackChip
                    style={style}
                    className="vertical-chip"
                    width={this.props.tableSize * this.state.widthConstant}
                    key={keyString}/>
                );
            default:
                break;
        }
    }

    getChipRack() {
        let chips = [];
        this.state.componentList.map((component, index) => {
            const randomNumb = Math.floor((Math.random() * this.state.maxChipCount) + 1);
            for (let i = 0; i < randomNumb; i++) {
                const style = {
                    left: `${this.state.left + this.state.leftAdd * index}%`,
                    top: `${this.state.topConstant + i * this.state.topPercent}%`,
                    zIndex: `${i}`
                };
                chips.push(this.getChipComponent(component,
                    style, `${index.toString()}_${i.toString()}`));
            }
        });

        return chips;
    }

    render() {
        return (
            <>
                {this.state.chipRack}
            </>
        );
    }
}

ChipRack.propTypes = {
    tableSize: PropTypes.number.isRequired
};

export default ChipRack;
