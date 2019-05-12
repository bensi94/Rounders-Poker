import React from 'react';
import { shallow } from 'enzyme';

import { Header } from '../../components/Header';

describe('Header Test suite', () => {
    it('Should render Header(snapshot) correctly', () => {
        const wrapper = shallow(<Header checkUser={jest.fn()}/>);
        expect(wrapper).toMatchSnapshot();
    });
});
