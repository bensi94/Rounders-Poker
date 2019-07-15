import React from 'react';

class Card extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className="card-wrapper">
                <svg id="bcb7fd9d-bab4-42c0-8618-7c28c00ccc49"
                    data-name="A&apos;s"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 68 90"
                    className="card-base"
                >
                    <defs>
                        <linearGradient id="c598038e-929c-49a3-bb73-1bcb01594f60"
                            x1="6.91" y1="44.9"
                            x2="61.41" y2="44.9"
                            gradientUnits="userSpaceOnUse"
                        >
                            <stop offset="0" stopColor="#fff"/>
                            <stop offset="1" stopColor="#e6e7e8"/>
                        </linearGradient>
                    </defs>
                    <title>card-spades</title>
                    <g id="e897df38-4927-4ab9-be85-2bc7fccda1fc" data-name="Spade card">
                        <g>
                            <rect x="7.16" y="6.9" width="54" height="76" rx="5" ry="5" className="card-rect-1"/>
                            <rect x="7.16" y="6.9" width="54" height="76" rx="5" ry="5" className="card-rect-2"/>
                        </g>
                        <path
                            d="M127.52,45.2c-0.76-1.62-9.36-10.25-9.36-10.25s-8.42,8.52-9.23,10a4.12,4.12,0,0,0-.52,2,
                              4.77,4.77,0,0,0,5,4.5,5.14,5.14,0,0,0,3.92-1.75,10.87,10.87,0,0,1-1.92,5h5.5a10.87,10.87,
                              0,0,1-1.92-5,5.14,5.14,0,0,0,3.92,1.75,4.77,4.77,0,0,0,5-4.5A4.1,4.1,0,0,0,127.52,45.2Z"
                            transform="translate(-84 0.09)"
                            className="card-black"
                        />
                        <g id="e375a035-2353-4cfb-a60d-c6e2572b9514" data-name="Number high copy 3">
                            <path
                                d="M102.28,27.71a54.24,54.24,0,0,0-4.21-4.61s-3.79,3.83-4.15,4.5a1.85,1.85,0,0,0-.23.9,
                                    2.15,2.15,0,0,0,2.25,2,2.31,2.31,0,0,0,1.76-.79A4.89,4.89,0,0,1,96.83,32H99.3a4.89,
                                    4.89,0,0,1-.86-2.24,2.31,2.31,0,0,0,1.76.79,2.15,2.15,0,0,0,2.25-2A1.85,1.85,0,0,0,
                                    102.28,27.71Z"
                                transform="translate(-84 0.09)"
                                className="card-black"
                            />
                            <text transform="translate(10.3 22.14)" className="card-black card-digit">A</text>
                        </g>
                        <g id="dcd80689-f491-456f-950d-327c7ff45193" data-name="Number low copy 3">
                            <text transform="translate(58.02 68.18) rotate(180)" className="card-black card-digit">
                                A
                            </text>
                            <path
                                d="M134,61.55a54.24,54.24,0,0,0,4.21,4.61s3.79-3.83,4.15-4.5a1.85,1.85,0,0,0,.23-0.9,
                                    2.15,2.15,0,0,0-2.25-2,2.31,2.31,0,0,0-1.76.79,4.89,4.89,0,0,1,.86-2.24H137a4.89,
                                    4.89,0,0,1,.86,2.24,2.31,2.31,0,0,0-1.76-.79,2.15,2.15,0,0,0-2.25,2A1.85,1.85,0,0,
                                    0,134,61.55Z"
                                transform="translate(-84 0.09)"
                                className="card-black"
                            />
                        </g>
                    </g>
                </svg>
            </div>

        );
    }
}

Card.propTypes = {
    card: (props, propName, componentName) => {
        // This prop needs  a custom propType check to make sure it is only able to get valid cards
        // Invalid cards could cause problems while rendering.
        // It checks if it string of length 2, and if the card value and suite is valid
        let prop = props[propName];
        if (prop) {
            if (typeof prop !== 'string') {
                return new Error(propName + ' is not a string');
            } else if (prop.length !== 2) {
                return new Error(propName + ' needs to be of length 2 of type cardValue:suite (example: Ah)');
            } else if (['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'].indexOf(prop[0]) < 0) {
                return new Error(propName + ' does not have correct card value');
            } else if (['h', 's', 'd', 'c'].indexOf(prop[1]) < 0) {
                return new Error(propName + ' does not have correct suite');
            }

            return null;
        }
        return new Error(propName + ' is required');
    }
};

export default Card;
