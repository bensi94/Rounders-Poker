import React from 'react';
import { shallow } from 'enzyme';

import { Navbar } from '../../components/Navbar';


describe('Navbar Test suite', () => {
    let wrapper;

    beforeEach(() => {
        wrapper = shallow(<Navbar active={''}/>);
    });

    it('Should render Navabar(snapshot) correctly', () => {
        expect(wrapper).toMatchSnapshot();
    });

    it('Should have router link to each menu', () => {
        expect(wrapper.find('NavLink')).toHaveLength(3);
    });
});
