import React from 'react';
import { shallow } from 'enzyme';

import Signup from '../../components/Signup';

describe('Signup Test suite', () => {
    it('Should render Signup(snapshot) correctly', () => {
        const wrapper = shallow(<Signup />);
        expect(wrapper).toMatchSnapshot();
    });

    it('Should change username', () => {
        const wrapper = shallow(<Signup />);
        const usernameVal = 'bensi94';

        // Input field at 0 is the username field, this sets the username
        wrapper.find('Input').at(0).simulate('change', usernameVal);

        expect(wrapper.state('form').username).toBe(usernameVal);
    });

    it('Should change password', () => {
        const wrapper = shallow(<Signup />);
        const passVal = 'testpassword';

        // Input field at 1 is the password field, this sets the password
        wrapper.find('Input').at(1).simulate('change', passVal);

        expect(wrapper.state('form').password).toBe(passVal);
    });

    it('Should call submit on button clicked', () => {
        const wrapper = shallow(<Signup />);

        // This replaces the handleSubmit with a mock function
        // that should be called when the button is clicked
        wrapper.instance().handleSubmit = jest.fn();
        wrapper.instance().forceUpdate();
        wrapper.find('Button').at(0).simulate('click');

        expect(wrapper.instance().handleSubmit).toHaveBeenCalledTimes(1);
    });
});
