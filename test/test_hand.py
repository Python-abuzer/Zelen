import pytest
from src.hand import Hand
from src.сard import Card
from src.price import Price

cards = [Card.load('tbb'), Card.load('tee'), Card.load('aaa')]

def test_init():
    d = Hand(cards)
    assert d.cards == cards


def test_save():
    h = Hand(cards=cards)
    assert h.save() == 'tbb tee aaa'


def test_load():
    d = Hand.load('tbb tee aaa')
    exp_d = Hand(cards)
    assert d == exp_d


def test_add_card():
    h = Hand.load('tbb tee aaa')
    h.add_card(Card.load('ttt'))
    assert h.save() == 'tbb tee aaa ttt' 

    h.add_card(Card.load('eee'))
    assert h.save() != 'tbb tee aaa bee'
    assert h.save() == 'tbb tee aaa eee'

def test_score():
    h = Hand(cards=[Card.load('tbb')])
    p = {"t": 2, "b": 3, "c": 3, "e": 4, "a": 5}  # Словарь с ценами
    assert h.score(p) == 2 + 3 + 3