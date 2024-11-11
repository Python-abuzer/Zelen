"Рука"
import typing
from src.сard import Card
from src.price import Price

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
    
    