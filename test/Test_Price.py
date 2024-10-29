import pytest
from src.price import Price
from src.сard import Card

def test_init():
    p = Price(t=3, b=1, c=2, e=0, a=4)
    assert p.d['t'] == 3
    assert p.d['b'] == 1
    assert p.d['c'] == 2
    assert p.d['e'] == 0
    assert p.d['a'] == 4
    

def test_validate_values():
    with pytest.raises(ValueError):
        q = Price(t=50)

def test_save():
    p = Price(t=3, b=1, c=2, e=0, a=4)
    assert repr(p) == 't:3 b:1 c:2 e:0 a:4 '

def test_eq():
    p1 = Price(t=3, b=1, c=2, e=0, a=4)
    p2 = Price(t=3, b=1, c=2, e=0, a=4)
    assert p1 == p2
    p3 = Price(t=2, b=1, c=2, e=0, a=4)
    assert p1 != p3

def test_add():
    p1 = Price(t=1, b=1, c=2, e=0, a=4)
    p2 = Price(t=1, b=2, c=3, e=0, a=1)
    p1.add(p2)
    assert p1.d['t'] == 2
    assert p1.d['b'] == 3
    assert p1.d['c'] == 5
    assert p1.d['e'] == 0
    assert p1.d['a'] == 5 