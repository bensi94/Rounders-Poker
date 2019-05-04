import React from 'react';
import { shallow } from 'enzyme';

import Signup from '../../components/Signup';

describe('Signup Test suite', () => {
    let wrapper;

    beforeEach(() => {
        wrapper = shallow(<Signup />);
    });

    it('Should render Signup(snapshot) correctly', () => {
        expect(wrapper).toMatchSnapshot();
    });

    it('Should change username', () => {
        const usernameVal = 'bensi94';

        // Input field at 0 is the username field, this sets the username
        wrapper.find('Input').at(0).simulate('change', usernameVal);

        expect(wrapper.state('form').username).toBe(usernameVal);
    });

    it('Should change password', () => {
        const passVal = 'testpassword';
        // Input field at 1 is the password field, this sets the password
        wrapper.find('Input').at(1).simulate('change', passVal);

        expect(wrapper.state('form').password).toBe(passVal);
    });

    it('Should call submit on button clicked', () => {
        // This replaces the handleSubmit with a mock function
        // that should be called when the button is clicked
        wrapper.instance().handleSubmit = jest.fn();
        wrapper.instance().forceUpdate();
        wrapper.find('Button').at(0).simulate('click');

        expect(wrapper.instance().handleSubmit).toHaveBeenCalledTimes(1);
    });

    it('Should have a username that is not empty', () => {
        const username = '';
        const callback = jest.fn();

        // Calling the validator with an empty username
        wrapper.instance().state.rules.username[1].validator('', username, callback);

        expect(callback).toHaveBeenCalledTimes(1);
        expect(callback).toHaveBeenCalledWith(new Error('Please input the username'));
    });

    it('Should have password length of at least 5', () => {
        const passVal = 'pw';
        const callback = jest.fn();

        // Calling the validator with a password that is too short
        wrapper.instance().state.rules.password[1].validator('', passVal, callback);

        expect(callback).toHaveBeenCalledTimes(1);
        expect(callback).toHaveBeenCalledWith(new Error('Password must be at least 5 characters'));
    });

    it('Should have matching passwords', () => {
        const passwordVal = 'testpass';
        const confirmPassVal = 'wrongpass';
        const callback = jest.fn();

        // Input field at 1 is the password field, this sets the password
        wrapper.find('Input').at(1).simulate('change', passwordVal);

        // Calling validator in confirmPassword and check if they match
        wrapper.instance().state.rules.confirmPassword[1].validator('', confirmPassVal, callback);

        expect(callback).toHaveBeenCalledTimes(1);
        expect(callback).toHaveBeenCalledWith(new Error('The passwords do not match'));
    });

    it('Should accept valid password', () => {
        const passwordVal = 'testpass';
        const confirmPassVal = 'testpass';
        const callback = jest.fn();

        // Input field at 1 is the password field, this sets the password
        wrapper.find('Input').at(1).simulate('change', passwordVal);

        // Calling the validator with an empty username
        wrapper.instance().state.rules.confirmPassword[1].validator('', confirmPassVal, callback);

        expect(callback).toHaveBeenCalledTimes(1);
        expect(callback).toHaveBeenCalledWith();
    });

    it('Should accept valid username', () => {
        const username = 'bensi94';
        const callback = jest.fn();

        // Calling the validator with an empty username
        wrapper.instance().state.rules.username[1].validator('', username, callback);

        expect(callback).toHaveBeenCalledTimes(1);
        expect(callback).toHaveBeenCalledWith();
    });
});
