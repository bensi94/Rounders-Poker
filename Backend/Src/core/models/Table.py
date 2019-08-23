from django.db import models


class Table(models.Model):
    """Model for the poker tables"""

    table_types = [('C', 'Cash'), ('T', 'Tournament')]
    status = [('A', 'Active'), ('W', 'Waiting'), ('C', 'Closed')]

    name = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    small_blind = models.PositiveIntegerField()
    big_blind = models.PositiveIntegerField()
    hand_count = models.BigIntegerField()
    average_pot = models.FloatField()
    max_players = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=1, choices=table_types)
    status = models.CharField(max_length=1, choices=status)
