from abc import ABC, abstractmethod
from src.сard import Card
from src.hand import Hand
from src.price import Price

class PlayerInteraction(ABC):
    @classmethod
    @abstractmethod
    def choose_card(
            cls, hand: Hand, cards: list[Card],price: Price, hand_counts: list[int] | None = None
    ) -> Card:
        pass