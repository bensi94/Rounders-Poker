class Card:
    _suite = None
    _rank = None

    def __init__(self, suite, rank):
        self._suite = suite
        self._rank = rank

    def isCard(self):
        if (self._suite and self._rank):
            return self._rank + ' of ' + self._suite
        return ''
