from game_engine import constants as const

game_state_schema = {
    "type": "object",
    "properties": {
        "stage": {
            "type": "string",
            "enum": ["PREFLOP", "FLOP", "TURN", "RIVER", ""]
        },
        "dealer_seat": {
            "type": "integer",
            "minimum": 0
        },
        "sb_seat": {
            "type": "integer",
            "minimum": 0
        },
        "bb_seat": {
            "type": "integer",
            "minimum": 0
        },
        "small_blind": {
            "type": "number",
            "minimum": 0
        },
        "big_blind": {
            "type": "number",
            "minimum": 0
        },
        "community_cards": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": const.DECK,
            },
            "uniqueItems": True,
            "maxItems": 5
        },
        "pot": {
            "type": "number",
            "minimum": 0
        },
        "action_on_seat": {
            "type": "integer",
            "minimum": 0
        },
        "players": {
            "type": "array",
            "uniqueItems": True,
            "items": {
                "type": "object",
                "properties": {
                    "seatnumber": {
                        "type": "integer",
                        "minimum": 1
                    },
                    "status": {
                        "type": "string",
                        "enum": ["ACTIVE", "FOLDED", "INACTIVE", "WAITING", "ALL_IN"]
                    },
                    "last_action": {
                        "type": "string",
                        "enum": ["BET", "CALL", "CHECK", "FOLD", "RAISE", "POST_BB", "POST_SB", ""]
                    },
                    "stack": {
                        "type": "number",
                        "minimum": 0
                    },
                    "bet": {
                        "type": "number",
                        "minimum": 0
                    }
                },
                "required": [
                    "seatnumber",
                    "status",
                    "stack",
                ]
            }
        },
        "observers": {
            "type": "array",
            "uniqueItems": True,
            "items": {
                "type": "string"
            }
        }
    },
    "required": [
        "stage",
        "dealer_seat",
        "sb_seat",
        "bb_seat",
        "small_blind",
        "big_blind",
        "community_cards",
        "pot",
        "action_on_seat",
        "players",
        "observers"
    ]
}
