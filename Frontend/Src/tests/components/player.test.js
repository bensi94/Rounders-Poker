import React from 'react';
import { shallow } from 'enzyme';

import Player from '../../components/Table/Player';


describe('Player test sutie', () => {
    let wrapper;

    it('should render component correctly', () => {
        wrapper = shallow(
            <Player tableSize={1000}
                stack={100}
                bet={10}
                name="bensi"
                seatNumber={1}
                status="ACTIVE"
            />
        );
        expect(wrapper).toMatchSnapshot();
    });

    it('should set the correct state for given seatNumber', () => {
        wrapper = shallow(
            <Player tableSize={1000}
                stack={100}
                bet={10}
                name="bensi"
                seatNumber={1}
                cards={['Kc', 'Kh']}
                status="ACTIVE"
            />
        );
        let caseStateObj = {
            rectLeft: '70%',
            rectTop: '-14%',
            stackLeft: 80,
            stackTop: 13,
            widthPercent: '16%',
            cardOpacity: {
                opacity: 1
            }
        };
        expect(wrapper.instance().state).toStrictEqual(caseStateObj);
    });

    it('should have a visual stack if there is bet', () => {
        wrapper = shallow(
            <Player tableSize={1000}
                stack={100}
                bet={10}
                name="bensi"
                seatNumber={1}
                cards={['Kc', 'Kh']}
                status="ACTIVE"
            />
        );
        expect(wrapper.find('Stack').length).toBe(1);
    });

    it('should not have a visual stack if there is no bet', () => {
        wrapper = shallow(
            <Player tableSize={1000}
                stack={100}
                name="bensi"
                seatNumber={1}
                status="FOLDED"
            />
        );
        expect(wrapper.find('Stack').length).toBe(0);
    });
});
