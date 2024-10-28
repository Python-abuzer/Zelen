"Карты"
import pytest
class Card:
    VEGETABLES = ["t","b","co","e","cr"] #tomato,broccoli,corn,eggplant,carrot
    QUANTITY = 3

    def __init__(self,**kwargs):
        if not kwargs or sum(kwargs.values()) != self.QUANTITY:
            raise ValueError
        for veg in self.VEGETABLES:
            setattr(self, veg, kwargs[veg])
    def __repr__(self):
        return ''.join([veg * getattr(self, veg) for veg in self.VEGETABLES])
    
    def __eq__(self, other):
       return self.t == other.t and self.b == other.b and self.c == other.c and self.e == other.e and self.cr == other.cr

    def save(self):
        return repr(self)   
    
    @staticmethod
    def load(text: str):
        return Card(text.count('t'), text.count('b'), text.count('co'), text.count('e'), text.count('cr'))  
    
    @staticmethod
    def all_cards(VEGETABLES: list[str] | None):
        if VEGETABLES is None:
            VEGETABLES = Card.VEGETABLES
        cards = [Card.load(veg1 * 2 + veg2 * 1) for veg1 in VEGETABLES for veg2 in VEGETABLES]
        cards = list(set(cards))
        r_card = [Card.load(veg * 3) for veg in VEGETABLES]
        for card in r_card:
            if card in cards:
                cards.remove(card)
        return cards
    
def test_init():
    c = Card(t=2, co=1)
    assert c.t == 2
    assert c.c0 == 1
    assert c.b == 0
    assert c.e == 0
    assert c.cr == 0


def test_save():
    c = Card(t=3)
    assert repr(c) == 'ttt'
    assert c.save() == 'ttt'
    c = Card(c0=2, cr=1)
    assert repr(c) == 'cococr'
    assert c.save() == 'cococr'


def test_load():
    z = 'ttb'
    x = 'ttt'
    c = 'eecr'
    d = Card.load(x)
    y = Card.load(z)
    q = Card.load(c)
    assert y == Card(t=2, b=1)
    assert d == Card(t=3)
    assert q == Card(e=2, cr=1)


def test_eq():
    c1 = Card(t=3)
    c2 = Card(t=3)
    c3 = Card(b=1, e=2)
    c4 = Card(co=2, cr=1)
    assert c1 == c2
    assert c1 != c3
    assert c2 != c3
    assert c1 != c4

def test_all_cards():
    cards = Card.all_cards(['t', 'b'])
    expected_cards = [
        Card.load('ttb'),
        Card.load('tbb'),
        Card.load('ttt'),
        Card.load('ttb'),
        Card.load('tbb'),
        Card.load('bbb')
    ]
    assert cards == expected_cards