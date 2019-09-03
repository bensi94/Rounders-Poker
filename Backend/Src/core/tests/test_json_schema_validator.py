from django.test import TestCase
from core.models.validators.json_schema_validator import JsonSchemaValidator
from django.core.exceptions import ValidationError

from core.tests.constants import valid_history_example, \
    invalid_history_seatnumber_required, invalid_history_invalid_stage


class JsonSchemaValidatorTests(TestCase):

    def test_valid_hand_history(self):
        """Test valid hand history"""
        instance = JsonSchemaValidator('hand_history_schema')
        instance(valid_history_example)

    def test_invalid_seatnumber_required(self):
        """
        Tests that seatnumber is required in seats array
        """
        expected_msg = \
            '["Error validating JSON: \'seatnumber\' is a required property"]'

        with self.assertRaisesMessage(ValidationError, expected_msg):
            instance = JsonSchemaValidator('hand_history_schema')
            instance(invalid_history_seatnumber_required)

    def test_invalid_stage(self):
        """
        Tests that the stage is valid
        """
        expected_msg = \
            '["Error validating JSON: \'HELLO\' is not one of [\'PREFLOP\', '\
            '\'FLOP\', \'TURN\', \'RIVER\']"]'

        with self.assertRaisesMessage(ValidationError, expected_msg):
            instance = JsonSchemaValidator('hand_history_schema')
            instance(invalid_history_invalid_stage)
