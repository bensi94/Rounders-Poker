import React from 'react';
import { shallow } from 'enzyme';

import Card from '../../components/Table/Card';

describe('Card Test suite', () => {
    let wrapper;

    it('Should render component correctly', () => {
        wrapper = shallow(<Card card="Ah" />);
        expect(wrapper).toMatchSnapshot();
    });

    it('Should throw error on missing card', () => {
        console.error = jest.fn();
        wrapper = shallow(<Card />);
        expect(console.error).toHaveBeenCalledTimes(1);
    });

    it('Should throw error on invalid card type', () => {
        console.error = jest.fn();
        wrapper = shallow(<Card card={1}/>);
        expect(console.error).toHaveBeenCalledTimes(1);
    });

    it('Should throw error on invalid card length', () => {
        console.error = jest.fn();
        wrapper = shallow(<Card card="invalid length"/>);
        expect(console.error).toHaveBeenCalledTimes(1);
    });

    it('Should throw error on invalid card value', () => {
        console.error = jest.fn();
        wrapper = shallow(<Card card="Bs"/>);
        expect(console.error).toHaveBeenCalledTimes(1);
    });

    it('Should throw error on invalid card suite', () => {
        console.error = jest.fn();
        wrapper = shallow(<Card card = "Ab" />);
        expect(console.error).toHaveBeenCalledTimes(1);
    });

    it('Should render A of hearts on prop', () => {
        wrapper = shallow(<Card card = "Ah" />);
        expect(wrapper.find('text').length).toBe(2);
        expect(wrapper.find('text').at(0).text()).toBe('A');
        expect(wrapper.find('text').at(1).text()).toBe('A');
        expect(wrapper.find('title').at(0).text()).toBe('card-heart');
    });

    it('Should render 9 of spades on prop', () => {
        wrapper = shallow(<Card card = "9s" />);
        expect(wrapper.find('text').length).toBe(2);
        expect(wrapper.find('text').at(0).text()).toBe('9');
        expect(wrapper.find('text').at(1).text()).toBe('9');
        expect(wrapper.find('title').at(0).text()).toBe('card-spades');
    });
});
