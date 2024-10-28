"Рука"
import typing
from src.сard import Card
from src.price import Price

class Hand:
    def __init__(self, cards: list[Card] = None):
        self.cards = cards if cards is not None else []

    def save(self) -> str:
        scards = [c.save() for c in self.cards]
        s = ' '.join(scards)
        return s
    def __repr__(self):
        return self.save()

    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, card: Card):
        if card in self.cards:
            self.cards.remove(card)

    def get_cards(self) -> list[Card]:
        return self.cards

    def score(self, price: Price) -> int:
        total_score = 0
        for card in self.cards:
            total_score += card.score(price)
        return total_score
    
    