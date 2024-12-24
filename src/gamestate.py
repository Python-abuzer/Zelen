
from src.сard import Card
from src.price import Price
from src.deck import Deck
from src.hand import Hand
from src.player import Player

class GameState:
    MAX_ROUND = 6
    MIN_PLAYERS = 2
    MAX_PLAYERS = 6

    def __init__(self,players: list[Player], deck: Deck, price: Price, cards: list[Card], current_player: int = 0,round_i: int = 1):
        if len(players) < self.MIN_PLAYERS or len(players) > self.MAX_PLAYERS:
            raise ValueError("Некорректное количество игроков")
        self.players: list[Player] = players
        self.deck: Deck = deck
        self._current_player: int = current_player
        self.price = price
        self.cards: list[Card] = cards
        self.round_i: int = round_i

    def current_player(self) -> Player:
        return self.players[self._current_player]

    def __eq__(self, other):
        if not isinstance(other, GameState):
            return False
        return (
            self.players == other.players
            and self.deck == other.deck
            and self._current_player == other._current_player
            and self.price == other.price
            and self.round_i == other.round_i
            and self.cards == other.cards
        )

    def save(self) -> dict:
        return {
            "Price": self.price.save(),
            "Deck": self.deck.save(),
            "CurrentPlayerIndex": self._current_player,
            "players": [p.save() for p in self.players],
            "Round": self.round_i,
            "cards": [card.save() for card in self.cards],
        }

    @classmethod
    def load(cls, data: dict):
        players = [Player.load(p) for p in data["players"]]
        return cls(
            players=players,
            deck=Deck.load(data["Deck"]),
            price=Price.load(data["Price"]),
            cards = [Card.load(s) for s in data["cards"]],
            current_player=int(data["CurrentPlayerIndex"]),
            round_i=int(data["Round"])   
        )

    def next_player(self):
        n = len(self.players)
        self._current_player = (self._current_player + 1) % n

    def distribution(self, num_cards_per_player: int = 1): 
        '''Кладет на стол столько карт,сколько игроков + 1'''
        num_cards_per_player = len(self.players) + 1
        for _ in range(num_cards_per_player):
            try:
                card = self.deck.draw_card()
                self.cards.append(card)
            except IndexError:
                print("В колоде кончились карты")
                break

   