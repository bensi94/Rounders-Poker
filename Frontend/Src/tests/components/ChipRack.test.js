import React from 'react';
import { shallow } from 'enzyme';

import ChipRack from '../../components/Table/ChipRack';

describe('ChipRack Test suite', () => {
    let wrapper;

    // This is done because we use Math.random in the component
    // But we can not do a snapshot test with random variables
    global.Math.random = () => 0.5;

    beforeEach(() => {
        wrapper = shallow(<ChipRack tableSize={500} />);
    });

    it('Should render ChipRack(snapshot) correctly', () => {
        expect(wrapper).toMatchSnapshot();
    });

    // Tests that the getChipComponent function works as expected
    it('Should contain the correct style and key on getChipComponent', () => {
        const styleObj = {
            left: '10%',
            top: '20%',
            zIndexL: 1
        };

        wrapper.instance().setState({
            widthConstant: 1
        });

        const responseComp = wrapper.instance().getChipComponent(
            'GreenChip',
            styleObj,
            'test_key'
        );

        expect(responseComp.key).toBe('test_key');
        expect(responseComp.props.style).toBe(styleObj);
        // Based on the tableSize prop and the widthConstant
        expect(responseComp.props.width).toBe(500);
    });

    it('Should not render a chip on invalid componentString', () => {
        const responseComp = wrapper.instance().getChipComponent(
            'INVALIDSTRING'
        );

        expect(responseComp).toBe(undefined);
    });


    it('Should render the correct amount of components in getChipRack', () => {
        wrapper.instance().setState({
            maxChipCount: 1,
            componentList: [
                'GreenChip',
                'RedChip',
                'BlueChip',
                'PinkChip',
                'BlackChip'
            ]
        });

        expect(wrapper.instance().getChipRack().length).toBe(5);
    });

    it('Should be calculating the style(postions) correctly in getChipRack', () => {
        wrapper.instance().setState({
            maxChipCount: 2,
            left: 1,
            leftAdd: 1,
            topConstant: 1,
            topPercent: 1,
            widthConstant: 1,
            componentList: [
                'GreenChip',
                'RedChip'
            ]
        });

        const responseList = wrapper.instance().getChipRack();
        const responseOne = responseList[0];
        const responseTwo = responseList[1];
        const responseThree = responseList[2];

        const styleOne = {
            left: '1%',
            top: '1%',
            zIndex: '0'
        };

        const styleTwo = {
            left: '1%',
            top: '2%',
            zIndex: '1'
        };

        const styleThree = {
            left: '2%',
            top: '1%',
            zIndex: '0'
        };

        // First component
        expect(responseOne.props.width).toBe(500);
        expect(responseOne.props.style).toStrictEqual(styleOne);

        // Second component
        expect(responseTwo.props.width).toBe(500);
        expect(responseTwo.props.style).toStrictEqual(styleTwo);

        // Third component
        expect(responseThree.props.width).toBe(500);
        expect(responseThree.props.style).toStrictEqual(styleThree);
    });
});
