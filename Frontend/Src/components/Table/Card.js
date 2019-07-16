import React from 'react';

class Card extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        if (typeof this.props.card !== 'string' || this.props.card.length !== 2) {
            return (<> </>);
        }
        let cardGraphic;
        // Switch case to determine which type of card is being rendered
        switch (this.props.card[1]) {
            // HEARTS
            case 'h':
                cardGraphic = (<>
                    <title>card-heart</title>
                        <g id="0f8e4d85-2f6a-4447-8c72-a7597776f2fd" data-name="Heart card">
                            <g>
                                <rect x="6.41" y="6.27" width="54" height="76" rx="5" ry="5" className="card-rect-1"/>
                                <rect x="6.41" y="6.27" width="54" height="76" rx="5" ry="5" className="card-rect-2"/>
                            </g>
                            <path
                                d="M58.77,41.3a4.1,4.1,0,0,0,.39-1.75,4.77,4.77,0,0,0-5-4.5,5,5,0,0,0-4.75,3.16,5,5,0,
                                0,0-4.75-3.16,4.77,4.77,0,0,0-5,4.5,4.12,4.12,0,0,0,.52,2C41,43,49.41,53.48,49.41,
                                53.48S58,42.92,58.77,41.3Z"
                                transform="translate(-16)"
                                className="card-red"
                            />
                            <g id="3cb033ef-9166-4ec5-8cca-6b37929f3d2c" data-name="Number high">
                                <path
                                    d="M33.53,26.21a1.85,1.85,0,0,0,.18-0.79,2.15,2.15,0,0,0-2.25-2,2.23,2.23,0,0,
                                    0-2.14,1.42,2.23,2.23,0,0,0-2.14-1.42,2.15,2.15,0,0,0-2.25,2,1.85,1.85,0,0,0,
                                    .23.9c0.37,0.67,4.15,5.37,4.15,5.37S33.18,26.93,33.53,26.21Z"
                                    transform="translate(-16)"
                                    className="card-red"
                                />
                                <text transform="translate(9.55 22.05)" className="card-red card-digit">
                                    {this.props.card[0]}
                                </text>
                            </g>
                            <g id="dcd80689-f491-456f-950d-327c7ff45193" data-name="Number low copy 3">
                                <text transform="translate(57.27 68.09) rotate(180)" className="card-red card-digit">
                                    {this.props.card[0]}
                                </text>
                                <path
                                    d="M65.3,63.06a1.85,1.85,0,0,0-.18.79,2.15,2.15,0,0,0,2.25,2,2.23,2.23,0,0,0,
                                    2.14-1.42,2.23,2.23,0,0,0,2.14,1.42,2.15,2.15,0,0,0,2.25-2,1.85,1.85,0,0,
                                    0-.23-0.9c-0.37-.67-4.15-5.37-4.15-5.37S65.64,62.33,65.3,63.06Z"
                                    transform="translate(-16)"
                                    className="card-red"
                                />
                            </g>
                        </g>
                    </>);
                break;
                // SPADES
            case 's':
                cardGraphic = (<>
                    <title>card-spades</title>
                        <g id="e897df38-4927-4ab9-be85-2bc7fccda1fc" data-name="Spade card">
                            <g>
                                <rect x="7.16" y="6.9" width="54" height="76" rx="5" ry="5" className="card-rect-1"/>
                                <rect x="7.16" y="6.9" width="54" height="76" rx="5" ry="5" className="card-rect-2"/>
                            </g>
                            <path
                                d="M127.52,45.2c-0.76-1.62-9.36-10.25-9.36-10.25s-8.42,8.52-9.23,10a4.12,4.12,0,0,0-.52,
                                2,4.77,4.77,0,0,0,5,4.5,5.14,5.14,0,0,0,3.92-1.75,10.87,10.87,0,0,1-1.92,5h5.5a10.87,
                                10.87,0,0,1-1.92-5,5.14,5.14,0,0,0,3.92,1.75,4.77,4.77,0,0,0,5-4.5A4.1,4.1,0,0,0,
                                127.52,45.2Z"
                                transform="translate(-84 0.09)"
                                className="card-black"
                            />
                            <g id="e375a035-2353-4cfb-a60d-c6e2572b9514" data-name="Number high copy 3">
                                <path
                                    d="M102.28,27.71a54.24,54.24,0,0,0-4.21-4.61s-3.79,3.83-4.15,4.5a1.85,1.85,0,0,
                                    0-.23.9,2.15,2.15,0,0,0,2.25,2,2.31,2.31,0,0,0,1.76-.79A4.89,4.89,0,0,1,
                                    96.83,32H99.3a4.89,4.89,0,0,1-.86-2.24,2.31,2.31,0,0,0,1.76.79,2.15,2.15,0,0,0,
                                    2.25-2A1.85,1.85,0,0,0,102.28,27.71Z"
                                    transform="translate(-84 0.09)"
                                    className="card-black"
                                />
                                <text transform="translate(10.3 22.14)" className="card-black card-digit">
                                    {this.props.card[0]}
                                </text>
                            </g>
                            <g id="dcd80689-f491-456f-950d-327c7ff45193" data-name="Number low copy 3">
                                <text transform="translate(58.02 68.18) rotate(180)" className="card-black card-digit">
                                    {this.props.card[0]}
                                </text>
                                <path
                                    d="M134,61.55a54.24,54.24,0,0,0,4.21,4.61s3.79-3.83,4.15-4.5a1.85,1.85,0,0,0,
                                    .23-0.9, 2.15,2.15,0,0,0-2.25-2,2.31,2.31,0,0,0-1.76.79,4.89,4.89,0,0,1,
                                    .86-2.24H137a4.89, 4.89,0,0,1,.86,2.24,2.31,2.31,0,0,0-1.76-.79,2.15,2.15,0,0,
                                    0-2.25,2A1.85,1.85,0,0,0,134,61.55Z"
                                    transform="translate(-84 0.09)"
                                    className="card-black"
                                />
                            </g>
                        </g>
                    </>);
                break;
                // DIAMONDS
            case 'd':
                cardGraphic = (<>
                    <title>card-dimond</title>
                        <g id="4fefe516-9bda-42af-a3e8-03ff61bcde3a" data-name="Dimond card">
                            <g>
                                <rect x="6.41" y="6.27" width="54" height="76" rx="5" ry="5" className="card-rect-1"/>
                                <rect x="6.41" y="6.27" width="54" height="76" rx="5" ry="5" className="card-rect-2"/>
                            </g>
                            <path
                                d="M271.36,43.89c-2.83,0-9.55,6.72-9.55,9.55,0-2.83-6.72-9.55-9.55-9.55,2.83,0,
                                9.55-6.72,9.55-9.55C261.81,37.17,268.53,43.89,271.36,43.89Z"
                                transform="translate(-228.4 0.09)"
                                className="card-red"
                            />
                            <g id="3cb033ef-9166-4ec5-8cca-6b37929f3d2c" data-name="Number high">
                                <path
                                    d="M246,27.54c-1.27,0-4.3,3-4.3,4.3,0-1.27-3-4.3-4.3-4.3,1.27,0,4.3-3,
                                    4.3-4.3C241.72,24.52,244.74,27.54,246,27.54Z"
                                    transform="translate(-228.4 0.09)"
                                    className="card-red"
                                />
                                <text transform="translate(9.55 22.14)" className="card-red card-digit">
                                    {this.props.card[0]}
                                </text>
                            </g>
                            <g id="dcd80689-f491-456f-950d-327c7ff45193" data-name="Number low copy 3">
                                <text transform="translate(57.27 68.09) rotate(180)" className="card-red card-digit">
                                    {this.props.card[0]}
                                </text>
                                <path
                                    d="M286.2,61.73c-1.27,0-4.3,3-4.3,4.3,0-1.27-3-4.3-4.3-4.3,1.27,0,4.3-3,
                                    4.3-4.3C281.91,58.7,284.93,61.73,286.2,61.73Z"
                                    transform="translate(-228.4 0.09)"
                                    className="card-red"
                                />
                            </g>
                        </g>
                    </>);
                break;
                // CLUBS
            case 'c':
                cardGraphic = (<>
                    <title>card-clubs</title>
                        <g id="a08d324b-7b80-48b0-87f3-15f3d72deae0" data-name="Club card">
                            <g>
                                <rect x="7.16" y="6.9" width="54" height="76" rx="5" ry="5" className="card-rect-1"/>
                                <rect x="7.16" y="6.9" width="54" height="76" rx="5" ry="5" className="card-rect-2"/>
                            </g>
                            <path
                                d="M196.89,41.9a5.49,5.49,0,0,0-1.17.14,4.26,4.26,0,0,0,1.42-3.14,5,5,0,0,0-10,0A4.26,
                                4.26,0,0,0,188.56,42a5.49,5.49,0,0,0-1.17-.14,4.77,4.77,0,0,0-5,4.5,4.77,4.77,0,0,0,5,
                                4.5,5.13,5.13,0,0,0,4-1.81,10.9,10.9,0,0,1-2,5.32h5.5a10.9,10.9,0,0,1-2-5.32,5.13,5.13,
                                0,0,0,4,1.81,4.77,4.77,0,0,0,5-4.5A4.77,4.77,0,0,0,196.89,41.9Z"
                                transform="translate(-157.98 0.09)"
                                className="card-black"
                            />
                            <g id="e375a035-2353-4cfb-a60d-c6e2572b9514" data-name="Number high copy 3">
                                <path
                                    d="M174.18,26.41a2.47,2.47,0,0,0-.53.06,1.92,1.92,0,0,0,.64-1.41,2.26,2.26,0,0,
                                    0-4.5,0,1.92,1.92,0,0,0,.64,1.41,2.47,2.47,0,0,0-.53-0.06,2,2,0,1,0,0,4.05,2.31,
                                    2.31,0,0,0,1.79-.81,4.9,4.9,0,0,1-.89,2.4h2.47a4.9,4.9,0,0,1-.89-2.4,2.31,2.31,0,
                                    0,0,1.79.81A2,2,0,1,0,174.18,26.41Z"
                                    transform="translate(-157.98 0.09)"
                                    className="card-black"
                                />
                                <text transform="translate(10.3 22.14)" className="card-black card-digit">
                                    {this.props.card[0]}
                                </text>
                            </g>
                            <g id="dcd80689-f491-456f-950d-327c7ff45193" data-name="Number low copy 3">
                                <text transform="translate(58.02 68.18) rotate(180)" className="card-black card-digit">
                                    {this.props.card[0]}
                                </text>
                                <path
                                    d="M210.1,62.85a2.47,2.47,0,0,0,.53-0.06A1.92,1.92,0,0,0,210,64.2a2.26,2.26,0,0,0,
                                    4.5,0,1.92,1.92,0,0,0-.64-1.41,2.47,2.47,0,0,0,.53.06,2,2,0,1,0,0-4.05,2.31,2.31,0,
                                    0,0-1.79.81,4.9,4.9,0,0,1,.89-2.4H211a4.9,4.9,0,0,1,.89,2.4,2.31,2.31,0,0,
                                    0-1.79-.81A2,2,0,1,0,210.1,62.85Z"
                                    transform="translate(-157.98 0.09)"
                                    className="card-black"
                                />
                            </g>
                        </g>
                    </>);
                break;
            default:
                return (<> </>);
        }
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
                    { cardGraphic }
                </svg>
            </div>

        );
    }
}

Card.propTypes = {
    card: (props, propName) => {
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
