from typing import Self
from src.сard import Card
import random

class Deck:
    def __init__(self, cards: list[Card] | None ):
        if cards is  None:
            self.cards = []
        else:
            self.cards = cards

    def __repr__(self):
        return self.save()

    def save(self) -> str:
        return ' '.join([card.save() for card in self.cards])
       
    
    def __eq__(self, other: Self):
        if isinstance(other, Deck):
            return self.cards == other.cards
        else:
            return False
    
    @classmethod
    def load(cls, data: list[str]):
        cards = [Card.load(card_str) for card_str in data.split()]
        return cls(cards)
    
    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("Колода пуста")
        return self.cards.pop()
    
    def shuffle(self):
        random.shuffle(self.cards)