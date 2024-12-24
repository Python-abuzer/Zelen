import inspect
import json
from src.сard import Card
from src.price import Price
from src.deck import Deck
from src.hand import Hand
from src.player import Player
from src.gamestate import GameState
from pathlib import Path
from src.player_interaction import PlayerInteraction
import src.player_interactions as all_player_types

class GameServer:
    def __init__(self, player_types, game_state):
        self.game_state: GameState = game_state
        self.player_types: dict = player_types

    @classmethod
    def load_game(cls):
        # TODO: выбрать имя файла
        filename = 'zelen.json'
        with open(Path(__file__).parent / filename, 'r') as fin:
            data = json.load(fin)
            game_state = GameState.load(data)
            print(game_state.save())
            player_types = {}
            for player, player_data in zip(game_state.players, data['players']):
                kind = player_data['kind']
                kind = getattr(all_player_types, kind)
                player_types[player] = kind
            return GameServer(player_types=player_types, game_state=game_state)


    def save(self):
        filename = 'zelen2.json'
        data = self.save_to_dict()
        with open(filename, 'w') as fout:
            json.dump(data, fout, indent=4)
            print(json.dumps(data, indent=4))

    def save_to_dict(self):
        # {'top': 'r2', 'deck': 'r0 g2 y1', 'current_player_index': 1, 'players': [{'name': 'Alex', 'hand': 'g5 b5', 'score': 0}, {'name': 'Bob', 'hand': 'y7', 'score': 1}]}
        data = self.game_state.save()
        for player_index, player in enumerate(self.player_types.keys()):
            player_interaction = self.player_types[player]
            data['players'][player_index]['kind'] = self.player_types[player].__name__
        return data


    @classmethod
    def new_game(cls, player_types: dict):
        # Shuffle the deck and deal the top card
        deck = Deck(cards=None)
        top = deck.draw_card()
        game_state = GameState(list(player_types.keys()), deck, top)

    @classmethod
    def get_players(cls):
        player_count = cls.request_player_count()

        player_types = {}
        for p in range(player_count):
            name, kind = cls.request_player()
            player = Player(name, Hand())
            player_types[player] = kind
        return player_types

    @staticmethod
    def request_player_count() -> int:
        while True:
            try:
                player_count = int(input("How many players?"))
                if 2 <= player_count <= 10:
                    return player_count
            except ValueError:
                pass
            print("Please input a number between 2 and 10")

    @staticmethod
    def request_player() -> (str, PlayerInteraction):
        """Возвращает имя и тип игрока."""

        """Разрешенные типы игроков из PlayerInteraction."""
        # Getting all names of subclasses of PlayerInteraction from  all_player_types
        player_types = []
        for name, cls in inspect.getmembers(all_player_types):
            if inspect.isclass(cls) and issubclass(cls, PlayerInteraction):
                player_types.append(cls.__name__)
        player_types_as_str = ', '.join(player_types)

        while True:
            name = input("How to call a player?")
            if name.isalpha():
                break
            print("Name must be a single word, alphabetic characters only")

        while True:
            try:
                kind = input(f"What kind of player is it ({player_types_as_str})?")
                kind = getattr(all_player_types, kind)
                break
            except AttributeError:
                print(f"Allowed player types are: {player_types_as_str}")
        return name, kind

    def run(self):
     for round in range(6):
          # положить карты на стол

          for player in self.game_state.players:
                card = self.player_types[player].choose_card(self.game_state.cards, ...)
                # эту карту убрать со стола
                self.game_state
def __main__():
    load_from_file = True
    if load_from_file:
        server = GameServer.load_game()
        server.save()
    else:
        server = GameServer.new_game(GameServer.get_players())
    server.run()


if __name__ == "__main__":
    __main__()