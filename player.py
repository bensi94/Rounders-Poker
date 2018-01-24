class Player:

    _name = None
    _stack = 0
    _isDealer = False
    _hand = []

    def __init__(self, name, startingStack, isDealer):
        self._name = name
        self._stack = startingStack
        self._isDealer = isDealer
        self._isSB = isDealer
        self._isBB = not isDealer

    def payBlind(self, blind):
        if self._stack < blind:
            blind = self._stack
            self._stack = 0
        else:
            self._stack = self._stack - blind
        return blind
