from player import Player
from card import Card
from constants import STATUS_ACTIVE, STATUS_FOLDED

def test_give_hand():
    player = Player(100)
    card1 = Card('hearts', '8')
    card2 = Card('spades', '9')

    hand = (card1, card2)
    player.give_hand(hand)

    assert player._hand[0].__str__() == '8 of hearts'
    assert player._hand[1].__str__() == '9 of spades'

def test_get_and_set_seat():
    player = Player(100)

    seat = 5
    player.set_seat(seat)

    assert player.get_seat() == seat

def test_bet_valid():
    player = Player(100)

    retrun_val = player.bet(50)

    assert player._stack == 50
    assert player._bet == 50
    assert retrun_val == True

def test_bet_invalid():
    player = Player(100)

    retrun_val = player.bet(200)

    assert player._stack == 100
    assert player._bet == 0
    assert retrun_val == False


def test_fold():
    player = Player(100)

    player.bet(50)
    player.fold()

    assert player._bet == 0
    assert player._stack == 50
    assert player._status == STATUS_FOLDED


def test_get_state():
    stack = 100
    bet = 50

    player = Player(stack)
    player.bet(bet)

    state = player.get_state()
    
    assert state['status'] == STATUS_ACTIVE
    assert state['stack'] == stack-bet
    assert state['bet'] == bet