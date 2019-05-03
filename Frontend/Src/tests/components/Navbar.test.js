import React from 'react';
import ReactShallowRenderer from 'react-test-renderer/shallow';
import { shallow } from 'enzyme';

import Navbar from '../../components/Navbar';


describe('Navbar Test suite', () => {
    it('Should render Navabar(snapshot) correctly', () => {
        const renderer = new ReactShallowRenderer();
        renderer.render(<Navbar />);
        expect(renderer.getRenderOutput()).toMatchSnapshot();
    });

    it('Should have router link to each menu', () => {
        const wrapper = shallow(<Navbar />);
        expect(wrapper.find('Link')).toHaveLength(3);
    });
});
