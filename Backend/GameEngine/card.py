class Card:
    def __init__(self, suite, rank):
        self._suite = suite
        self._rank = rank

    def __str__(self):
        if (self._suite and self._rank):
            return self._rank + ' of ' + self._suite
        return ''
