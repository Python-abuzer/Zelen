import pytest 
from src.сard import Card

def test_init():
    c = Card("c",2)
    assert c.vegs == "c"
    assert c.quant == 2

def test_save():
    c = Card('c', 3)
    assert repr(c) == 'c3'
    assert c.save() == 'c3'
    c = Card('b', 2)
    assert repr(c) == 'b2'
    assert c.save() == 'b2'

def test_load():
    s = 'ttt'
    c = Card.load(s)
    assert c == Card('t', 3)

def test_eq():
    c1 = Card('c', 2)
    c2 = Card('c', 2)
    c3 = Card('b', 3)
    assert c1 == c2
    assert c1 != c3
    assert c2 != c3