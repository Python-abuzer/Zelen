from src.сard import Card
from src.hand import Hand
from src.player import Player
from src.price import Price
from src.player_interaction import PlayerInteraction


class Human(PlayerInteraction):
    @classmethod
    def choose_card(
       cls, hand: Hand, cards: list[Card],price: Price, hand_counts: list[int] | None = None
    ) -> Card:
        """
        Принимает решение, какую карту с руки играть.
        Возвращает карту или None, если нельзя играть карту с руки.
        """
        
        while True:
            try:
                card_text = input("Choose card: ")
                card = Card.load(card_text)
                if card in cards:
                    return card
                else:
                    print('Эту карту нельзя играть.')
            except ValueError:
                print("Карта задется,как 'ttb'.")