import React from 'react';
import PropTypes from 'prop-types';

import BlackChip from '../../../assets/black-chip-horizontal.svg';
import BlueChip from '../../../assets/blue-chip-horizontal.svg';
import GreenChip from '../../../assets/green-chip-horizontal.svg';
import PinkChip from '../../../assets/pink-chip-horizontal.svg';
import RedChip from '../../../assets/red-chip-horizontal.svg';

class Stack extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            widthRatio: 0.027,
            leftRatio: 0.028,
            topRatio: 0.003,
            heightRatio: 0.025,
            fontRatio: 0.011,
            chipRankList: [
                'PinkChip',
                'BlackChip',
                'RedChip',
                'BlueChip',
                'GreenChip'
            ],
            chipStack: undefined,
            stackWidth: 0
        };
    }

    componentDidMount() {
        this.setState({
            chipStack: this.getChipStack(),
            height: this.state.heightRatio * this.props.tableSize
        });
    }

    getChipComponent(component, style, keyString) {
        switch (component) {
            case 'GreenChip':
                return (<GreenChip
                    style={style}
                    className="horizontal-chip"
                    width={this.props.tableSize * this.state.widthRatio}
                    key={keyString} />
                );
            case 'RedChip':
                return (<RedChip
                    style={style}
                    className="horizontal-chip"
                    width={this.props.tableSize * this.state.widthRatio}
                    key={keyString} />
                );
            case 'BlueChip':
                return (<BlueChip
                    style={style}
                    className="horizontal-chip"
                    width={this.props.tableSize * this.state.widthRatio}
                    key={keyString} />
                );
            case 'PinkChip':
                return (<PinkChip
                    style={style}
                    className="horizontal-chip"
                    width={this.props.tableSize * this.state.widthRatio}
                    key={keyString} />
                );
            case 'BlackChip':
                return (<BlackChip
                    style={style}
                    className="horizontal-chip"
                    width={this.props.tableSize * this.state.widthRatio}
                    key={keyString}/>
                );
            default:
                break;
        }
    }

    getChipStack() {
        let chips = [];
        // We reverse the string to start with the smallest number(chip)
        const amount = this.props.stackAmount.toString().split('').reverse().join('');
        // If chips go above 100k we do not generate them at this point
        for (let i = 0; i < amount.length && i < this.state.chipRankList.length; i++) {
            const currentChipCount = amount[i];
            for (let j = 0; j < currentChipCount; j++) {
                const style = {
                    left: `${this.state.leftRatio * this.props.tableSize * i}px`,
                    top: `-${this.state.topRatio * this.props.tableSize * j}px`,
                    zIndex: j
                };
                chips.push(this.getChipComponent(this.state.chipRankList[i],
                    style, `${i.toString()}_${j.toString()}`));
            }
            this.setState({
                stackWidth: this.state.leftRatio * this.props.tableSize * (i + 1)
            });
        }

        return chips;
    }

    render() {
        let style = {
            left: `${this.props.left}%`,
            top: `${this.props.top}%`,
            transform: `translateX(-${this.state.stackWidth / 2}px)`
        };

        let labelPosClass = this.props.top > 50 ? 'lbl-pos-top' : 'lbl-pos-bottom';

        return (
            <div className="stack-wrapper" style={style}>
                {this.state.chipStack}
                <div className={`bet-amount-lbl ${labelPosClass}`}
                    style={{ fontSize: `${this.props.tableSize * this.state.fontRatio}pt` }}
                >
                    ${ this.props.stackAmount }
                </div>
            </div>
        );
    }
}

Stack.propTypes = {
    stackAmount: PropTypes.number.isRequired,
    tableSize: PropTypes.number.isRequired,
    left: PropTypes.number.isRequired,
    top: PropTypes.number.isRequired
};

export default Stack;
