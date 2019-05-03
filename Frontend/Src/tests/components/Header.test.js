import React from 'react';
import { shallow } from 'enzyme';
import ReactShallowRenderer from 'react-test-renderer/shallow';

import Header from '../../components/Header';

describe('Header Test suite', () => {
    it('Should render Header(snapshot) correctly', () => {
        const renderer = new ReactShallowRenderer();
        renderer.render(<Header />);
        expect(renderer.getRenderOutput()).toMatchSnapshot();
    });

    it('Should have header Navbar', () => {
        const wrapper = shallow(<Header />);
        expect(wrapper.find('Navbar')).toHaveLength(1);
    });
});
