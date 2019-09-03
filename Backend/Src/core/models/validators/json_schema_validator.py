from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from jsonschema import validate, ValidationError as JSONValidationError

from core.constants import deck, game_stages, player_actions, player_statuses

schemas = {
    'hand_history_schema': {
        'type': 'object',
        'properties': {
            'seats': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'seatnumber': {
                            'type': 'integer',
                            'minimum': 1,
                            'unique': True
                        },
                        'player': {
                            'type': 'integer',
                            'minimum': 1,
                            'unique': True
                        }
                    },
                    'required': ['seatnumber', 'player']
                },
                'uniqueItems': True
            },
            'dealer_seat': {
                'type': 'integer',
                'minimum': 1
            },
            'SB_seat': {
                'type': 'integer',
                'minimum': 1
            },
            'BB_seat': {
                'type': 'integer',
                'minimum': 1
            },
            'SB': {
                'type': 'number',
                'minimum': 0
            },
            'BB': {
                'type': 'number',
                'minimum': 0
            },
            'states': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'stage': {
                            'type': 'string',
                            'enum': game_stages
                        },
                        'timestamp': {
                            'type': 'string',
                            'format': 'date-time'
                        },
                        'action_on_seat': {
                            'type': 'integer',
                            'minimum': 1
                        },
                        'community_cards': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': deck,
                            },
                            'uniqueItems': True,
                            'maxItems': 5
                        },
                        'pot': {
                            'type': 'number',
                            'minimum': 0
                        },
                        'players': {
                            'type': 'array',
                            'items': {
                                'seatnumber': {
                                    'type': 'integer',
                                    'minimum': 1
                                },
                                'status': {
                                    'type': 'string',
                                    'enum': player_statuses
                                },
                                'last_action': {
                                    'type': 'string',
                                    'enum': player_actions
                                },
                                'stack': {
                                    'type': 'number',
                                    'minimum': 0
                                },
                                'bet': {
                                    'type': 'number',
                                    'minimum': 0
                                }
                            },
                            'required': ['seatnumber', 'status', 'last_action',
                                         'stack', 'bet']
                        }
                    },
                    'required': ['stage', 'timestamp', 'action_on_seat',
                                 'community_cards', 'pot']
                }
            }
        },
        'required': ['seats', 'dealer_seat', 'SB_seat',
                     'BB_seat', 'SB', 'BB', 'states']
    }
}


@deconstructible
class JsonSchemaValidator:

    def __init__(self, schema):
        self.schema = schemas[schema]

    def __call__(self, json_value):

        try:
            validate(json_value, self.schema)
        except JSONValidationError as error:
            raise ValidationError('Error validating JSON: ' + error.message)
