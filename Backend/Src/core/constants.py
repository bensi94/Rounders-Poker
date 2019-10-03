deck = [
    'Ah', '2h', '3h', '4h', '5h', '6h', '7h',  # HEARTS
    '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh',
    'As', '2s', '3s', '4s', '5s', '6s', '7s',  # SPADES
    '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks',
    'Ad', '2d', '3d', '4d', '5d', '6d', '7d',  # DIAMONDS
    '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd',
    'Ac', '2c', '3c', '4c', '5c', '6c', '7c',  # CLUBS
    '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc'
]

game_stages = ['PREFLOP', 'FLOP', 'TURN', 'RIVER']


player_actions = ['BET', 'CALL', 'CHECK',
                  'FOLD', 'RAISE', 'POST_BB', 'POST_SB', '']

player_statuses = ['ACTIVE', 'FOLDED', 'INACTIVE', 'WAITING', 'ALL_IN']
