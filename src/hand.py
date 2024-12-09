"Рука"
from typing import Self
from src.сard import Card

class Hand:
    def __init__(self, cards: list[Card] = None):
        if cards is not None:
            self.cards = cards  
        else: 
            self.cards = []

    def __repr__(self):
        return self.save()
    
    def save(self) -> str:
        return ' '.join(card.save() for card in self.cards)
    
    def __eq__(self, other: Self):
        if isinstance(other, Hand):
            return self.cards == other.cards
        else:
            return False
    
    @classmethod
    def load(cls, data: str):
        cards = [Card.load(card_str) for card_str in data.split()]
        return cls(cards)
    
    def add_card(self, card: Card):
        self.cards.append(card)

    def __getattr__(self, name):
        if name in Card.VEGETABLES:
            return sum(getattr(card, name) for card in self.cards)
        else:
            raise AttributeError

    def score(self, other):
        return sum(getattr(self, v) * getattr(other, v) for v in Card.VEGETABLES)
    
    
    