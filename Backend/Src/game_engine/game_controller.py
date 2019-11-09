from threading import Thread
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from queue import Queue
from functools import wraps
from jsonschema import validate, ValidationError
import random

from game_engine import constants as const
from game_engine.player import Player
from game_engine.hand import Hand
from core.models.table import Table
from game_engine.utils.game_state_schema import game_state_schema


class GameController(Thread):
    """
    Each game controller control single table flow. For now it's meant for cash
    game tables, might change to layer supertype pattern
    when tournaments come in later

    The controller inherits from the standard Thread class and runs on it own
    thread. The controller has decorator that should be placed all event
    functions that are called on the thread.
    """

    INITIAL_GAME_STATE = {
        "stage": "",
        "dealer_seat": 0,
        "sb_seat": 0,
        "bb_seat": 0,
        "small_blind": 0,
        "big_blind": 0,
        "community_cards": [],
        "pot": 0,
        "action_on_seat": 0
    }

    def __init__(self, table_id):
        Thread.__init__(self)
        self._players = {}
        self._observers = {}
        self._table_id = table_id
        self._runing = True
        self._channel_layer = get_channel_layer()
        self._fnQueue = Queue()
        self._first = True
        self._game_state = self.INITIAL_GAME_STATE
        self._hand = None
        self._seat_order = []
        self._waiting_for_user = False
        self._action_on_player = None

    def run(self):
        while self._runing:
            fn, a, kw = self._fnQueue.get()
            print(fn.__name__)  # USED to for debug

            # The reason why we do this so any function can return const.WAIT (FALSE)
            # if it needs the add_next_action function and the thread to go into wait mode
            # This happens for example everytime we wait for user to do an aciton
            if fn(self, *a, **kw) is None or const.RUN:
                self._waiting_for_user = const.RUN
            else:
                self._waiting_for_user = const.WAIT

            self._fnQueue.task_done()
            self.broadcast_state()
            self.add_next_action()

    # This function is uses the current game state to determine what should be the next action it
    # adds the next action to the function Queue of thread where they will run in order.
    # If it does not add anything to the function Queue it means that the controller is waiting
    # for external call, for example user to do.
    # The point of it is the controller will never have to let any external actions starve
    def add_next_action(self):
        # We don't add any actions if we are waiting for user action
        if self._waiting_for_user:
            return

        if self._game_state['stage'] == '':
            self.setup_table()
        elif self._hand is None:
            self.init_hand()
        elif self._action_on_player is None:
            self.update_table()

    # This is decorater that takes the function being called and adds
    # it to the queue of functions that the controller is running.
    # If no functions are in the queue it waits until a function is added
    def add_to_thread_queue(fn):
        @wraps(fn)
        def wrapper(self, *a, **kw):
            # This is done to prevent the exact same function, with
            # same arguments, to be added to the queue more than once
            if (fn, a, kw) not in list(self._fnQueue.queue):
                self._fnQueue.put((fn, a, kw))
        return wrapper

    @add_to_thread_queue
    def add_player(self, player, buy_in, seatnumber, channel_id):
        # User can not be a player and observer at the same time
        if player in self._observers:
            del self._observers[player]
        self._players[player] = {
            "player": Player(buy_in, seatnumber, player),
            "channel_id": channel_id
        }

    @add_to_thread_queue
    def add_observer(self, observer, channel_id):
        self._observers[observer] = {
            "channel_id": channel_id
        }

    def broadcast_state(self):

        try:
            state = self.render()
            validate(state, game_state_schema)
            async_to_sync(self._channel_layer.group_send)(
                str(self._table_id), {"type": "state_update", "state": self.render()}
            )
            for player in self._players.values():
                async_to_sync(self._channel_layer.send)(
                    player['channel_id'],
                    {
                        'type': 'individual_update',
                        'cards': ''.join(player['player'].cards)
                    }
                )

        except ValidationError as error:
            async_to_sync(self._channel_layer.group_send)(
                str(self._table_id), {"type": "state_update", "error": error.message}
            )

    def render(self):
        return {
            **self._game_state,
            "players": [
                player['player'].get_player_obj()
                for player in self._players.values()
            ],
            "observers": [observer_key for observer_key in self._observers.keys()],
        }

    @add_to_thread_queue
    def setup_table(self):
        """Sets the table up for next hand"""
        if len(self._players) < 2:
            return const.WAIT

        active_count = 0

        table = Table.objects.get(pk=self._table_id)
        seats = []

        # All players that are waiting will be made active
        for player_val in self._players.values():
            player = player_val['player']
            if player.status == const.STATUS_WAITING:
                player.status = const.STATUS_ACTIVE

            if player.status == const.STATUS_ACTIVE:
                seats.append((player.seatnumber, player))
                active_count += 1

        # We need at least 2 Active players to play
        if active_count < 2:
            return const.WAIT

        # We need to sort the seats we have
        seats = sorted(seats)
        dealer_seat = None

        # If we have a dealer_seat it means that we need to move the dealer_seat
        if table.dealer_seat:

            # We try to find next seat (bigger seat) and assign that seat as dealer_seat
            for seatnumber, player in seats:
                if seatnumber > table.dealer_seat:
                    dealer_seat = seatnumber
                    break

            # If we do not find a bigger seat it means that we are at the first (active) seat
            if not dealer_seat:
                dealer_seat = seats[0][0]  # The seatnumber in the tuple
        else:
            dealer_seat = random.choice(seats)[0]

        for i, (seatnumber, player) in enumerate(seats):
            if seatnumber == dealer_seat:
                back = seats[:i+1]
                front = seats[i+1:]
                self._seat_order = [player for (seatnumber, player) in front + back]
                break

        action_on_seat = None

        # If there are only two players the dealer is small blind and first player is big blind
        # If two players the action is on the dealer/small_blind else the action is on bb+1
        if active_count == 2:
            sb_seat = self._seat_order[-1].seatnumber
            bb_seat = self._seat_order[0].seatnumber
            action_on_seat = self._seat_order[1].seatnumber
        else:
            sb_seat = self._seat_order[0].seatnumber
            bb_seat = self._seat_order[1].seatnumber
            action_on_seat = self._seat_order[2].seatnumber

        # Update Game_state
        self._game_state['stage'] = const.PREFLOP
        self._game_state['dealer_seat'] = dealer_seat
        self._game_state['sb_seat'] = sb_seat
        self._game_state['bb_seat'] = bb_seat
        self._game_state['small_blind'] = table.small_blind
        self._game_state['big_blind'] = table.big_blind
        self._game_state['action_on_seat'] = action_on_seat

        # Update Table Model
        table.dealer_seat = dealer_seat
        table.sb_seat = sb_seat
        table.bb_seat = bb_seat
        table.status = Table.ACTIVE
        table.save()

    @add_to_thread_queue
    def init_hand(self):
        self._hand = Hand(
            self._seat_order, (self._game_state['small_blind'], self._game_state['big_blind'])
        )
        self.update_table()

    @add_to_thread_queue
    def update_table(self):
        self._hand.update_table()

    @add_to_thread_queue
    def stop_thread(self):
        self._runing = False
