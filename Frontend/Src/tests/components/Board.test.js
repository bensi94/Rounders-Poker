import React from 'react';
import { shallow } from 'enzyme';

import Board from '../../components/Table/Board';

describe('Board Test sutie', () => {
    let wrapper;

    it('Should render component correctly', () => {
        wrapper = shallow(<Board tableSize={1000} board={['Ah', 'As', '9d', '6c', '7c']} pot={99999}/>);
        expect(wrapper).toMatchSnapshot();
    });

    it('Should render correct amount of cards', () => {
        wrapper = shallow(<Board tableSize={1000} board={['Ah', 'As', '9d', '6c']} pot={99999} />);
        expect(wrapper.find('Card').length).toBe(4);
    });

    it('Should render in correct order', () => {
        wrapper = shallow(<Board tableSize={1000} board={['Ah', 'As', '9d', '6c', '7c']} pot={99999} />);
        expect(wrapper.find('Card').at(0).prop('card')).toBe('Ah');
        expect(wrapper.find('Card').at(1).prop('card')).toBe('As');
        expect(wrapper.find('Card').at(2).prop('card')).toBe('9d');
        expect(wrapper.find('Card').at(3).prop('card')).toBe('6c');
        expect(wrapper.find('Card').at(4).prop('card')).toBe('7c');
    });

    it('Should render in correct stackAmount', () => {
        wrapper = shallow(<Board tableSize={1000} board={['Ah', 'As', '9d', '6c', '7c']} pot={99999} />);
        expect(wrapper.find('Stack').first().prop('stackAmount')).toBe(99999);
    });
    it('Should render in correct stackAmount on undefined', () => {
        wrapper = shallow(<Board tableSize={1000} board={['Ah', 'As', '9d', '6c', '7c']} />);
        expect(wrapper.find('Stack').first().prop('stackAmount')).toBe(0);
    });
});
