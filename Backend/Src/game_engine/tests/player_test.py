from game_engine.player import Player
from game_engine.card import Card
from game_engine.constants import STATUS_ACTIVE, STATUS_FOLDED


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
    assert retrun_val is True


def test_bet_invalid():
    player = Player(100)

    retrun_val = player.bet(200)

    assert player._stack == 100
    assert player._bet == 0
    assert retrun_val is False


def test_fold():
    player = Player(100)

    player.bet(50)
    player.fold()

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


def test_pay_blind_full():
    stack = 100
    blind = 20

    player = Player(stack)
    player.pay_blind(blind)

    assert player._bet == blind
    assert player._stack == stack - blind


# Test when blind is more than stack
def test_pay_blind_less():
    stack = 10
    blind = 20

    player = Player(stack)
    player.pay_blind(blind)

    assert player._bet == stack
    assert player._stack == 0


def test_reset_bet():
    player1 = Player(100)
    player1.bet(20)
    player1.reset_bet()

    assert player1._bet == 0
