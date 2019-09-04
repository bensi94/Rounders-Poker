from django.db import models
from django.contrib.postgres.fields import JSONField

from core.models.validators.json_schema_validator import JsonSchemaValidator
from core.models.table import Table


class Hand(models.Model):
    """Model for each poker Hand"""

    table = models.ForeignKey(Table, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    history = JSONField(default=dict, validators=[JsonSchemaValidator(
        schema='hand_history_schema')])
