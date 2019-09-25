from threading import Thread
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from queue import Queue
from functools import wraps
import logging

from game_engine.player import Player


class GameController(Thread):
    """
    Each game controller control single table flow. For now it's meant for cash
    game tables, might change to layer supertype pattern
    when tournaments come in later

    The controller inherits from the standard Thread class and runs on it own
    thread. The controller has decorator that should be placed all event
    functions that are called on the thread.
    """

    def __init__(self, table_id):
        Thread.__init__(self)
        self._players = {}
        self._observers = {}
        self._table_id = table_id
        self._runing = True
        self._channel_layer = get_channel_layer()
        self._fnQueue = Queue()
        self._first = True
        self._game_state = {}
        self._hand = None

    def run(self):
        while self._runing:
            logging.info(self._fnQueue)
            fn, a, kw = self._fnQueue.get()
            fn(self, *a, **kw)
            self._fnQueue.task_done()
            self.add_next_action()

    # This function is uses the current game state to determine what should be the next action it
    # adds the next action to the function Queue of thread where they will run in order.
    # If it does not add anything to the function Queue it means that the controller is waiting
    # for external call, for example user to do.
    # The point of it is the controller will never have to let any external actions starve
    def add_next_action(self):
        if not self._game_state:
            pass

    # This is decorater that takes the function being called and adds
    # it to the queue of functions that the controller is running.
    # If no functions are in the queue it waits until a function is added
    def add_to_thread_queue(fn):
        @wraps(fn)
        def wrapper(self, *a, **kw):
            self._fnQueue.put((fn, a, kw))
        return wrapper

    @add_to_thread_queue
    def add_player(self, player, buy_in, seat_number, channel_id):
        # User can not be a player and observer at the same time
        if player in self._observers:
            self._observers.remove(player)
        self._players[player] = {
            "player": Player(buy_in, seat_number),
            "channel_id": channel_id
        }
        self.broadcast_state()

    @add_to_thread_queue
    def add_observer(self, observer, channel_id):
        self._observers[observer] = {
            "channel_id": channel_id
        }
        self.broadcast_state()

    def broadcast_state(self):
        async_to_sync(self._channel_layer.group_send)(
            str(self._table_id), {"type": "state_update", "state": self.render()}
        )

    def render(self):
        return {
            "players": {
                player_id: player['player'].get_player_obj()
                for player_id, player in self._players.items()
            },
            "observers": [observer_key for observer_key, obj in self._observers]
        }

    @add_to_thread_queue
    def set_up_table(self):
        if len(self._players) >= 2:
            pass

    # This function uses the button to order the players in right order
    # Button player last, others before
    # def get_button_ordered_players(self):
    #     button = self._table.get_button()
    #     players_positions = sorted(self._players.keys())
    #     more_then_button = []
    #     less_then_button = []

    #     # Here we do a little tricks around the button to position the
    #     # players in the right order
    #     for position in players_positions:
    #         if position < button:
    #             less_then_button.append(self._players[position])
    #         elif position > button:
    #             more_then_button.append(self._players[position])

    #     # If there are players in higher seat then button they come first
    #     # Then seat 1 to button and the button seat last
    #     return more_then_button + less_then_button + [self._players[button]]

    @add_to_thread_queue
    def stop_thread(self):
        self._runing = False
