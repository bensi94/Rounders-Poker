import React from 'react';
import { shallow } from 'enzyme';

import Login from '../../components/Login';

describe('Login Test suite', () => {
    let wrapper;

    beforeEach(() => {
        wrapper = shallow(<Login />);
    });

    it('Should render Login(snapshot) correctly', () => {
        expect(wrapper).toMatchSnapshot();
    });

    it('Should change username', () => {
        const username = 'bensi94';

        // Input field at 0 should be username field
        wrapper.find('Input').at(0).simulate('change', username);

        expect(wrapper.state('form').username).toBe(username);
    });

    it('Should change password', () => {
        const password = 'testpassword';

        // Input field at 1 should be password field
        wrapper.find('Input').at(1).simulate('change', password);

        expect(wrapper.state('form').password).toBe(password);
    });

    it('Should call submit on button clicked', () => {
        // Replaces the handleSubmit with a mock function
        // that should be clicked when the button is clicked
        const submitMock = jest.fn();
        wrapper.instance().handleSubmit = submitMock;
        wrapper.instance().forceUpdate();
        wrapper.find('Button').at(0).simulate('click');

        expect(submitMock).toHaveBeenCalledTimes(1);
    });

    it('Should have a username that is not empty', () => {
        const username = '';
        const callback = jest.fn();

        // Calling the validator with an empty username
        wrapper.instance().state.rules.username[1].validator('', username, callback);

        expect(callback).toHaveBeenCalledTimes(1);
        expect(callback).toHaveBeenCalledWith(new Error('Please input the username'));
    });

    it('Should have a password that is not empty', () => {
        const password = '';
        const callback = jest.fn();

        // Calling the validator with an empty username
        wrapper.instance().state.rules.password[1].validator('', password, callback);

        expect(callback).toHaveBeenCalledTimes(1);
        expect(callback).toHaveBeenCalledWith(new Error('Please input the password'));
    });
});
