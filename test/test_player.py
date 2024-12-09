import pytest
from src.hand import Hand
from src.player import Player

def test_init():
    h = Hand.load('ttt taa bee')
    p = Player(name='Arnold', hand=h, score=15)
    assert p.name == 'Arnold'
    assert p.hand == h
    assert p.score == 15


def test_load():
    d = {'name': 'Arnold', 'hand': 'ttt taa bee', 'score': 15}
    h_exp = Hand.load('ttt taa bee')
    p_exp = Player(name='Arnold', hand=h_exp, score=15)
    assert str(p_exp) == str(Player.load(d))


def test_save():
    h = Hand.load('ttt taa bee') 
    p = Player(name='Arnold', hand=h, score=15)
    assert str(p) == 'Arnold(15):ttt taa bee'  
    assert p.save() == {'name': 'Arnold', 'hand': 'ttt taa bee', 'score': 15}