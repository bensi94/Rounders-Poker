import React from 'react';
import { shallow } from 'enzyme';

import Header from '../../components/Header';


describe('Header Test suite', () => {
    it('Should have header \'Rounders Poker \'', () => {
        const wrapper = shallow(<Header />);
        expect(wrapper.find('h1').text()).toEqual('Rounders Poker');
    });
});
