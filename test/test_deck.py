import pytest
from src.сard import Card
from src.deck import Deck

cards = [Card.load('tbt'), Card.load('ete'), Card.load('aab'), Card.load('ttt')]

def test_init():
    d = Deck(cards)
    assert d.cards == cards

def test_save():
    d = Deck(cards=cards)
    assert d.save() == 'ttb tee baa ttt'  
    d = Deck(cards=[])
    assert d.save() == ''

def test_load():
    d = Deck.load('tbt ete aab ttt')
    expected_deck = Deck(cards)
    assert d == expected_deck

def test_draw_card():
    d1 = Deck.load('tbt ete aab ttt')
    d2 = Deck.load('tbt ete aab')
    c = d1.draw_card()
    assert c == Card.load('ttt')
    assert d1 == d2


