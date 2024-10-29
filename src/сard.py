"Карты"
class Card:
    VEGETABLES = ["t", "b", "c", "e", "a"]  # tomato,broccoli,corn,eggplant,apple
    QUANTITY = 3

    def __init__(self, **kwargs):
        if not kwargs or sum(kwargs.values()) != self.QUANTITY:
            raise ValueError
        for veg in self.VEGETABLES:
            setattr(self, veg, kwargs.get(veg, 0))

    def __repr__(self):
        return ''.join([self.t * 't', self.b * 'b', self.c * 'c', self.e * 'e', self.a * 'a'])

    def __eq__(self, other):
        return self.t == other.t and self.b == other.b and self.c == other.c and self.e == other.e and self.a == other.a

    def save(self):
        return repr(self)

    @staticmethod
    def load(text: str):
        return Card(t=text.count('t'), b=text.count('b'), c=text.count('c'), e=text.count('e'), a=text.count('a'))

    @staticmethod
    def all_cards(VEGETABLES: list[str] | None):
        if VEGETABLES is None:
            VEGETABLES = Card.VEGETABLES
        cards = [Card.load(veg1 * 2 + veg2 * 1) for veg1 in VEGETABLES for veg2 in VEGETABLES]
        cards += cards.copy()
        r_card = [Card.load(veg * 3) for veg in VEGETABLES]
        for card in r_card:
            cards.remove(card)
        return cards