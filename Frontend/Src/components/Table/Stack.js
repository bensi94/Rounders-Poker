import React from 'react';
import BlackChip from '../../../assets/black-chip-horizontal.svg';
// import BlueChip from '../../../assets/blue-chip-horizontal.svg';
// import GreenChip from '../../../assets/green-chip-horizontal.svg';
// import PinkChip from '../../../assets/pink-chip-horizontal.svg';
// import RedChip from '../../../assets/red-chip-horizontal.svg';

class Stack extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        let chips = [];
        for (let i = 0; i < 10; i++) {
            let style = {
                top: `${0 + i * -3}px`,
                left: '200px',
                zIndex: `${i * 1}`
            };

            chips.push(<BlackChip style={style} key={i} className="black-chip" width="15px"/>);
        }
        return (
            <>
                {chips}
            </>
        );
    }
}

export default Stack;
