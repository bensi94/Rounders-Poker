import React from 'react';
import { shallow } from 'enzyme';

import Stack from '../../components/Table/Stack';


describe('Stack Test suite', () => {
    let wrapper;

    it('Should render component correctly', () => {
        expect(wrapper).toMatchSnapshot();
    });

    it('Should Generate correct stack for amount: 2543', () => {
        wrapper = shallow(
            <Stack stackAmount={2543}
                tableSize={500}
                left={10}
                top={10}/>);
        // 3 + 4 + 5 + 2 = 14
        expect(wrapper.instance().getChipStack().length).toBe(14);
    });

    it('Should Generate correct stack for amount: 24839', () => {
        wrapper = shallow(
            <Stack stackAmount={24839}
                tableSize={500}
                left={10}
                top={10}/>);
        // 9 + 3 + 8 + 4 + 2 = 26
        expect(wrapper.instance().getChipStack().length).toBe(26);
    });

    it('Should be calculating the style(positions correctly in getChipStack()', () => {
        wrapper = shallow(
            <Stack stackAmount={12}
                tableSize={1000}
                left={10}
                top={10}/>);

        wrapper.instance().setState({
            widthRatio: 1,
            leftRatio: 1,
            topRatio: 1,
            heightRatio: 1
        });

        const responseList = wrapper.instance().getChipStack();
        const respOne = responseList[0];
        const respTwo = responseList[1];
        const respThree = responseList[2];

        const styleOne = {
            left: '0px',
            top: '-0px',
            zIndex: 0
        };
        const styleTwo = {
            left: '0px',
            top: '-1000px',
            zIndex: 1
        };
        const styleThree = {
            left: '1000px',
            top: '-0px',
            zIndex: 0
        };

        // First component
        expect(respOne.props.width).toBe(1000);
        expect(respOne.props.style).toStrictEqual(styleOne);

        // Second component
        expect(respTwo.props.width).toBe(1000);
        expect(respTwo.props.style).toStrictEqual(styleTwo);

        // Third component
        expect(respThree.props.width).toBe(1000);
        expect(respThree.props.style).toStrictEqual(styleThree);
    });
});
