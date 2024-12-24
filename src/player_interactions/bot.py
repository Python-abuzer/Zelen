from src.сard import Card
from src.hand import Hand
from src.player import Player
from src.price import Price
from src.player_interaction import PlayerInteraction


class Bot(PlayerInteraction):
    @classmethod
    def choose_card(
        cls, hand: Hand, cards: list[Card],price: Price, hand_counts: list[int] | None = None
    ) -> Card:
        """
        Берет первую карту
        """
        return cards[0]