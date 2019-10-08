SUITES = ["clubs", "diamonds", "hearts", "spades"]
RANKS = ["ace", "2", "3", "4", "5", "6", "7", "8", "9",
         "10", "jack", "queen", "king"]

DECK = [
    "Ah", "2h", "3h", "4h", "5h", "6h", "7h",  # HEARTS
    "8h", "9h", "Th", "Jh", "Qh", "Kh",
    "As", "2s", "3s", "4s", "5s", "6s", "7s",  # SPADES
    "8s", "9s", "Ts", "Js", "Qs", "Ks",
    "Ad", "2d", "3d", "4d", "5d", "6d", "7d",  # DIAMONDS
    "8d", "9d", "Td", "Jd", "Qd", "Kd",
    "Ac", "2c", "3c", "4c", "5c", "6c", "7c",  # CLUBS
    "8c", "9c", "Tc", "Jc", "Qc", "Kc"
]

PENDING = 'PENDING'
RUNNING = 'RUNNING'
STATUS_ACTIVE = 'ACTIVE'
STATUS_FOLDED = 'FOLDED'
STATUS_WAITING = 'WAITING'
STATUS_INACTIVE = 'INACTIVE'
STATUS_ALL_IN = 'ALL_IN'

# STAGES
PREFLOP = 'PREFLOP'
FLOP = 'FLOP'
TURN = 'TURN'
RIVER = 'RIVER'

WAIT = True
RUN = False


# ACTION NAMES
POST_SB = 'POST_SB'
POST_BB = 'POST_BB'
BET = 'BET'
CALL = 'CALL'
CHECK = 'CHECK'
FOLD = 'FOLD'
RAISE = 'RAISE'
