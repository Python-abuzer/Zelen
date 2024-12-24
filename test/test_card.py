import pytest
from src.сard import Card

def test_init():
    c = Card(t=2, a=1)
    assert c.t == 2
    assert c.a == 1
    assert c.b == 0
    assert c.e == 0
    assert c.c == 0

def test_save():
    c = Card(t=3)
    assert repr(c) == 'ttt'
    assert c.save() == 'ttt'
    c = Card(c=2, a=1)
    assert repr(c) == 'cca'
    assert c.save() == 'cca'

def test_load():
    z = 'ttb'
    x = 'ttt'
    c = 'eec'
    d = Card.load(x)
    y = Card.load(z)
    q = Card.load(c)
    assert y == Card(t=2, b=1)
    assert d == Card(t=3)
    assert q == Card(e=2, c=1)

def test_eq():
    c1 = Card(t=3)
    c2 = Card(t=3)
    c3 = Card(b=1, e=2)
    c4 = Card(c=2, a=1)
    assert c1 == c2
    assert c1 != c3
    assert c2 != c3
    assert c1 != c4

def test_all_cards():
    cards = Card.all_cards(['t', 'b'])
    expected_cards = [
        Card(t=2, b=1),
        Card(t=1, b=2),
        Card(t=3, b=0),
        Card(t=2, b=1),
        Card(t=1, b=2),
        Card(b=3, t=0)
    ]
    assert cards == expected_cards