from django.db import models
from django.core.validators import MinValueValidator


class Table(models.Model):
    """Model for the poker tables"""

    CASH = 'C'
    TOURNAMENT = 'T'
    ACTIVE = 'A'
    WAITING = 'W'
    CLOSED = 'C'

    table_types = [(CASH, 'Cash'), (TOURNAMENT, 'Tournament')]
    status = [(ACTIVE, 'Active'), (WAITING, 'Waiting'), (CLOSED, 'Closed')]

    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    small_blind = models.FloatField(validators=[MinValueValidator(0)])
    big_blind = models.FloatField(validators=[MinValueValidator(0)])
    hand_count = models.BigIntegerField(default=0)
    average_pot = models.FloatField(default=0.0)
    max_players = models.PositiveSmallIntegerField(default=9)
    type = models.CharField(max_length=1, choices=table_types, default='C')
    status = models.CharField(max_length=1, choices=status, default='W')
    dealer_seat = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
    sb_seat = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
    bb_seat = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
