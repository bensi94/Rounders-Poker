import React from 'react';
import { shallow } from 'enzyme';

import Navbar from '../../components/Navbar';


describe('Navbar Test suite', () => {
    it('Should render Navabar(snapshot) correctly', () => {
        const wrapper = shallow(<Navbar />);
        expect(wrapper).toMatchSnapshot();
    });

    it('Should have router link to each menu', () => {
        const wrapper = shallow(<Navbar />);
        expect(wrapper.find('NavLink')).toHaveLength(3);
    });
});
