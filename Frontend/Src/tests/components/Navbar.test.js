import React from 'react';
import { shallow } from 'enzyme';

import { Navbar } from '../../components/Navbar';


describe('Navbar Test suite', () => {
    let wrapper;

    beforeEach(() => {
        wrapper = shallow(<Navbar
            active={''}
            isAuthenticated={false}
            logOut={jest.fn()}
            checkUser={jest.fn()}
        />);
    });

    it('Should render Navabar(snapshot) correctly', () => {
        expect(wrapper).toMatchSnapshot();
    });

    it('Should have router link to each menu on unauthenticated', () => {
        expect(wrapper.find('NavLink')).toHaveLength(3);
    });

    it('Should have router link to each menu on unauthenticated', () => {
        wrapper = shallow(<Navbar
            active={''}
            isAuthenticated
            logOut={jest.fn()}
            checkUser={jest.fn()}
        />);
        expect(wrapper.find('NavLink')).toHaveLength(2);
    });
});
