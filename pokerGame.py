from deck import Deck
from ui import UI
from player import Player

class PokerGame:

    _ui = UI()
    _deck = Deck()
    _player1 = None
    _player2 = None
    _BB = 20
    _SB = 10
    _pot = 0

    def __init__(self):
        players = self._ui.getPlayerNames()
        startingStack = 10000
        isDealer = True
        self._player1 = Player(players[0], startingStack, isDealer)
        self._player2 = Player(players[1], startingStack, isDealer)
        self._ui.welcome(self._player1, self._player2, startingStack)
        self.runGame()

    def hand(self):
        self.payBlinds()
        deck.deal()

    def payBlinds(self):
        if self._player1._isDealer:
            self._pot += self._player1.payBlind(self._BB) #Pay Big blind
            self._pot += self._player2.payBlind(self._SB) #Pay Small blind
        else:
            self._pot += self._player1.payBlind(self._SB) #Pay Small blind
            self._pot += self._player2.payBlind(self._BB) #Pay Big blind

    def runGame(self):
        while self._player1._stack > 0 and self._player2._stack > 0:
            self.hand()
            print(self._pot)

x = PokerGame()
